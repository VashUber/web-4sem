<script setup lang="ts">
import AuthorBlock from '@/components/ui/AuthorBlock.vue'
import type { PropType } from 'vue'
const props = defineProps({
  name: {
    type: String,
    required: true
  },
  avatar: {
    type: String,
    default: ''
  },
  title: {
    type: String,
    required: true
  },
  tags: {
    type: Array as PropType<string[]>,
    default: () => []
  },
  content: {
    type: String,
    required: true
  },
  image: {
    type: String,
    default: null
  },
  author: {
    type: Number,
    required: true,
  }
})
</script>

<template>
  <div class="ArticleContent main-right-column-card">
    <div class="ArticleContent__author">
      <author-block :id="props.author" :name="props.name" :avatar="props.avatar" />
    </div>
    <h1 class="ArticleContent__title">
      {{ props.title }}
    </h1>
    <div class="ArticleContent__tags">
      <div v-for="(tag, index) in props.tags" :key="index" class="ArticleContent__tags-item">
        {{ tag }}
      </div>
    </div>
    <img v-if="props.image" :src="props.image" class="ArticleContent__image" />
    <div class="ArticleContent__content" v-html="content" />
  </div>
</template>

<style lang="scss" scoped>
.ArticleContent {
  &__title {
    margin-top: step(3);
    font-weight: 700;
    @include textWithMobile(25px);
  }

  &__tags {
    margin: step(3) step(-3.5) step(-7);
    display: flex;
    flex-wrap: wrap;

    &-item {
      margin: 0 step(3.5) step(7);
      font-weight: 500;
      color: $gray-500;
      @include textWithMobile(16px);
    }
  }

  &__image {
    display: block;
    margin-top: step(3);
    width: 100%;
    max-height: 400px;
    object-fit: cover;
  }

  &__content {
    margin-top: step(3);
    @include textWithMobile(20px);
  }
}

@media screen and (max-width: 768px) {
  .ArticleContent {
    &__tags {
      margin: step(3) step(-1) step(-2);

      &-item {
        margin: 0 step(1) step(2);
      }
    }

    &__image {
      max-height: 300px;
    }

    &__content {
      font-size: 16px;
    }
  }
}
</style>
