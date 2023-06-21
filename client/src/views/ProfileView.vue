<script setup lang="ts">
import ProfileArticleList from '@/components/parts/profile/ProfileArticleList.vue'
import ProfileCard from '@/components/parts/profile/ProfileCard.vue'
import ProfileRightColumn from '@/components/parts/profile/ProfileRightColumn.vue'
import ProfileStats from '@/components/parts/profile/ProfileStats.vue'
import ProfileTabs from '@/components/parts/profile/ProfileTabs.vue'
import { user } from '@/composable/fetchUser'
import type { IArticle } from '@/models/Articles'
import type { IUser } from '@/models/User'
import Api from '@/utils/api/Api'
import _ from 'lodash'
import { computed, onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const $route = useRoute()
const $router = useRouter()

const userData = ref<IUser>()
const count = ref(0)
const isMyProfile = computed(() => {
  return user.value?.id === +$route.params.id
})

const articles = ref<IArticle[]>([])
const articlesPage = ref(1)

const currentTab = ref('article')

onMounted(async () => {
  if (isMyProfile.value && user.value) {
    userData.value = _.cloneDeep<IUser>(user.value)
  } else {
    await Api.fetchUser(+$route.params.id).then((res) => {
      userData.value = res
    })
  }

  await Api.fetchUserArticleCount
  await loadMore()
})

const isLoadMore = ref(false)

const loadMore = async () => {
  await Api.fetchUserArticle(+$route.params.id, articlesPage.value).then((res) => {
    isLoadMore.value = res.count > articlesPage.value * res.per_page
    count.value = res.count
    articlesPage.value += 1
    articles.value.push(...res.data)
  })
}

const redirectOnCreate = () => {
  $router.push('/create')
}
</script>

<template>
  <div v-if="userData">
    <div class="main__content ProfileView__content">
      <div class="ProfileView__content-right">
        <profile-card :name="userData.username" :avatar="userData.avatar" />
        <profile-stats
          class="ProfileView__stats"
          :count-articles="'0'"
          :created-ad="userData.created_ad"
        />

        <profile-tabs v-model="currentTab" @created-article="redirectOnCreate" />

        <profile-article-list
          v-if="currentTab === 'article'"
          :is-load-more="isLoadMore"
          :articles="articles"
          @process="loadMore"
        />
      </div>
      <div class="main__content-left_column">
        <profile-right-column :count-articles="count" :created-ad="userData.created_ad" />
      </div>
    </div>
  </div>
</template>

<style lang="scss">
.ProfileView {
  &__content {
    grid-template-columns: 5fr 2fr;

    &-right {
      > *:not(:last-child) {
        margin-bottom: step(6);
      }
    }
  }
}
@media screen and (min-width: 992px) {
  .ProfileView {
    &__stats {
      display: none;
    }
  }
}
</style>
