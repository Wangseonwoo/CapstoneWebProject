<template>
  <div>
    <TheHeader></TheHeader>
    <div class="section1">
      <div class="container">
        <div class="row full-height justify-content-center">
          <div class="col-12 text-center align-self-center py-5">
            <div class="section pb-5 pt-5 pt-sm-2 text-center">
              <h6 class="mb-0 pb-3">
                <span>이메일 찾기</span><span>비밀번호 찾기</span>
              </h6>
              <input
                class="checkbox"
                type="checkbox"
                id="reg-log"
                name="reg-log"
              />
              <label for="reg-log"></label>
              <div class="card-3d-wrap mx-auto">
                <div class="card-3d-wrapper">
                  <div class="card-front">
                    <div class="center-wrap">
                      <div class="section text-center">
                        <h4 class="mb-4 pb-3">이메일 찾기</h4>
                        <div class="form-group">
                          <input
                            v-model="name"
                            type="text"
                            name="logename"
                            class="form-style"
                            placeholder="이름을 입력하세요"
                            id="logname"
                            autocomplete="off"
                          />
                          <i class="input-icon uil uil-user"></i>
                        </div>
                        <div class="form-group mt-2">
                          <input
                            v-model="phone"
                            type="tel"
                            name="logphone"
                            class="form-style"
                            placeholder="전화번호를 입력하세요"
                            id="logphone"
                            autocomplete="off"
                          />
                          <i class="input-icon uil uil-phone"></i>
                        </div>
                        <a @click="findEmail" class="btn mt-4">이메일 찾기</a>
                      </div>
                    </div>
                  </div>
                  <div class="card-back">
                    <div class="center-wrap">
                      <div class="section text-center">
                        <h4 class="mb-4 pb-3">비밀번호 찾기</h4>
                        <div class="form-group">
                          <input
                            v-model="resetName"
                            type="text"
                            name="logename"
                            class="form-style"
                            placeholder="이름 입력하세요"
                            id="passlogname"
                            autocomplete="off"
                          />
                          <i class="input-icon uil uil-user"></i>
                        </div>
                        <div class="form-group mt-2">
                          <input
                            v-model="resetEmail"
                            type="email"
                            name="logmail"
                            class="form-style"
                            placeholder="이메일을 입력하세요"
                            id="logmail1"
                            autocomplete="off"
                          />
                          <i class="input-icon uil uil-at"></i>
                        </div>
                        <a @click="resetPassword" class="btn mt-4">제출</a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-if="showResetForm">
        <h4 class="mb-4 pb-3">비밀번호 재설정</h4>
        <div class="form-group">
          <input
            v-model="newPassword"
            type="password"
            name="newPassword"
            class="form-style"
            placeholder="새로운 비밀번호를 입력하세요"
            id="newPassword"
          />
          <i class="input-icon uil uil-lock-alt"></i>
        </div>
        <div class="form-group mt-2">
          <input
            v-model="confirmPassword"
            type="password"
            name="confirmPassword"
            class="form-style"
            placeholder="비밀번호 재입력"
            id="confirmPassword"
          />
          <i class="input-icon uil uil-lock-alt"></i>
        </div>
        <a @click="submitResetPassword" class="btn mt-4">비밀번호 재설정</a>
      </div>
    </div>
  </div>
</template>

<script setup>
import TheHeader from '@/layouts/TheHeader.vue';
import axios from '@/api/axioscall.js';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const name = ref('');
const phone = ref('');
const resetName = ref('');
const resetEmail = ref('');
const newPassword = ref('');
const confirmPassword = ref('');
const showResetForm = ref(false); // 초기에는 비밀번호 재설정 폼을 숨김

const findEmail = async () => {
  try {
    const response = await axios.post('/find/find-email', {
      name: name.value,
      phone: phone.value,
    });
    if (response.status === 200) {
      const { email } = response.data;
      if (email) {
        // 이메일 정보를 사용하여 팝업 창 또는 메시지를 표시
        alert(`고객님의 이메일은  ${email}  입니다`);
      } else {
        // 이메일을 찾을 수 없는 경우
        alert('이메일을 찾을 수 없습니다.');
      }
    }
  } catch (error) {
    console.error('이메일 찾기 중 오류 발생:', error);
    // 서버에서 오류 응답을 반환하는 경우 처리
    if (error.response && error.response.status === 404) {
      alert('회원 가입한 사용자의 이름 또는 전화번호가 틀립니다.');
    }
  }
};
const resetPassword = async () => {
  try {
    // 서버로 요청을 보내서 이름과 이메일이 DB와 일치하는지 확인하는 로직을 수행합니다.
    const response = await axios.post('/find/reset-password-check', {
      name: resetName.value,
      email: resetEmail.value,
    });

    if (response.status === 200 && response.data.matched) {
      // 이름과 이메일이 DB와 일치하는 경우, 비밀번호 재설정 폼을 표시합니다.
      showResetForm.value = true;
    } else {
      // 이름과 이메일이 DB와 일치하지 않는 경우 에러 메시지를 표시합니다.
      alert('이름 또는 이메일이 일치하지 않습니다.');
    }
  } catch (error) {
    console.error('비밀번호 재설정 중 오류 발생:', error);
    // 서버에서 오류 응답을 반환하는 경우 처리
    if (error.response && error.response.status === 404) {
      alert('이름 또는 이메일이 일치하지 않습니다.');
    }
  }
};

const submitResetPassword = async () => {
  try {
    // 서버로 요청을 보내서 새로운 비밀번호로 업데이트하는 로직을 수행합니다.
    const response = await axios.post('/find/submit-reset-password', {
      name: resetName.value,
      email: resetEmail.value,
      new_password: newPassword.value,
    });

    if (response.status === 200) {
      alert('비밀번호가 성공적으로 재설정되었습니다.');
      router.push({ name: 'Login' });
      // 비밀번호 재설정 성공 후 어떤 작업을 수행할 수 있습니다.
    } else {
      alert('비밀번호 재설정에 실패했습니다.');
    }
  } catch (error) {
    console.error('비밀번호 재설정 중 오류 발생:', error);
    // 서버에서 오류 응답을 반환하는 경우 처리
    if (error.response && error.response.status === 404) {
      alert(
        '비밀번호 재설정에 실패했습니다. 이름 또는 이메일이 일치하지 않습니다.',
      );
    }
  }
};
</script>

<style scoped>
@import '@/assets/find.css';
@import '@/assets/common.css';
</style>
