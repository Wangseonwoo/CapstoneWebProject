<template>
  <header>
    <div class="inner">
      <RouterLink class="logo" to="/">
        <img src="../images/hanbat_logo.png" alt="HANBAT" />
      </RouterLink>
      <div class="sub-menu">
        <ul class="menu">
          <li v-if="!isLoggedIn">
            <RouterLink to="/login">LogIn</RouterLink>
          </li>
          <li v-if="isLoggedIn">
            <RouterLink class="btn" to="/otp">OTP</RouterLink>
            <button class="btn" @click="logout">LogOut</button>
          </li>
        </ul>
      </div>
    </div>
  </header>
</template>

<script setup>
import { computed } from 'vue';
import { RouterLink } from 'vue-router';
import Cookies from 'js-cookie';

// 로그인 상태를 쿠키에서 읽어오도록 수정
const isLoggedIn = computed(() => Cookies.get('isLoggedIn') === 'true');

const logout = () => {
  if (confirm('로그아웃 하시겠습니까?')) {
    // 로그아웃 시 쿠키를 삭제
    Cookies.remove('isLoggedIn');
    // 추가적으로 로그아웃 시 필요한 처리를 수행
    location.href = '/';
  }
};
</script>
