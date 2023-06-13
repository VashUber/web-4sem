<script lang="ts" setup>
import { onMounted, onUnmounted, ref, watch } from 'vue'

const column = ref<HTMLDivElement>()

const columnStickyTop = ref(false)
const columnStickyBottom = ref(false)

const isHeightColumnMoreScreen = ref(false)

const prevScrollY = ref(window.scrollY)
const scrollUp = ref(window.scrollY < prevScrollY.value)

const addMarginTop = () => {
  if (column.value) {
    column.value.style.marginTop = column.value.offsetTop - 84 + 'px'
  }
}

const onScroll = (): void => {
  scrollUp.value = window.scrollY < prevScrollY.value

  if (column.value) {
    isHeightColumnMoreScreen.value = window.innerHeight < column.value.clientHeight
    columnStickyBottom.value =
      Math.ceil(window.innerHeight - column.value.getBoundingClientRect().bottom) >= 24
    columnStickyTop.value = Math.ceil(column.value.getBoundingClientRect().top) >= 24
  }

  if (isHeightColumnMoreScreen.value) {
    if (
      (scrollUp.value && columnStickyBottom.value) ||
      (!scrollUp.value && columnStickyTop.value)
    ) {
      addMarginTop()
    }
  }

  prevScrollY.value = window.scrollY
}

watch(
  () => columnStickyBottom.value || columnStickyTop.value,
  (newValue) => {
    if (newValue && column.value) {
      column.value.style.marginTop = ''
    }
  }
)

onMounted(() => {
  onScroll()
  window.addEventListener('scroll', onScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', onScroll)
})
</script>

<template>
  <div
    ref="column"
    class="ColumnCustomScroll"
    :class="{
      ColumnCustomScroll__sticky: columnStickyBottom && !scrollUp,
      'ColumnCustomScroll__sticky-top': (columnStickyTop && scrollUp) || !isHeightColumnMoreScreen
    }"
  >
    <slot />
  </div>
</template>

<style lang="scss">
.ColumnCustomScroll {
  height: min-content;

  > * {
    &:not(:last-child) {
      margin-bottom: step(6);
    }
  }

  &__sticky {
    margin-top: auto;
    position: sticky;
    bottom: 24px;

    &-top {
      position: sticky;
      margin-top: 0;
      top: 24px;
    }
  }
}
</style>
