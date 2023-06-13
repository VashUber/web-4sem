<script setup lang="ts">
import { PButton } from '@/uiComponents'
import type { IArticle } from '@/models/Articles'
import type { PropType } from 'vue'
import BlogCard from '../home/BlogCard.vue'
import InfinityScroll from '@/components/ui/InfinityScroll.vue'
import { user } from '@/composable/fetchUser'
const props = defineProps({
  articles: {
    type: Array as PropType<IArticle[]>,
    default: () => []
  },
  isLoadMore: Boolean
})

const emits = defineEmits(['process'])
</script>

<template>
  <template v-if="props.articles.length">
    <BlogCard v-for="article in articles" :id="article.id" :key="article.id" class="ProfileArticleList" :img="article.img"
      :short-description="article.content_text" :tags="[]" :title="article.title">
      <template #buttons>
        <router-link v-if="user?.id === article.author" :to="`/edit/${article.id}`">
          <p-button> Редактировать </p-button>
        </router-link>
      </template>
    </BlogCard>
    <InfinityScroll :active="props.isLoadMore" @process="emits('process')"/>
  </template>
  <template v-else>
    <div class="ProfileArticleList__empty profile-left-column-card">Нет постов</div>
  </template>
</template>
