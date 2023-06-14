<script lang="ts" setup>
import PartitionList from '@/components/parts/layout/PartitionList.vue'
import ReadingBlogsList from '@/components/parts/layout/ReadingBlogsList.vue'
import TopBlogs from '@/components/parts/layout/TopBlogs.vue'
import ColumnCustomScroll from '@/components/ui/ColumnCustomScroll.vue'
</script>

<template>
  <column-custom-scroll>
    <partition-list v-if="false" />
    <top-blogs />
    <reading-blogs-list />
  </column-custom-scroll>
</template>
