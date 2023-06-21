<script setup lang="ts">
import { user } from '@/composable/fetchUser'
import { PButton } from '@/uiComponents'

interface ITab {
  title: string
  value: string
  show?: boolean
}

const props = defineProps({
  modelValue: {
    type: String,
    default: ''
  }
})

const emits = defineEmits(['update:modelValue', 'createdArticle'])

const tabs: ITab[] = [
  {
    title: 'Публикации',
    value: 'article'
  },
  {
    title: 'Написать пост',
    value: 'created',
    show: !user.value?.id,
  } 
].filter((el) => !el.show)

const clickTab = (tab: ITab) => {
  if (tab.value === 'created') {
    emits('createdArticle')
    return
  }

  emits('update:modelValue', tab.value)
}
</script>

<template>
  <div class="profile-left-column-card">
    <div class="ProfileTabs">
      <p-button
        v-for="(tab, index) in tabs"
        :key="index"
        class="ProfileTabs__button"
        :outlined="tab.value !== props.modelValue"
        @click="clickTab(tab)"
      >
        {{ tab.title }}
      </p-button>
    </div>
  </div>
</template>

<style lang="scss">
.ProfileTabs {
  display: flex;
  flex-wrap: nowrap;
  overflow-x: auto;
  justify-content: space-between;
  margin: step(-1.5);

  & > * {
    margin: step(1.5);
  }
}

@media screen and (max-width: 470px) {
  .ProfileTabs {
    flex-direction: column;
  }
}
</style>
