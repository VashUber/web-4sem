<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'

const props = defineProps({
  active: {
    type: Boolean,
    default: () => true
  },
  distance: {
    type: String,
    default: () => '200px'
  },
  autoLoad: {
    type: Boolean,
    default: () => false
  }
})

const emits = defineEmits(['process'])

const infiniteScrollObserver = ref<Element>()

const getStyle = computed(() => {
  return {
    marginBottom: '-' + props.distance,
    top: '-' + props.distance
  }
})

onMounted(() => {
  if (props.autoLoad) {
    emitEvent()
  }

  observer()
})

const observer = () => {
  const options = {
    rootMargin: '0px',
    threshold: 0
  }

  const callback = (entries: any) => {
    if (props.active && entries[0].isIntersecting) {
      emitEvent()
    }
  }

  const observer = new IntersectionObserver(callback, options)
  if (infiniteScrollObserver.value) {
    observer.observe(infiniteScrollObserver.value)
  }
}

const emitEvent = () => {
  emits('process')
}
</script>

<template>
  <div
    v-if="props.active"
    ref="infiniteScrollObserver"
    class="infiniteScrollObserver"
    :style="getStyle"
  ></div>
</template>

<style scoped>
.infiniteScrollObserver {
  height: 5px;
  position: relative;
}
</style>
