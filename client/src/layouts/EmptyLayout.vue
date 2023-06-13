<script setup lang="ts">
import HeaderLogo from '@/components/ui/HeaderLogo.vue'
import { PMenu, PToast } from '@/uiComponents'
import { user } from '@/composable/fetchUser'
import { logout } from '@/utils/api/Auth'
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'

const $router = useRouter()

const items = computed(() => {
  if (user.value) {
    return [
      {
        label: 'Профиль',
        icon: 'pi pi-user',
        command: () => {
          $router.push(`/profile/${user.value!.id}`)
        }
      },
      {
        label: 'Выйти',
        icon: 'pi pi-sign-out',
        command: () => {
          logout()
        }
      }
    ]
  }

  return [
    {
      label: 'войти',
      icon: 'pi pi-user',
      command: () => {
        $router.push('/login')
      }
    }
  ]
})

const menu = ref()

const toggle = (event: any) => {
  menu.value.toggle(event)
}
</script>

<template>
  <PToast position="bottom-right" group="br" />

  <header class="header">
    <div class="container">
      <div class="header__content">
        <header-logo />
        <div>
          <div
            aria-haspopup="true"
            aria-controls="overlay_menu"
            class="header__content-user-wrap"
            @click="toggle"
          >
            <span style="font-size: 24px; color: #fff" class="pi pi-user" />
          </div>
          <PMenu id="overlay_menu" ref="menu" :model="items" :popup="true" />
        </div>
      </div>
    </div>
  </header>
  <main class="main">
    <div class="container">
      <slot />
    </div>
  </main>
</template>

<style lang="scss" scoped>
.header__content {
  display: flex;
  justify-content: space-between;
  align-items: center;

  &-user-wrap {
    height: 40px;
    display: flex;
    align-items: center;
  }
}
</style>
