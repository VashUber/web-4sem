<script setup lang="ts">
import LayoutLeftColumnInfo from '@/components/parts/layout/LayoutLeftColumnInfo.vue'
import EmptyLayout from './EmptyLayout.vue'
</script>

<template>
  <empty-layout>
    <div class="main__content">
      <layout-left-column-info class="main__content-left_column" />
      <div class="DefaultLayout__right">
        <slot />
      </div>
    </div>
  </empty-layout>
</template>

<style lang="scss">
.DefaultLayout {
  &__right {
    > * {
      &:not(:last-child) {
        margin-bottom: step(6);
      }
    }
  }
}

@media screen and (max-width: 768px) {
  .DefaultLayout {
    &__right {
      > * {
        &:not(:last-child) {
          margin-bottom: step(3);
        }
      }
    }
  }
}
</style>
