<script lang="ts" setup>
import type { IArticle } from '@/models/Articles'
import Api from '@/utils/api/Api'
import { onMounted, ref } from 'vue'

const blogs = ref<IArticle[]>([])

onMounted(async () => {
  await Api.fetchTopBlogs().then((res) => {
    blogs.value = res
  })
})
</script>

<template>
  <div class="TopBlogs main-left-column-card">
    <div class="TopBlogs__title">Топ блоги</div>
    <div class="TopBlogs__list">
      <router-link
        :to="`/article/${blog.id}`"
        v-for="blog in blogs"
        :key="blog.id"
        class="TopBlogs__list-item"
      >
        <div class="TopBlogs__list-item__img-wrap">
          <img class="TopBlogs__list-item__img" :src="blog.author_data.avatar" />
        </div>
        <div class="TopBlogs__list-item__title">
          {{ blog.title }}
        </div>
      </router-link>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.TopBlogs {
  &__title {
    margin-bottom: step(3);
    font-size: 20px;
    font-weight: bold;
    text-transform: uppercase;
  }

  &__list {
    &-item {
      display: flex;

      &:not(:last-child) {
        margin-bottom: step(4);
      }

      &__img {
        width: 30px;
        height: 30px;
        margin-right: step(2);
        border-radius: $radius-1;
      }

      &__title {
        font-size: 16px;

        color: $gray-500;
      }
    }
  }
}
</style>
