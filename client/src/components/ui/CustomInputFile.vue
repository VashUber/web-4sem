<script setup lang="ts">
import { computed, defineProps, defineEmits, ref } from 'vue'
import { PButton } from '@/uiComponents'
import FormFieldWrap from './FormFieldWrap.vue'
import type { PropType } from 'vue'

export interface IValue {
  name: string
  url: string
  [s: string]: any
}

const props = defineProps({
  modelValue: {
    type: [File, Object] as PropType<File | IValue>,
    default: undefined
  },
  errorMessage: {
    type: String,
    default: undefined
  },
  placeholder: {
    type: String,
    default: 'Загрузите файл'
  },
  id: {
    type: String,
    default: ''
  },
  visibleItem: {
    type: Boolean,
    default: true
  },
  canUpload: {
    type: Boolean,
    default: true
  },
  hiddenClear: Boolean,
  isReadonly: Boolean,
  error: Boolean
})

const emits = defineEmits(['update:modelValue'])

const file = ref<HTMLInputElement>()
const selectedFile = computed(() => !!props.modelValue)
const isError = computed(() => !!props.errorMessage || props.error)

const filesURL = computed(() => {
  if (!props.modelValue) {
    return
  }

  if (props.modelValue instanceof File) {
    return URL.createObjectURL(props.modelValue as File)
  }

  return (props.modelValue as IValue).url
})

const placeholderInputText = computed(() => {
  if (props.modelValue) {
    return props.modelValue.name
  }

  return props.placeholder
})

const previewFile = (event: Event) => {
  const files = (event.target as HTMLInputElement).files

  if (files?.length) {
    emits('update:modelValue', files[0])
  }

  if (file.value) {
    file.value.value = ''
  }
}

const removeFile = () => {
  if (file.value) {
    file.value.files = null
    emits('update:modelValue', undefined)
  }
}
</script>

<template>
  <form-field-wrap>
    <slot />
    <template #content>
      <div v-if="filesURL && visibleItem" class="CustomInputFile__img-wrap">
        <img
          class="CustomInputFile__img"
          :class="{
            'CustomInputFile__img-error': isError
          }"
          :src="filesURL"
        />
      </div>
      <div
        v-bind="$attrs"
        class="CustomInputFile__input"
        :class="{
          'CustomInputFile__input-error': isError
        }"
        @click="!props.isReadonly && canUpload && file?.click()"
      >
        <div class="CustomInputFile__input__text">
          {{ placeholderInputText }}
        </div>
        <div
          v-if="!props.isReadonly"
          class="CustomInputFile__input__button-wrap"
          :class="{
            'CustomInputFile__input-error': isError
          }"
        >
          <div
            v-if="selectedFile && !props.hiddenClear"
            class="CustomInputFile__input-clear"
            @click.prevent.stop="removeFile"
          >
            <i
              class="pi pi-times-circle"
              style="color: black; margin-right: 4px; font-size: 20px"
            ></i>
          </div>
          <PButton
            v-if="props.canUpload"
            class="CustomInputFile__input__button dowload ui-cursor-pointer ui-select-none ui-flex ui-ml-[10px] ui-items-center ui-rounded-base ui-bg-white-900 ui-py-[8px] ui-px-[10px] ui-border-black-50 ui-border-2 ui-text-black-900 ui-text-p14-semibold ui-whitespace-nowrap"
          >
            Выберите файл
          </PButton>
        </div>
      </div>
      <input
        :id="id"
        ref="file"
        class="CustomInputFile__input__field ui-absolute ui-pointer-events-none ui-opacity-0"
        type="file"
        name="photo"
        accept="image/jpeg,image/png,image/jpg"
        @change="previewFile"
      />
    </template>
  </form-field-wrap>
</template>

<style lang="scss">
.CustomInputFile {
  &__img {
    border-radius: 0px;
    max-height: 150px;
    border-width: 2px;

    &-error {
      border-color: red;
    }

    &-wrap {
      margin-bottom: step(3);
    }
  }

  &__input {
    font-weight: 600;
    padding-left: 10px;
    padding-right: 2px;
    background: white;
    border: 1px solid black;
    justify-content: space-between;
    align-items: center;
    display: flex;
    cursor: pointer;
    min-height: 48px;
    transition: all 300ms ease;

    &:hover {
      border-color: #6366f1;

      .CustomInputFile__input__button-wrap::after {
        background: #6366f1;
      }
    }

    &-error {
      border-color: #ff6a55 !important;

      .CustomInputFile__input__button-wrap::after {
        background: #ff6a55;
      }
    }

    &__text {
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      padding-top: step(0.5);
      padding-bottom: step(0.5);
    }

    &__button {
      cursor: pointer;
      user-select: none;
      margin-left: 10px;
      display: flex;
      align-items: center;
      background: $purple-900;
      padding: step(2) step(2.5);
      color: white;
      width: 158px;

      &-wrap {
        align-self: stretch;
        align-items: center;
        display: flex;
        position: relative;

        &::after {
          position: absolute;
          content: '';
          transition: all 300ms ease;
          background: black;
          height: 100%;
          width: 0.5px;
          right: 168px;
          top: 0;
        }
      }
    }

    &-clear {
      cursor: pointer;
      display: flex;
      justify-content: center;
      align-items: center;
      margin-right: 4px;
    }

    &__field {
      position: absolute;
      width: 0px;
      opacity: 0;
    }
  }
}
</style>
