<template>
  <router-link to="/" class="HeaderLogo">
    <span class="HeaderLogo__text"> Полихабр </span>
    <!-- <span class="HeaderLogo__inner"> КАК СТАТЬ АВТОРОМ </span> -->
  </router-link>
</template>

<style lang="scss" scoped>
.HeaderLogo {
  color: white;

  &__text {
    font-weight: bold;
    font-size: 31px;
    line-height: 45px;
  }

  &__inner {
    display: inline-flex;
    align-items: center;
    padding: 0px 16px;
    height: 39px;
    border-radius: 10px;
    border: 1px solid white;
    font-size: 20px;
    line-height: 29px;
    font-weight: medium;
    text-transform: uppercase;
  }
}

@media screen and (max-width: 768px) {
  .HeaderLogo {
    &__inner {
      display: none;
    }
  }
}
</style>
