<script setup lang="ts">
import type { IComments } from '@/models/Comments'
import { ref, type PropType } from 'vue'
import { PTextarea, PButton } from '@/uiComponents'
import { user } from '@/composable/fetchUser'
import ArticleCommentItem from './ArticleCommentItem.vue'
import { useRoute } from 'vue-router'
import Api from '@/utils/api/Api'

const props = defineProps({
  comments: {
    type: Array as PropType<IComments[]>,
    default: () => []
  }
})

const emits = defineEmits(['addComment'])

const text = ref('')
const $route = useRoute()

const articleId = +$route.params.id

const onSubmit = async () => {
  await Api.createComments(text.value, user.value!.id, articleId)
    .then((res) => {
      emits('addComment', res)
      text.value = ''
    })
}
</script>

<template>
  <div class="ArticleComments main-right-column-card">
    <h3 class="ArticleComments__title">Комментарии</h3>
    <div v-if="user" class="ArticleComments__form-wrap">
      <h4 class="ArticleComments__form-title">
        Написать комментарий
      </h4>
      <form class="ArticleComments__form" @submit.prevent="onSubmit">
        <PTextarea v-model="text" rows="4" class="ArticleComments__form-textarea"/>
        <PButton class="ArticleComments__form-button" type="submit">Отправить</PButton>
      </form>
    </div>
    <div class="ArticleComments__comments">
      <template v-if="props.comments.length">
        <article-comment-item
          v-for="(comment, index) in props.comments"
          :key="index"
          :comment="comment"
        />
      </template>
      <template v-else>
        Нет комментариев
      </template>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.ArticleComments {
  &__title {
    font-weight: 500;
    @include textWithMobile(20px);
  }

  &__comments {
    margin-top: step(4);
  }

  &__form {
    margin-top: step(2);
    display: flex;
    flex-direction: column;

    &-title {
      font-weight: 500;
    }

    &-textarea {
      resize: none;
      margin-bottom: step(2);
    }

    &-button {
      max-width: 150px;
    }
  }
}
</style>
