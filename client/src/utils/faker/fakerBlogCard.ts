import type { IArticle } from '@/models/Articles'
import { faker } from './faker'
import fakerAuthor from './fakerAuthor'

export default (): IArticle => {
  const author = fakerAuthor()
  return {
    author_data: author,
    id: faker.datatype.number(),
    author: author.id,
    content: `<div>${faker.lorem.text()}</div>`,
    content_text: faker.lorem.text(),
    created_ad: '',
    img: faker.image.abstract(),
    title: faker.lorem.words(3),
  } as IArticle
}
