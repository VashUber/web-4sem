<script setup lang="ts">
import LoginCard from '@/components/parts/login/LoginCard.vue'
import AuthSwitch from '@/components/ui/AuthSwitch.vue'
import { user } from '@/composable/fetchUser'
</script>

<template>
  <div class="LoginView">
    <div class="LoginView__wrap">
      <login-card />
      <auth-switch is-login />
    </div>
  </div>
</template>

<style lang="scss" scoped>
.LoginView {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: calc(100vh - 108px);

  &__wrap {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    max-width: 534px;
    justify-content: center;
    margin-top: calc(-60px - 24px);

    > *:not(:first-child) {
      margin-top: step(6);
    }
  }
}

@media screen and (max-width: 768px) {
  .LoginView {
    &__wrap {
      > *:not(:first-child) {
        margin-top: step(3);
      }
    }
  }
}
</style>
