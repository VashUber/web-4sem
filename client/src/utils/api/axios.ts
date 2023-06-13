import $axios from 'axios'
import { logout, refreshToken } from './Auth'
export const regAccessToken = /(?<=\baccess=).*?(?=(;|$))/gi

const axios = $axios.create({
  baseURL: import.meta.env.VITE_BASE_URL,
  headers: {
    Authorization: 'Bearer ' + document.cookie.match(regAccessToken)?.[0]
  }
})

function createAxiosResponseInterceptor() {
  const interceptor = axios.interceptors.response.use(
    (response) => response,
    (error) => {
      
      if (error?.response?.status !== 401) {
        return Promise.reject(error)
      }

      if (error.request.responseURL === import.meta.env.VITE_BASE_URL + '/auth/jwt/refresh/') {
        return Promise.reject(error)
      }

      axios.interceptors.response.eject(interceptor)

      const handler = async () => {
        try {
          await refreshToken()
        } catch (error) {
          logout()
        }
        finally {
          createAxiosResponseInterceptor()
        }
      }
      return handler() 
    }
  )
}

createAxiosResponseInterceptor()

export default axios
