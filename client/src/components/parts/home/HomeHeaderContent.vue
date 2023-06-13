<script setup lang="ts">
import SortSelect from '@/components/ui/SortSelect.vue'
import { onMounted, ref, watch } from 'vue'
import { useRouter } from 'vue-router'

const types = ref([
  {
    title: 'Статьи',
    code: 'articles'
  },
  {
    title: 'Новости',
    code: 'news'
  }
])

const sort = ref('all')

const $router = useRouter()

const sortItems = [
  {
    title: 'Все подряд',
    value: 'all'
  },
  {
    title: 'Самые популярные',
    value: 'popular'
  }
]

onMounted(async () => {
  $router.replace({
    query: {
      sort: sort.value
    }
  })
})

watch(sort, async (newValue) => {
  $router?.replace({
    query: {
      sort: newValue
    }
  })
})
</script>

<template>
  <div class="HomeHeaderContent main-right-column-card">
    <div class="HomeHeaderContent__title">Все разделы</div>
    <div class="HomeHeaderContent__content">
      <div class="HomeHeaderContent__content-list">
        <div
          v-for="(type, index) in types"
          :key="index"
          class="HomeHeaderContent__content-list__item"
        >
          {{ type.title }}
        </div>
      </div>
      <div class="HomeHeaderContent__content-sort">
        <sort-select v-model="sort" :options="sortItems" />
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.HomeHeaderContent {
  &__title {
    font-weight: 700;
    font-size: 25px;
    margin-bottom: step(3);
  }

  &__content {
    display: flex;
    align-items: center;
    justify-content: space-between;

    &-list {
      display: flex;
      margin: 0 step(-2);

      &__item {
        font-weight: 500;
        @include textWithMobile(20px);
        margin: 0 step(2);
        color: $gray-500;
      }
    }
  }
}

@media screen and (max-width: 768px) {
  .HomeHeaderContent {
    &__title {
      display: none;
    }

    &__content {
      display: block;

      &-sort {
        margin-top: step(2);
      }
    }
  }
}
</style>
