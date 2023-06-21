import $axios from 'axios'
import { logout, refreshToken } from './Auth'
export const regAccessToken = /(?<=\baccess=).*?(?=(;|$))/gi
export const regCSRF = /(?<=\bcsrftoken=).*?(?=(;|$))/gi
export const regSessionId = /(?<=\bsessionid=).*?(?=(;|$))/gi

const accessToken = localStorage.getItem('access')
const CSRF = document.cookie.match(regCSRF)?.[0]

const headers = {} as Record<string, string>

if (accessToken) {
  headers.Authorization = 'JWT ' + accessToken
}

if (CSRF) {
  headers['X-CSRFToken'] = CSRF
}

const axios = $axios.create({
  baseURL: import.meta.env.VITE_BASE_URL,
  withCredentials: true,
  headers,
})

function createAxiosResponseInterceptor() {
  const interceptor = axios.interceptors.response.use(
    (response) => response,
    (error) => {
      if (error?.response?.status !== 401) {
        return Promise.reject(error)
      }

      if (error.request.responseURL === import.meta.env.VITE_BASE_URL + '/djoser/jwt/refresh/') {
        return Promise.reject(error)
      }

      axios.interceptors.response.eject(interceptor)

      const handler = async () => {
        try {
          await refreshToken()
        } catch (error) {
          logout()
        } finally {
          createAxiosResponseInterceptor()
        }
      }
      return handler()
    }
  )
}

createAxiosResponseInterceptor()

export default axios
