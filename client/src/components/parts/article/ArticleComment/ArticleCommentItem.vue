<script lang="ts" setup>
import AuthorBlock from '@/components/ui/AuthorBlock.vue'
import type { IComments } from '@/models/Comments'
import type { PropType } from 'vue'

const props = defineProps({
  comment: {
    type: Object as PropType<IComments>,
    required: true
  },
  parentComment: {
    type: Object as PropType<IComments>,
    default: null
  }
})
</script>

<template>
  <div class="ArticleCommentItem" :style="{
    paddingLeft: props.parentComment ? '12px' : ''
  }">
    <div class="ArticleCommentItem__author">
      <author-block :id="props.comment.author" :avatar="props.comment.author_data.avatar"
        :name="props.comment.author_data.username">
        <template v-if="props.parentComment" #default="{ name }">
          {{ name }} ответ {{ props.parentComment.author_data.username }}
        </template>
      </author-block>
    </div>
    <div class="ArticleCommentItem__comment">
      <div v-text="props.comment.text" />
    </div>
    <div class="ArticleCommentItem__stats">
    </div>
  </div>

  <div class="ArticleCommentItem__answer">
  </div>
</template>

<style lang="scss" scoped>
.ArticleCommentItem {
  margin-top: step(3);

  &__author {
    display: flex;
  }

  &__comment {
    margin-top: step(3);
    @include textWithMobile(16px);
  }

  &__stats {
    margin-top: step(3);
    display: flex;

    &-like {
      display: flex;
      align-items: center;

      &__value {
        margin-left: step(1);
        font-weight: 500;
        @include textWithMobile(16px);
      }

      &__icon {
        font-size: 16px;
      }
    }

    &-answer {
      margin-left: step(5);
      cursor: pointer;
      color: $purple-900;
      @include textWithMobile(20px);
    }
  }
}

@media screen and (max-width: 768px) {
  .ArticleCommentItem {

    &__comment,
    &__stats {
      margin-top: step(2);
    }
  }
}
</style>
