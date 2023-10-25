<template>
  <TheHeader></TheHeader>
  <div class="poster">
    <img src="../images/poster.jpg" alt="" />
  </div>
  <TheFooter></TheFooter>
</template>

<script>
import TheHeader from '@/layouts/TheHeader.vue';
import TheFooter from '@/layouts/TheFooter.vue';
export default {
  components: { TheHeader, TheFooter },
  setup() {
    return {};
  },
};
</script>

<style scoped>
@import '@/assets/poster.css';
@import '@/assets/common.css';
</style>
