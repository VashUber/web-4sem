<script setup lang="ts">
import CustomInput from '@/components/ui/CustomInput.vue'
import CustomInputFile from '@/components/ui/CustomInputFile.vue'
import { PButton } from '@/uiComponents'
import { registration } from '@/utils/api/Auth'
import { computed, ref } from 'vue'
import type { IFormRegistration } from '@/utils/api/Auth'

export interface IRows {
  label: string,
  component: object,
  props?: object,
  value: string,
  slot?: string,
  memo?: unknown[],
  class?: string,
}

const form = ref({
  email: '',
  name: '',
  password: '',
  password_confirm: '',
  avatar: undefined,
  username: '',
  surname: '',
  patronymic: '',
} as IFormRegistration)

const currentStep = ref(0)
const isError = ref(false)
const errors = ref({} as Record<string, string[]>)

const allFormData = [
  [
    {
      component: CustomInput,
      label: 'Имя',
      value: 'username',
    },
    {
      component: CustomInput,
      label: 'Фамилия',
      value: 'surname',
    },
    {
      component: CustomInput,
      label: 'Отчество',
      value: 'patronymic',
    },
  ],
  [
    {
      component: CustomInput,
      label: 'Никнейм',
      value: 'name',
    },{
      component: CustomInput,
      label: 'E-mail',
      value: 'email',
    },
    {
      component: CustomInputFile,
      label: 'Аватар',
      value: 'avatar',
    },
  ],
  [
    {
      component: CustomInput,
      label: 'Пароль',
      value: 'password'
    },
    {
      component: CustomInput,
      label: 'Пароль ещё раз',
      value: 'password_confirm'
    },
  ]
] as IRows[][]

const currentFormRow = computed(() => {
  return allFormData[currentStep.value]
})

const onSubmit = async () => {
  await registration(form.value)
    .catch((error) => {
      isError.value = true
      errors.value = error.response.data

      const errorStep = allFormData.reduce((minIndex, item, index) => {
        if (minIndex > index && !!item.find(el => errors.value[el.value])) {
          return index
        }

        return minIndex
      }, allFormData.length)

      currentStep.value = errorStep
    })
}
</script>

<template>
  <div class="RegistrationCard main-right-column-card">
    <h1 class="RegistrationCard__title">Регистрация</h1>
    <div class="RegistrationCard__error-wrap">
      <div v-for="(error, key) of errors" :key="key" class="RegistrationCard__error">
        <b>{{ key }}</b>: {{ error[0] }}
      </div>
    </div>
    <form class="RegistrationCard__form" @submit.prevent="onSubmit">
      <template v-for="(field, index) in currentFormRow" :key="index">
        <component :is="field.component" :id="field.value" v-model="form[field.value as keyof typeof form]"
          v-bind="field.props"> {{ field.label }}</component>
      </template>
      <div class="RegistrationCard__form-btn--wrap">
        <p-button v-show="currentStep > 0" class="RegistrationCard__form-btn" @click="currentStep = Math.max(0, --currentStep)">
          Назад
        </p-button>
        <p-button v-show="currentStep < allFormData.length - 1" class="RegistrationCard__form-btn" @click="currentStep = Math.min(allFormData.length - 1, ++currentStep)">
          Дальше
        </p-button>
        <p-button v-show="currentStep === allFormData.length - 1" type="submit" class="RegistrationCard__form-btn">
          Зарегистрироваться
        </p-button>
      </div>
    </form>
  </div>
</template>

<style lang="scss" scoped>
.RegistrationCard {
  width: 100%;
  background: white;
  padding-top: step(6);
  padding-bottom: step(6);

  &__title {
    text-align: center;
    font-weight: bold;
    @include textWithMobile(24px);
  }

  &__error {
    color: red;
  }

  &__form {
    margin-top: step(3);
    display: flex;
    flex-direction: column;

    >*:not(:first-child) {
      margin-top: step(3);
    }

    &-btn {
      width: 200px;
      margin-top: step(5) !important;
      align-self: center;

      &:not(:first-child) {
        margin-left: auto;
      }

      &--wrap {
        display: flex;
        justify-content: space-between;
      }
    }
  }

  &__services {
    margin-top: step(3);
  }
}
</style>
