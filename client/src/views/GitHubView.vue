<script setup lang="ts">
import axios from '@/utils/api/axios'
import { onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { setTokens, fetchUser, logout } from '@/utils/api/Auth'
import { user } from '@/composable/fetchUser'
const $route = useRoute()
const $router = useRouter()

const googleAuthenticate = async (state: string, code: string) => {
    if (state && code && !localStorage.getItem('access')) {
        const config = {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        }

        const details = {
            'state': state,
            'code': code
        }

        const formBody = Object.keys(details).map(key => encodeURIComponent(key) + '=' + encodeURIComponent(details[key as keyof typeof details])).join('&')

        try {
            const res = await axios.post(`${import.meta.env.VITE_BASE_URL}/djoser/o/github/?${formBody}`, config)

            setTokens({
              access: res.data.access,
              refresh: res.data.refresh
            })
            await fetchUser()
        } catch (err) {
          console.log(err)
        }
    }
}


onMounted(() => {
  const query = $route.query

  googleAuthenticate(query.state as string, query.code as string)
    .then(() => {
      $router.push(`/profile/${user.value?.id}`)
    })
    .catch(() => {
      logout()
      $router.push('/')
    })
})

</script>

<template>
  <div>
  </div>
</template>

<style lang="scss" scoped>
.HomeView {
  &__left {
    position: sticky;

    > * {
      &:not(:last-child) {
        margin-bottom: step(6);
      }
    }
  }
}
</style>
