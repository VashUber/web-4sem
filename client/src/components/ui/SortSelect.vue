<script lang="ts" setup>
import { PSelect } from '@/uiComponents'
import { computed, type PropType } from 'vue'

interface IOptions {
  [key: string]: unknown
}

const props = defineProps({
  modelValue: {
    type: String,
    default: 'all'
  },
  options: {
    type: Array as PropType<IOptions[]>,
    default: () => [
      {
        title: 'Всё подряд',
        value: 'all'
      }
    ]
  },
  optionLabel: {
    type: String,
    default: 'title'
  },
  optionValue: {
    type: String,
    default: 'value'
  }
})

const emits = defineEmits(['update:modelValue'])

const value = computed({
  get() {
    return props.modelValue
  },
  set(v) {
    emits('update:modelValue', v)
  }
})
</script>

<template>
  <p-select
    v-model="value"
    class="SortSelect"
    :options="options"
    :option-label="optionLabel"
    :option-value="optionValue"
  />
</template>

<style lang="scss">
.SortSelect {
  &.p-dropdown {
    background: transparent;
    border: none;
    border-radius: 0px;

    .p-dropdown-label {
      padding: 0;
      margin-right: step(1);
      @include textWithMobile(20px);
    }

    .p-dropdown-trigger {
      width: auto;
    }
  }
}
</style>
