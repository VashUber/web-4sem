<script lang="ts" setup>
import { onMounted, ref } from 'vue'
import Api from '@/utils/api/Api'
import type { IArticle } from '@/models/Articles'
const blogs = ref<IArticle[]>([])

onMounted(async () => {
  await Api.fetchReadingBlogs().then((res) => {
    blogs.value = res
  })
})
</script>

<template>
  <div class="BlogsList main-left-column-card">
    <div class="BlogsList__title">ЧИТАЮТ СЕЙЧАС</div>
    <div class="BlogsList__list">
      <router-link
        :to="`/article/${blog.id}`"
        v-for="blog in blogs"
        :key="blog.id"
        class="BlogsList__list-item"
      >
        {{ blog.content_text }}
      </router-link>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.BlogsList {
  &__title {
    margin-bottom: step(3);
    font-size: 20px;
    font-weight: bold;
    text-transform: uppercase;
  }

  &__list {
    &-item {
      display: flex;
      cursor: pointer;
      padding: step(1);
      color: black;
      border: 1px solid black;
      overflow: hidden;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;

      &:not(:last-child) {
        margin-bottom: step(4);
      }
    }
  }
}
</style>
