<script setup lang="ts">
import { PChips } from '@/uiComponents'
import { computed } from 'vue'
import FormFieldWrap from './FormFieldWrap.vue'

const props = defineProps({
  modelValue: {
    type: Array,
    default: () => [],
    required: false
  },
  id: {
    type: String,
    default: ''
  }
})

const emits = defineEmits(['update:modelValue'])

const value_ = computed({
  get() {
    return props.modelValue
  },
  set(v) {
    emits('update:modelValue', v)
  }
})
</script>

<template>
  <FormFieldWrap :id="id">
    <slot />
    <template #content>
      <PChips v-bind="$attrs" v-model="value_" :input-id="id" class="CustomInputChips__input" />
    </template>
  </FormFieldWrap>
</template>

<style lang="scss">
.CustomInputChips__input {
  .p-inputtext {
    width: 100%;
  }
}
</style>
