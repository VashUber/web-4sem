<script setup lang="ts">
import Api from '@/utils/api/Api'
import type { IPartitionsRaw } from '@/models/Partitions'
import { onMounted, ref } from 'vue'

const partitions = ref<IPartitionsRaw[]>([])

onMounted(async () => {
  await Api.fetchPartitions().then((res) => {
    partitions.value = res
  })
})
</script>

<template>
  <div class="PartitionList main-left-column-card">
    <div v-for="(partition, index) in partitions" :key="index" class="PartitionList__item">
      {{ partition.title }}
    </div>
  </div>
</template>

<style lang="scss" scoped>
.PartitionList {
  display: flex;
  flex-direction: column;
  margin: step(-1) 0;

  &__item {
    margin: step(1) 0;
    font-weight: 500;
    font-size: 20px;
  }
}
</style>
