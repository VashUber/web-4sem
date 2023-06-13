<script setup lang="ts">
import BlogList from '@/components/parts/home/BlogList.vue'
import HomeHeaderContent from '@/components/parts/home/HomeHeaderContent.vue'
</script>

<template>
  <home-header-content />
  <blog-list />
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
