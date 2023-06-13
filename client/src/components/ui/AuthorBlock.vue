<script setup lang="ts">
const props = defineProps({
  name: {
    type: String,
    required: true
  },
  avatar: {
    type: String,
    default: ''
  },
  id: {
    type: Number,
    required: true,
  }
})
</script>

<template>
  <router-link :to="`/profile/${props.id}`" class="ArticleContent__author">
    <slot
      name="avatar"
      v-bind="{
        avatar: props.avatar
      }"
    >
      <img class="ArticleContent__author-img" :src="props.avatar"/>
    </slot>
    <span class="ArticleContent__author-name">
      <slot
        v-bind="{
          name: props.name
        }"
      >
        {{ props.name }}
      </slot>
    </span>
  </router-link>
</template>

<style lang="scss" scoped>
.ArticleContent {
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
}

@media screen and (max-width: 768px) {
  .BlogCard {
    &__author {
      &-img {
        width: 20px;
        height: 20px;
      }
    }
  }
}
</style>
