import type { IComments } from '@/models/Comments'
import { faker } from '@faker-js/faker'
import fakerAuthor from './fakerAuthor'

export default (): IComments => {
  const author = fakerAuthor()
  return {
    article: 0,
    created_at: '',
    text: faker.lorem.text(),
    author_data: author,
    author: author.id,
    id: faker.datatype.number(),
  }
}