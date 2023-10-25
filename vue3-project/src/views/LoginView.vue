<template>
  <TheHeader></TheHeader>
  <section class="signin">
    <h1>HBGATE 로그인</h1>
    <div class="signin__card">
      <form @submit.prevent="login">
        <input v-model="email" type="text" placeholder="이메일을 입력하세요." />
        <input
          v-model="password"
          type="password"
          placeholder="비밀번호를 입력하세요."
        />
        <input type="submit" value="로그인" />
      </form>
      <div class="actions">
        <RouterLink to="/signup">회원가입</RouterLink>
        <RouterLink to="/find">이메일 /비밀번호 찾기</RouterLink>
      </div>
    </div>
  </section>
  <TheFooter></TheFooter>
</template>

<script setup>
import TheFooter from '@/layouts/TheFooter.vue';
import TheHeader from '@/layouts/TheHeader.vue';
import { ref } from 'vue';
import { RouterLink } from 'vue-router';
import axios from '@/api/axioscall.js';
import router from '@/router';
import Cookies from 'js-cookie';

const email = ref('');
const password = ref('');

const login = async () => {
  try {
    const response = await axios.post('/login', {
      email: email.value, // .value를 추가해서 실제 값을 전달
      password: password.value, // .value를 추가해서 실제 값을 전달
    });

    if (response.status === 200) {
      alert('로그인 성공');
      Cookies.set('isLoggedIn', 'true', { expires: 7 });
      Cookies.set('user_email', email.value, { expires: 7 });
      router.push('/');
    } else {
      alert('로그인 실패: ' + response.data.error);
    }
  } catch (error) {
    console.error(error);
    alert('로그인 실패: ' + error.response.data.error);
  }
};
</script>

<style scoped>
@import '@/assets/login.css';
@import '@/assets/common.css';
</style>
