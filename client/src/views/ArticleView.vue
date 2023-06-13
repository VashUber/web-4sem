<script lang="ts" setup>
import ArticleComments from '@/components/parts/article/ArticleComment/ArticleComments.vue'
import ArticleContent from '@/components/parts/article/ArticleContent/ArticleContent.vue'
import type { IArticle } from '@/models/Articles'
import type { IComments } from '@/models/Comments'
import Api from '@/utils/api/Api'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

const blog = ref<IArticle>()
const comments = ref<IComments[]>([])
const $route = useRoute()

onMounted(async () => {
  await Api.fetchCurrentArticle(+$route.params.id).then((res) => {
    blog.value = res
  })

  await Api.fetchCurrentArticleComments(+$route.params.id).then((res) => {
    comments.value = res
  })
})

const onAddComments = (comment: IComments) => {
  comments.value.unshift(comment)
}
</script>

<template>
  <div v-if="blog">
    <article-content
      :avatar="blog.author_data.avatar"
      :name="blog.author_data.username" :title="blog.title" :content="blog.content" :image="blog.img"
      :author="blog.author" />
  </div>
  <div>
    <article-comments :comments="comments"  @add-comment="onAddComments"/>
  </div>
</template>
