<script setup lang="ts">
const props = defineProps({
  name: {
    type: String,
    required: true
  },
  avatar: {
    type: String,
    default: null
  }
})
</script>

<template>
  <div class="ProfileCard profile-left-column-card">
    <img class="ProfileCard__avatar" :src="props.avatar" />

    <div class="ProfileCard__info">
      <div class="ProfileCard__info-nick">@{{ props.name }}</div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.ProfileCard {
  display: flex;

  &__avatar {
    display: block;
    width: 130px;
    height: 130px;
    object-fit: contain;
    margin-right: step(5);
    border-radius: $radius-1;
  }

  &__info {
    &-nick {
      font-weight: bold;
      @include textWithMobile(25px);
    }

    &-text {
      margin-top: step(3);
      @include textWithMobile(20px);
    }
  }
}

@media screen and (max-width: 768px) {
  .ProfileCard {
    flex-direction: column;
    &__avatar {
      margin-right: 0;
      margin-bottom: step(3);
    }
  }
}
</style>
