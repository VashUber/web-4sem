<script setup lang="ts">
import { ref } from 'vue'
import type { IArticle } from '@/models/Articles'
import Api from '@/utils/api/Api'
import BlogCard from '@/components/parts/home/BlogCard.vue'
import { useRouter } from 'vue-router'
import InfinityScroll from '@/components/ui/InfinityScroll.vue'

const blogs = ref<IArticle[]>([])
const blogPage = ref(1)
const isLoadMore = ref(true)
const $router = useRouter()

const onGoRead = (id: number): void => {
  $router.push(`article/${id}`)
}

const loaded = ref(false)

const loadMore = async () => {
  if (!loaded.value) {
    loaded.value = true
    await Api.fetchArticles(blogPage.value).then((res) => {
      if (blogPage.value === 1) {
        blogs.value = res.data
      }
      else {
        blogs.value.push(...res.data)
      }
      
      isLoadMore.value = res.count > blogPage.value * res.per_page
      blogPage.value += 1 
    })

    loaded.value = false
  } 
}
</script>

<template>
  <blog-card
    v-for="(blog, index) in blogs"
    :id="blog.id"
    :key="index"
    :author="blog.author_data"
    :img="blog.img"
    :title="blog.title"
    :short-description="blog.content_text"
    :tags="[]"
    @go-read="onGoRead"
  />
  <InfinityScroll
    :active="isLoadMore"
    :auto-load="false"
    @process="loadMore"
  />
</template>
