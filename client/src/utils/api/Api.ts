import type { Pagination } from '@/models'
import type IArticleCreateResponse from '@/models/Articles'
import type { IArticle } from '@/models/Articles'
import type { IComments } from '@/models/Comments'
import type { IPartitionsRaw } from '@/models/Partitions'
import type { IUser } from '@/models/User'
import type { AxiosResponse } from 'axios'
import { faker } from '../faker/faker'
import fakerBlogCard from '../faker/fakerBlogCard'
import fakerBlogList from '../faker/fakerBlogList'
import fakerComment from '../faker/fakerComment'
import fakerComments from '../faker/fakerCommetsList'
import fakerUser from '../faker/fakerUser'
import axios, { regAccessToken, regCSRF } from './axios'

enum AxiosMethodsEnum {
  POST = 'POST',
  GET = 'GET',
  DELETE = 'DELETE',
  PUT = 'PUT'
}

const useApi = import.meta.env.VITE_USE_API

abstract class Api {
  static get useApi() {
    return false
  }

  static async fetchUser(id: number): Promise<IUser> {
    if (useApi) {
      return await this.callFetch<IUser>(`/accounts/${id}`)
    } else {
      return fakerUser()
    }
  }

  static async fetchUserArticle(id: number, page: number): Promise<Pagination<IArticle[]>> {
    if (useApi) {
      return await this.callFetch<Pagination<IArticle[]>>(`/accounts/${id}/article?page=${page}`)
    } else {
      return fakerBlogList()
    }
  }
  static async fetchUserArticleCount(id: number): Promise<number> {
    if (useApi) {
      return await this.callFetch<number>(`/accounts/${id}/counts`)
    } else {
      return faker.datatype.number({ max: 100 })
    }
  }

  static async fetchCurrentArticle(id: number): Promise<IArticle> {
    if (useApi) {
      return await this.callFetch<IArticle>(`/articles/${id}/`)
    } else {
      return fakerBlogCard()
    }
  }

  static async fetchCurrentArticleComments(id: number): Promise<IComments[]> {
    if (useApi) {
      return await this.callFetch<IComments[]>(`/articles/${id}/comments/`, AxiosMethodsEnum.GET)
    }

    return fakerComments()
  }

  static async createComments(text: string, userId: number, articleId: number): Promise<IComments> {
    if (useApi) {
      return await this.callFetch<IComments>('/comments/', AxiosMethodsEnum.POST, {
        text,
        author: userId,
        article: articleId
      })
    } else {
      return fakerComment()
    }
  }
  static async fetchArticles(page = 1): Promise<Pagination<IArticle[]>> {
    if (useApi) {
      return await this.callFetch<Pagination<IArticle[]>>(`/articles/?page=${page}`)
    } else {
      return fakerBlogList()
    }
  }

  static async editArticle(id: number, form: any): Promise<IArticle> {
    if (useApi) {
      return this.callFetch<IArticle>(`/articles/${id}/`, AxiosMethodsEnum.PUT, form)
    } else {
      return fakerBlogCard()
    }
  }

  static async fetchReadingBlogs(): Promise<IArticle[]> {
    if (useApi) {
      return await this.callFetch<IArticle[]>('/articles/read')
    } else {
      return Array.from({ length: 3 }, () => fakerBlogCard())
    }
  }

  static async fetchTopBlogs(): Promise<IArticle[]> {
    if (useApi) {
      return await this.callFetch<IArticle[]>('/articles/top')
    } else {
      return Array.from({ length: 3 }, () => fakerBlogCard())
    }
  }

  static async fetchPartitions(): Promise<IPartitionsRaw[]> {
    if (useApi) {
      return await this.callFetch<IPartitionsRaw[]>('/partitions/index')
    } else {
      return Array.from({ length: 5 }, () => {
        const code = faker.word.adjective({
          length: {
            max: 10,
            min: 4
          }
        })
        return {
          title: faker.lorem.words(1),
          code
        }
      }) as IPartitionsRaw[]
    }
  }

  static async createArticle(data: any): Promise<IArticleCreateResponse> {
    if (useApi) {
      return this.callFetch<any>('/articles/', AxiosMethodsEnum.POST, data)
    } else {
      return fakerBlogCard()
    }
  }

  private static callFetch<T = any>(
    endpoint: string,
    method: AxiosMethodsEnum = AxiosMethodsEnum.GET,
    args?: any,
    headers?: Record<string, string>
  ): Promise<T> {
    return new Promise((resolve, reject) => {
      const headersAuth = {} as Record<string, string>

      const accessToken = localStorage.getItem('access')
      const CSRF = document.cookie.match(regCSRF)?.[0]

      if (CSRF) {
        headersAuth['X-CSRFToken'] = CSRF
      }

      if (accessToken) {
        headersAuth.Authorization = 'JWT ' + localStorage.getItem('access')
      }

      axios({
        method,
        url: endpoint,
        data: args,
        headers: {
          ...headers,
          ...headersAuth
        }
      })
        .then((res: AxiosResponse<T>) => {
          resolve(res.data)
        })
        .catch((err) => {
          reject(err)
        })
    })
  }
}

export default Api
