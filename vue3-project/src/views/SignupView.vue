<template>
  <div>
    <div class="wrapper">
      <div class="title">
        <router-link to="/" class="logo">
          <img src="../images/hanbat_logo.png" alt="HANBAT" />
        </router-link>
        <h1 style="font-size: 21px">회원가입</h1>
      </div>
      <div class="email">
        <input
          v-model="email"
          type="text"
          placeholder="이메일을 입력해 주세요."
        />
        <div id="emailError" class="error"></div>
      </div>
      <div class="name">
        <input v-model="name" type="text" placeholder="이름을 입력해 주세요." />
        <div id="nameError" class="error"></div>
      </div>
      <div class="password">
        <input
          v-model="password"
          type="password"
          placeholder="비밀번호를 입력해 주세요."
        />
        <div id="passwordError" class="error"></div>
      </div>
      <div class="passwordCheck">
        <input
          v-model="passwordCheck"
          type="password"
          placeholder="비밀번호를 다시 입력해 주세요."
        />
        <div id="passwordCheckError" class="error"></div>
      </div>
      <div class="phone1">
        <input
          v-model="phone"
          type="text"
          size="2"
          maxlength="11"
          placeholder=" 전화번호를 입력해 주세요"
        />
      </div>
      <div class="line">
        <hr />
      </div>
      <div class="signUp">
        <button id="signUpButton" :disabled="!isValid" @click="signUp">
          가입하기
        </button>
      </div>
    </div>
    <div class="signup-success" v-if="showSignupSuccess">
      <div class="alert">
        회원가입이 완료되었습니다.
        <button @click="navigateToSignin">확인</button>
      </div>
    </div>
  </div>
  <TheFooter></TheFooter>
</template>

<script setup>
import { ref, computed } from 'vue';
import TheFooter from '@/layouts/TheFooter.vue';
import axios from '@/api/axioscall.js';
import router from '@/router';

const email = ref('');
const name = ref('');
const password = ref('');
const passwordCheck = ref('');
const phone = ref('');
const showSignupSuccess = ref(false);

const isValid = computed(() => {
  return (
    email.value !== '' &&
    name.value !== '' &&
    password.value !== '' &&
    password.value === passwordCheck.value &&
    phone.value !== ''
  );
});

const signUp = async () => {
  try {
    const response = await axios.post('/signup', {
      email: email.value,
      name: name.value,
      password: password.value,
      phone: phone.value,
    });
    if (response.status === 201) {
      // 회원가입 성공
      showSignupSuccess.value = true;
      const confirmed = confirm(
        '회원가입이 완료되었습니다. 로그인 페이지로 이동하시겠습니까?',
      );
      if (confirmed) {
        router.push('/login');
      }
    }
  } catch (error) {
    console.error(error); // 에러 처리
    if (error.response && error.response.status === 400) {
      const responseData = error.response.data; // 서버 응답 데이터
      if (responseData.message === '이미 가입된 회원입니다.') {
        alert(responseData.message); // 알림 표시
      } else {
        // 기타 실패 메시지 처리
        alert('회원가입 실패: ' + responseData.message);
      }
    } else {
      // 기타 오류 처리
      alert('서버 요청 중 오류가 발생했습니다.');
    }
  }
};
</script>

<style scoped>
@import '@/assets/signup.css';
@import '@/assets/common.css';
.signup-success {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}

.alert {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
  text-align: center;
}

.alert button {
  margin-top: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 8px 16px;
  cursor: pointer;
}
</style>
