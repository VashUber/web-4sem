<script setup lang="ts">
import dayjs from '@/utils/dayjs'
const props = defineProps({
  createdAd: {
    type: String,
    required: true
  },
  countArticles: {
    type: [String, Number],
    required: true
  }
})
</script>

<template>
  <div class="ProfileStats main-right-column-card">
    <h3 class="ProfileStats__title">Дополнительная информация</h3>
    <div class="ProfileStats__item">
      <span> Зарегистрирован: </span>
      <span>
        {{ dayjs(props.createdAd).format('DD.MM.YYYY') }}
      </span>
    </div>
    <div class="ProfileStats__item">
      <span> Количество публикаций: </span>
      <span>
        {{ props.countArticles }}
      </span>
    </div>
  </div>
</template>

<style lang="scss">
.ProfileStats {
  &__title {
    @include textWithMobile(25px);
  }

  &__item {
    margin-top: step(3);
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    @include textWithMobile(16px);
  }
}
</style>
