import type { Authordata } from '.'
export interface IComments {
  id: number
  author_data: Authordata
  text: string
  created_at: string
  author: number
  article: number
}
