import type { IComments } from '@/models/Comments'
import { faker } from './faker'
import fakerComment from './fakerComment'

const fakerComments = (): IComments[] => {
  return Array.from({ length: faker.datatype.number({ min: 1, max: 3 }) }, fakerComment)
}

export default fakerComments
