import { setUser, user } from '@/composable/fetchUser'
import type { IToken } from '@/models/Token'
import type { IUser } from '@/models/User'
import type { AxiosResponse } from 'axios'
import axios, { regAccessToken, regSessionId } from './axios'

const reg = /(?<=\baccess=).*?(?=(;|$))/gi

interface ILoginRes {
  access: string
  refresh: string
}

export interface IFormRegistration {
  email: string
  name: string
  password: string
  password_confirm: string
  avatar?: File
}

interface IFormRegistrationRequest {
  user: IUser
  token: IToken
}

const registration = async (form: IFormRegistration) => {
  const formData = new FormData()
  formData.append('email', form.email)
  formData.append('username', form.name)
  formData.append('password', form.password)
  formData.append('re_password', form.password_confirm)
  formData.append('password2', form.password_confirm)
  if (form.avatar) {
    formData.append('avatar', form.avatar)
  }

  await axios({
    method: 'POST',
    url: '/accounts/register',
    data: formData
  }).then(({ data }: AxiosResponse<IFormRegistrationRequest>) => {
    setTokens(data.token)
    setUser(data.user)

    redirectProfile()
  })
}

const login = async (email: string, password: string) => {
  await axios({
    method: 'POST',
    url: import.meta.env.VITE_BASE_URL + '/djoser/jwt/create/',
    data: {
      email,
      password
    }
  })
    .then(({ data }: AxiosResponse<ILoginRes>) => {
      setTokens(data)
    })
    .then(fetchUser)
    .then(redirectProfile)
}

const fetchUser = async () => {
  const accessToken = localStorage.getItem('access')

  try {
    const headers = {} as Record<string, string>

    if (accessToken) {
      headers.Authorization = 'JWT ' + accessToken
    }
    
    return await axios({
      method: 'GET',
      url: import.meta.env.VITE_BASE_URL + '/djoser/users/me/',
      headers
    })
      .then(({ data }) => {
        setUser(data)
      })
      .catch(() => {
        refreshToken()
      })
  } catch (err) {
    console.log(err)
  }
}

const redirectProfile = () => {
  window.location.replace(`/profile/${user.value?.id}`)
}

const setTokens = (data: IToken) => {
  localStorage.setItem('refresh', data.refresh)
  localStorage.setItem('access', data.access)
}

const refreshToken = async () => {
  const tokenRefresh = localStorage.getItem('refresh')

  if (!tokenRefresh) return

  return new Promise((resolve, reject) => {
    axios({
      method: 'POST',
      url: import.meta.env.VITE_BASE_URL + '/djoser/jwt/refresh/',
      data: {
        refresh: localStorage.getItem('refresh')
      }
    })
      .then(({ data }: AxiosResponse<{ access: string }>) => {
        document.cookie = `access=${data.access}`
        resolve(null)
      })
      .catch((err) => {
        logout()
        reject(err)
      })
  })
}

const logout = () => { 
  localStorage.removeItem('refresh')
  localStorage.removeItem('access')
  setUser(undefined)
}

export { login, fetchUser, refreshToken, logout, registration, setTokens }
