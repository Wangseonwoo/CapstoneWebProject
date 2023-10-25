<template>
  <TheHeader></TheHeader>

  <!-- VISUAL -->
  <section class="visual">
    <div class="inner"></div>
  </section>

  <!-- NOTICE -->
  <section class="notice">
    <div class="notice-line">
      <div class="bg"></div>
      <div class="inner">
        <h2>고객 센터</h2>
      </div>
      <TheSwiper></TheSwiper>
    </div>
  </section>
  <TheGsap></TheGsap>

  <TheFooter></TheFooter>
</template>

<script setup>
import TheHeader from '@/layouts/TheHeader.vue';
import TheFooter from '@/layouts/TheFooter.vue';
import TheSwiper from '@/layouts/TheSwiper.vue';
import TheGsap from '@/layouts/TheGsap.vue';
</script>

<style scoped>
@import '@/assets/home.css';
@import '@/assets/common.css';
</style>
