<script setup lang="ts">
const props = defineProps({
  isLogin: Boolean
})
</script>

<template>
  <div class="AuthSwitch main-right-column-card">
    <div>
      <template v-if="props.isLogin">
        Еще нет аккаунта?
        <span class="AuthSwitch__action">
          <router-link to="/registration"> Зарегистрируйтесь </router-link>
        </span>
      </template>
      <template v-else>
        Уже зарегистрированы?
        <span class="AuthSwitch__action">
          <router-link to="/login"> Войдите </router-link>
        </span>
      </template>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.AuthSwitch {
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
  @include textWithMobile(18px);

  &__action {
    color: $purple-900;
  }
}

@media screen and (max-width: 768px) {
  .AuthSwitch {
    height: 60px;
  }
}
</style>
