<script setup lang="ts">
import { PEditor } from '@/uiComponents'
import type { EditorTextChangeEvent } from 'primevue/editor'
import { computed } from 'vue'

const props = defineProps({
  modelValue: {
    type: String,
    default: ''
  },
  text: {
    type: String,
    default: ''
  }
})

const emits = defineEmits(['update:modelValue', 'update:text'])

const value_ = computed({
  get() {
    return props.modelValue
  },
  set(v) {
    emits('update:modelValue', v)
  }
})

const toolbar = [
  ['bold', 'italic', 'underline', 'strike'],
  ['blockquote', 'code-block'],

  [{ header: 1 }, { header: 2 }],
  [{ list: 'ordered' }, { list: 'bullet' }],
  [{ script: 'sub' }, { script: 'super' }],
  [{ indent: '-1' }, { indent: '+1' }],
  [{ direction: 'rtl' }],

  [{ size: ['small', false, 'large', 'huge'] }],
  [{ header: [1, 2, 3, 4, 5, 6, false] }],

  [{ color: [] }, { background: [] }],
  [{ font: [] }],
  [{ align: [] }],

  ['link'],

  ['clean']
]

const onTextChange = (e: EditorTextChangeEvent) => {
  emits('update:text', e.textValue)
}
</script>

<template>
  <div class="CreateFormContent profile-left-column-card">
    <h3 class="CreateFormContent__title">Контент</h3>
    <p-editor
      v-model="value_"
      class="CreateFormContent__editor"
      :modules="{ toolbar }"
      @text-change="onTextChange"
    />
  </div>
</template>

<style lang="scss">
.CreateFormContent {
  padding-top: 0;
  &__title {
    margin-bottom: step(3);
    @include textWithMobile(25px);
  }

  &__editor {
    .p-editor-toolbar {
      display: none;
    }
  }
}
</style>
