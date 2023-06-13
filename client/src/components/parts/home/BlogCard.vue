<script setup lang="ts">
import AuthorBlock from '@/components/ui/AuthorBlock.vue'
import type { IAuthor } from '@/models/Author'
import { PButton } from '@/uiComponents'
import type { PropType } from 'vue'

const props = defineProps({
  author: {
    type: Object as PropType<IAuthor>,
    default: null
  },
  title: {
    type: String,
    required: true
  },
  shortDescription: {
    type: String,
    required: true
  },
  tags: {
    type: Array as PropType<string[]>,
    required: true
  },
  img: {
    type: String,
    default: null
  },
  id: {
    type: Number,
    required: true
  },
})

const emits = defineEmits(['goRead'])

const onClickBlogCard = (): void => {
  if (window.innerWidth <= 768) {
    emits('goRead', props.id)
  }
}
</script>

<template>
  <div class="BlogCard main-right-column-card" @click="onClickBlogCard">
    <div v-if="props.author" class="BlogCard__author">
      <author-block :id="props.author.id" :avatar="props.author.avatar" :name="props.author.username" />
    </div>
    <div class="BlogCard__title">
      {{ props.title }}
    </div>
    <div v-if="props.tags.length" class="BlogCard__tags">
      <div v-for="(tag, index) in props.tags" :key="index" class="BlogCard__tags-item">
        {{ tag }}
      </div>
    </div>
    <div v-if="props.img" class="BlogCard__img-wrap">
      <img class="BlogCard__img" :src="props.img"/>
    </div>
    <div class="BlogCard__description">
      {{ props.shortDescription }}
    </div>
    <div class="BlogCard__btn-wrap">
      <slot name="buttons">
        <router-link :to="`/article/${props.id}`">
          <p-button class="BlogCard__btn"> Читать статью </p-button>
        </router-link>
      </slot>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.BlogCard {
  padding-top: step(6);
  padding-bottom: step(6);
  &__author {
    display: flex;
    align-items: center;

    &-img {
      width: 30px;
      height: 30px;
      border-radius: $radius-1;
      margin-right: step(2);
    }

    &-name {
      color: $gray-500;
      @include textWithMobile(16px);
    }
  }

  &__title {
    margin-top: step(2);
    font-weight: bold;
    @include textWithMobile(25px);
  }

  &__tags {
    display: flex;
    flex-wrap: wrap;
    margin: step(-1.5);
    margin-top: step(2 - 1.5);

    &-item {
      font-weight: 500;
      margin: step(1.5);
      padding: step(1) step(1.5);
      border: 1px solid $purple-900;
      border-radius: $radius-2;
      @include textWithMobile(13px);
    }
  }

  &__img {
    width: 100%;
    max-height: 400px;
    object-fit: cover;

    &-wrap {
      margin-top: step(2);
    }
  }

  &__description {
    font-weight: 500;
    margin-top: step(5);
    @include textWithMobile(16px);
  }

  &__btn {
    padding: step(1) step(4);
    font-weight: 500;
    font-size: 16px;
    &-wrap {
      margin-top: step(3);
    }
  }
}

@media screen and (max-width: 768px) {
  .BlogCard {
    &__author {
      &-img {
        width: 20px;
        height: 20px;
      }
    }

    &__description {
      margin-top: step(2);
    }

    &__btn {
      display: none;
    }
  }
}
</style>
