export interface Authordata {
  username: string
  id: number
  email: string
  avatar?: string
}

export type Pagination<T> = {
  count: number
  per_page: number
  data: T
}
