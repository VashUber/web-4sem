import type { IUser } from '@/models/User'
import { faker } from './faker'

export default (): IUser => ({
  created_ad: '',
  is_active: false,
  is_admin: false,
  name: faker.name.firstName(),
  last_login: '',
  email: faker.internet.email(),
  id: faker.datatype.number(),
  avatar: faker.image.avatar(),
})
