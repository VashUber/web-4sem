<script setup lang="ts">
const props = defineProps({
  id: {
    type: String,
    default: ''
  }
})
</script>

<template>
  <div class="FormFieldWrap">
    <label v-if="$slots['default']" class="FormFieldWrap__label" :for="props.id">
      <slot />
    </label>
    <slot name="content" v-bind="{ id: props.id }" />
  </div>
</template>

<style lang="scss">
.FormFieldWrap {
  display: flex;
  flex-direction: column;

  &__label {
    font-size: 18px;
    line-height: 100%;
    font-weight: 500;
    margin-bottom: step(2);
  }
}
</style>
