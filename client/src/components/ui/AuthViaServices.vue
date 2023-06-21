<script lang="ts" setup>
import axios from '@/utils/api/axios'

const test = import.meta.env.VITE_BASE_URL + '/login/github/?redirect_uri=http://localhost:3000/'

const continueWithGitHUb = async () => {
    const res = await axios.get(`${import.meta.env.VITE_BASE_URL}/djoser/o/github/?redirect_uri=http://localhost:3000/github`)
    window.location.replace(res.data.authorization_url)
}

</script>

<template>
  <div class="AuthViaServices">
    <div class="AuthViaServices__title">С помощью сервиса</div>
    <div class="AuthViaServices__services">
      <div @click="continueWithGitHUb" class="LoginCard__form-btn">
        <div class="AuthViaServices__services-item">
          <i class="pi pi-github" style="font-size: 20px; color: black;"></i>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.AuthViaServices {
  &__title {
    text-align: center;
    font-weight: 500;
    @include textWithMobile(18px);
  }

  &__services {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: step(-2);
    margin-top: step(3-2);

    &-item {
      margin: step(2);
      display: flex;
      cursor: pointer;
    }
  }
}
</style>
