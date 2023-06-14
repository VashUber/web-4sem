import type { Pagination } from '@/models'
import type { IArticle } from '@/models/Articles'
import { faker } from './faker'
import fakerBlogCard from './fakerBlogCard'

export default (): Pagination<IArticle[]> => {
  const count = faker.datatype.number({ min: 3, max: 8 })
  return {
    count: count,
    per_page: 10,
    data: Array.from({ length: count }, () => fakerBlogCard())
  }
}
