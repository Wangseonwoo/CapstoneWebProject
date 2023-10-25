<template>
  <TheHeader></TheHeader>
  <div class="to">
    <h2>게시글 수정</h2>
    <hr class="my-4" />
    <form @submit.prevent="edit">
      <div class="mb-3">
        <label for="title" class="form-label">제목</label>
        <input
          v-model="form.title"
          type="text"
          class="form-control"
          id="title"
        />
      </div>
      <div class="mb-3">
        <label for="content" class="form-label">내용</label>
        <textarea
          v-model="form.content"
          class="form-control"
          id="content"
          rows="3"
        ></textarea>
      </div>
      <div class="pt-4">
        <button
          type="button"
          class="btn btn-outline-danger"
          @click="goDetailPage"
        >
          취소
        </button>
        <button class="btn btn-primary">수정</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import TheHeader from '@/layouts/TheHeader.vue';
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from '@/api/axioscall.js';

const route = useRoute();
const router = useRouter();
const form = ref({
  title: '',
  content: '',
});

// 게시물 데이터 가져오기
const fetchPostData = async () => {
  const postId = Number(route.params.id);
  try {
    const response = await axios.get(`/posts/${postId}`, {
      withCredentials: true,
    });
    form.value.title = response.data.title; // title 값을 form 객체에 할당
    form.value.content = response.data.content; // content 값을 form 객체에 할당
  } catch (error) {
    console.error('Error fetching post:', error);
  }
};

// 컴포넌트가 마운트될 때 게시물 데이터 가져오기
onMounted(fetchPostData);

// 취소 버튼 클릭 시 게시물 상세 페이지로 이동
const goDetailPage = () => {
  const postId = Number(route.params.id);
  router.push({ name: 'PostDetail', params: { id: postId } });
};

// 수정 버튼 클릭 시 게시물 수정 요청 보내기
const edit = async () => {
  const postId = Number(route.params.id);
  try {
    await axios.put(`/posts/${postId}`, form.value, { withCredentials: true });
    router.push({ name: 'PostDetail', params: { id: postId } });
  } catch (error) {
    console.error('Error updating post:', error);
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
