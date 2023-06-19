<script setup lang="ts">
import { PButton } from '@/uiComponents'
import CustomInput from '@/components/ui/CustomInput.vue'
import { ref } from 'vue'
import { login } from '@/utils/api/Auth'
import AuthViaServices from '@/components/ui/AuthViaServices.vue'
const form = ref({
  email: '',
  password: ''
})

const onLogin = async () => {
  login(form.value.email, form.value.password)
}
</script>

<template>
  <div class="LoginCard main-right-column-card">
    <h1 class="LoginCard__title">Вход</h1>
    <form class="LoginCard__form" @submit.prevent>
      <custom-input id="email" v-model="form.email"> E-mail </custom-input>
      <custom-input id="password" v-model="form.password" type="password"> Пароль </custom-input>
      <p-button class="LoginCard__form-btn" type="submit" @click="onLogin"> Войти </p-button>
      <a href="#" class="LoginCard__form-btn">
        <p-button>
          Войти через
          <i class="pi pi-github" style="font-size: 20px"></i>
        </p-button>
      </a>
    </form>
    <auth-via-services class="LoginCard__services" />
  </div>
</template>

<style lang="scss" scoped>
.LoginCard {
  width: 100%;
  background: white;
  padding-top: step(6);
  padding-bottom: step(6);

  &__title {
    text-align: center;
    font-weight: bold;
    @include textWithMobile(24px);
  }

  &__form {
    margin-top: step(3);
    display: flex;
    flex-direction: column;

    > *:not(:first-child) {
      margin-top: step(3);
    }

    &-btn {
      width: 180px;
      margin-top: step(5) !important;
      align-self: center;
    }

    a > * {
      display: flex;
      align-items: center;
      gap: 10px;
      width: 100%;
    }
  }

  &__services {
    margin-top: step(3);
  }
}
</style>
