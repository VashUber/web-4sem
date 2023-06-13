<script lang="ts" setup>
import { computed, defineAsyncComponent } from 'vue'
import { useRoute } from 'vue-router'

const Default = defineAsyncComponent(() => import('@/layouts/DefaultLayout.vue'))
const Empty = defineAsyncComponent(() => import('@/layouts/EmptyLayout.vue'))

const route = useRoute()

const layouts = {
  Default,
  Empty
}

const layout = computed(() => {
  const layout = route?.meta?.layout as keyof typeof layouts

  if (layout) {
    return layouts[layout]
  }

  return 'div'
})
</script>

<template>
  <component :is="layout">
    <router-view />
  </component>
</template>
