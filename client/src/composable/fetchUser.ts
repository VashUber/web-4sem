import type { IUser } from '@/models/User'
import { ref } from 'vue'

export const user = ref<IUser>()

export const setUser = (userData: any) => {
  user.value = userData
}
