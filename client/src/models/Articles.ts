import type { Authordata } from '.'

export default interface IArticleCreateResponse {
  id: number
  author_data: Authordata
  created_ad: string
  title: string
  content: string
  content_text: string
  img: string
  author: number
}

export interface IArticle {
  id: number
  author_data: Authordata
  created_ad: string
  title: string
  content: string
  content_text: string
  img: string
  author: number
}
