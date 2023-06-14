<script setup lang="ts">
import ColumnCustomScroll from '@/components/ui/ColumnCustomScroll.vue'
import ProfileStats from './ProfileStats.vue'

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
  <column-custom-scroll>
    <profile-stats :created-ad="props.createdAd" :count-articles="props.countArticles" />
  </column-custom-scroll>
</template>
