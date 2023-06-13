import { setUser, user } from '@/composable/fetchUser'
import type { IToken } from '@/models/Token'
import type { IUser } from '@/models/User'
import type { AxiosResponse } from 'axios'
import axios from './axios'

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
  formData.append('name', form.name)
  formData.append('password', form.password)
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
    url: import.meta.env.VITE_BASE_URL + '/accounts/login',
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
  const tokenRefresh = localStorage.getItem('refresh')

  if (!tokenRefresh) {
    logout()
    return
  }

  // try {
  await refreshToken()
  // } catch (error) {
  //   return
  // }

  try {
    return await axios({
      method: 'GET',
      url: import.meta.env.VITE_BASE_URL + '/accounts/current',
      headers: {
        Authorization: 'Bearer ' + document.cookie.match(reg)?.[0]
      }
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
  document.cookie = `access=${data.access}`
  localStorage.setItem('refresh', data.refresh)
}

const refreshToken = async () => {
  const tokenRefresh = localStorage.getItem('refresh')

  if (!tokenRefresh) return

  return new Promise((resolve, reject) => {
    axios({
      method: 'POST',
      url: import.meta.env.VITE_BASE_URL + '/accounts/refresh',
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
  axios({
    method: 'POST',
    url: import.meta.env.VITE_BASE_URL + '/accounts/logout',
    data: {
      refresh: localStorage.getItem('refresh')
    }
  }).then(() => {
    document.cookie = 'access='
    localStorage.removeItem('refresh')
    setUser(undefined)
  })
}

export { login, fetchUser, refreshToken, logout, registration }
