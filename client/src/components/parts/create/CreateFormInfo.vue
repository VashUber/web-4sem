<script setup lang="ts">
import CustomInput from '@/components/ui/CustomInput.vue'
import CustomInputChips from '@/components/ui/CustomInputChips.vue'
import CustomInputFile from '@/components/ui/CustomInputFile.vue'
import FormFieldWrap from '@/components/ui/FormFieldWrap.vue'
import { PTextarea } from '@/uiComponents'
import { computed } from 'vue'

const props = defineProps({
  title: {
    type: String,
    required: true
  },
  tags: {
    type: Array,
    required: true
  },
  contentText: {
    type: String,
    default: null
  },
  file: {
    type: File,
    default: null,
  }
})

const emits = defineEmits(['update:title', 'update:tags', 'update:contentText', 'update:file'])

const title_ = computed({
  get() {
    return props.title
  },
  set(v) {
    emits('update:title', v)
  }
})

const tags_ = computed({
  get() {
    return props.tags
  },
  set(v) {
    emits('update:tags', v)
  }
})
const contentText_ = computed({
  get() {
    return props.contentText
  },
  set(v) {
    emits('update:contentText', v)
  }
})

const file_ = computed({
  get() {
    return props.file
  },
  set(v) {
    emits('update:file', v)
  }
})
</script>

<template>
  <div class="CreateFormInfo profile-left-column-card">
    <h3 class="CreateFormInfo__title">Основная информация</h3>
    <custom-input id="title" v-model="title_" class="CreateFormInfo__field">
      Заголовок
    </custom-input>
    <custom-input-chips id="tags" v-model="tags_" class="CreateFormInfo__field">
      Теги
    </custom-input-chips>
    <FormFieldWrap id="desc">
      Описание
      <template #content="{ id }">
        <PTextarea
          :id="id"
          v-model="contentText_"
          style="resize: none;"
          rows="5"
        />
      </template>
    </FormFieldWrap>

    <CustomInputFile v-model="file_" class="CreateFormInfo__field"> Обложка </CustomInputFile>
    
  </div>
</template>

<style lang="scss">
.CreateFormInfo {
  &__title {
    margin-bottom: step(5);
    @include textWithMobile(25px);
  }

  &__field {
    &:not(:last-child) {
      margin-bottom: step(3);
    }
  }
}
</style>
