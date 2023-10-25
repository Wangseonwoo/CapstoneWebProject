<template>
  <div>
    <TheHeader></TheHeader>
    <div class="container">
      <h1><strong>OTP 발급 받기</strong></h1>
      <button class="btn otp-btn" @click="issueOTP">OTP 발급 받기</button>
      <div class="otp-number" v-if="otp">{{ otp }}</div>
    </div>
  </div>
</template>

<script setup>
import TheHeader from '@/layouts/TheHeader.vue';
import { ref } from 'vue';
import axios from '@/api/axioscall.js';

const otp = ref(''); // 발급된 OTP를 저장할 변수

const issueOTP = async () => {
  try {
    const response = await axios.post('/generate-otp');
    if (response.status === 200) {
      // 서버에서 OTP 발급이 성공하면 otp 변수에 저장
      otp.value = response.data.otp;
    }
  } catch (error) {
    console.error('OTP 발급 중 오류 발생:', error);
  }
};
</script>

<style scoped>
.container {
  text-align: center;
  margin-top: 150px;
}
.otp-btn {
  margin: 0 auto;
  margin-top: 50px;
  width: 140px;
}

.otp-number {
  font-size: 50px;
  margin-top: 30px;
}
</style>
