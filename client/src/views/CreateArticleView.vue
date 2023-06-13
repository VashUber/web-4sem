<script setup lang="ts">
import CreateFormContent from '@/components/parts/create/CreateFormContent.vue'
import CreateFormInfo from '@/components/parts/create/CreateFormInfo.vue'
import { user } from '@/composable/fetchUser'
import { PButton } from '@/uiComponents'
import Api from '@/utils/api/Api'
import { useToast } from 'primevue/usetoast'
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
const toast = useToast()

const $route = useRoute()
const $router = useRouter()
const isCreated = $route.meta.create

const form = ref({
  title: '',
  tags: [],
  content: '',
  content_text: '',
  img: undefined,
  author: String(user.value?.id)
})

const onClick = async () => {
  if (isCreated) {
    await onSave()
  }
  else {
    await onEdit()
  }
}

const onSave = async () => {
  const formData = new FormData()

  formData.append('title', form.value.title)
  formData.append('content', form.value.content)
  formData.append('content_text', form.value.content_text)
  formData.append('author', String(user.value!.id))

  if (form.value.img) {
    formData.append('img', form.value.img)
  }

  await Api.createArticle(formData)
    .then((res) => {
      $router.push(`/edit/${res.id}`)
    })
}

const onEdit = async () => {
  const formData = new FormData()
  formData.append('title', form.value.title)
  formData.append('content', form.value.content)
  formData.append('content_text', form.value.content_text)
  formData.append('author', String(user.value!.id))

  if (form.value.img) {
    formData.append('img', form.value.img)
  }

  await Api.editArticle(+$route.params.id, formData)
    .then((res) => {
      form.value = {
        author: String(user.value?.id),
        content: res.content,
        content_text: res.content_text,
        img: undefined,
        tags: [],
        title: res.title,
      }

      toast.add({ severity: 'success', summary: 'Успешно', detail: 'Запись изменена', group: 'br', life: 3000 })
    })
}

onMounted(async () => {
  if (!isCreated) {
    await Api.fetchCurrentArticle(+$route.params.id)
      .then((res) => {
        form.value = {
          author: String(user.value?.id),
          title: res.title,
          tags: [],
          content: res.content,
          content_text: res.content_text,
          img: undefined,
        }
      })
  }
})
</script>

<template>
  <div>
    <create-form-info v-model:title="form.title" v-model:tags="form.tags" v-model:content-text="form.content_text" v-model:file="form.img"/>
    <create-form-content v-model="form.content" />
    <div class="CreateArticleView__save profile-left-column-card">
      <p-button @click="onClick"> Сохранить </p-button>
    </div>
  </div>
</template>

<style lang="scss">
.CreateArticleView {
  &__save {
    padding-top: 0;
  }
}
</style>
