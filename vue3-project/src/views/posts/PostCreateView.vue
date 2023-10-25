<template>
  <TheHeader></TheHeader>
  <div class="mb-3 to">
    <h2>게시글 등록</h2>
    <hr class="my-4" />
    <form @submit.prevent="save">
      <div class="mb-3">
        <label for="title" class="form-label"> 제목 </label>
        <input
          v-model="form.title"
          type="text"
          class="form-control"
          id="title"
        />
      </div>
      <div class="mb-3">
        <label for="content" class="form-label"> 내용 </label>
        <textarea
          v-model="form.content"
          class="form-control"
          id="content"
          rows="3"
        ></textarea>
      </div>
      <div class="pt-4">
        <button type="button" class="btn btn-outline-red" @click="goListPage">
          취소
        </button>
        <button class="btn btn-primary">저장</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import TheHeader from '@/layouts/TheHeader.vue';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from '@/api/axioscall.js';
import Cookies from 'js-cookie';

const router = useRouter();
const form = ref({
  title: null,
  content: null,
});

const goListPage = () => {
  router.push('/posts');
};

const save = async () => {
  try {
    const email = Cookies.get('user_email');
    const response = await axios.post('/posts', {
      title: form.value.title,
      content: form.value.content,
      email: email,
    });
    if (response.status === 201) {
      // 성공적으로 저장되었을 때 처리할 코드 추가
      // 예: 글 목록 페이지로 이동
      router.push({ name: 'PostList' });
    } else {
      // 저장 실패 시 처리할 코드 추가
      console.error('Failed to save the post.');
    }
  } catch (error) {
    console.error('Error saving the post:', error);
  }
};
</script>

<style scoped>
.to {
  width: 1100px;
  margin: 0 auto;
  margin-top: 150px;
}
.btn {
  float: right;
}
</style>
