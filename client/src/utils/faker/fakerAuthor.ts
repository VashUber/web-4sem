import type { IAuthor } from '@/models/Author'
import { faker } from './faker'

export default (): IAuthor => ({
  id: faker.datatype.number(),
  email: faker.internet.email(),
  username: faker.name.firstName(),
  avatar: faker.image.avatar()
})
