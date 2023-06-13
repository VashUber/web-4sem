<script setup lang="ts">
import { PInputText } from '@/uiComponents'
import { computed } from 'vue'
import FormFieldWrap from './FormFieldWrap.vue'

const props = defineProps({
  modelValue: {
    type: String,
    default: '',
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
      <PInputText v-bind="$attrs" :id="id" v-model="value_" class="CustomInput__input" />
    </template>
  </FormFieldWrap>
</template>
