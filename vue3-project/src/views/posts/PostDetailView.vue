<template>
  <TheHeader></TheHeader>
  <div class="to">
    <h2>{{ post.title }}</h2>
    <p>{{ post.content }}</p>
    <p class="text-muted">{{ post.createdAt }}</p>
    <hr class="my-4" />
    <div class="row">
      <div class="col-auto">
        <button class="btn btn-outline-dark" @click="goPrevPost">이전글</button>
      </div>
      <div class="col-auto">
        <button class="btn btn-outline-dark" @click="goNextPost">다음글</button>
      </div>

      <div class="col-auto me-auto"></div>

      <div class="col-auto">
        <router-link :to="{ name: 'PostList' }" class="btn btn-outline-dark">
          목록
        </router-link>
      </div>
      <div class="col-auto">
        <button @click="checkEmail" class="btn btn-outline-primary">
          수정
        </button>
      </div>
      <div class="col-auto">
        <button class="btn btn-outline-danger" @click="deletePost">삭제</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import TheHeader from '@/layouts/TheHeader.vue';
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from '@/api/axioscall.js';
import Cookies from 'js-cookie';

const route = useRoute();
const router = useRouter();
const post = ref({});
const allPosts = ref([]);

const fetchAllPosts = async () => {
  try {
    const response = await axios.get('/posts', { withCredentials: true });
    allPosts.value = response.data;
  } catch (error) {
    console.error('Error fetching all posts:', error);
  }
};

onMounted(async () => {
  const postId = Number(route.params.id);
  await fetchAllPosts(); // 모든 게시글 가져오기
  try {
    const response = await axios.get(`/posts/${postId}`, {
      withCredentials: true,
    });
    post.value = response.data;
  } catch (error) {
    console.error('Error fetching post:', error);
  }
});

const goPrevPost = async () => {
  const currentIndex = allPosts.value.findIndex(p => p.id === post.value.id);
  if (currentIndex > 0) {
    const prevPost = allPosts.value[currentIndex - 1];
    await fetchPostData(prevPost.id); // 이전 글의 ID를 인자로 전달하여 데이터 불러오기
    router.push({ name: 'PostDetail', params: { id: prevPost.id } });
  }
};

const goNextPost = async () => {
  const currentIndex = allPosts.value.findIndex(p => p.id === post.value.id);
  if (currentIndex < allPosts.value.length - 1) {
    const nextPost = allPosts.value[currentIndex + 1];
    await fetchPostData(nextPost.id); // 다음 글의 ID를 인자로 전달하여 데이터 불러오기
    router.push({ name: 'PostDetail', params: { id: nextPost.id } });
  }
};

const fetchPostData = async postId => {
  try {
    const response = await axios.get(`/posts/${postId}`, {
      withCredentials: true,
    });
    post.value = response.data;
  } catch (error) {
    console.error('Error fetching post:', error);
  }
};

const checkEmail = async () => {
  try {
    const postId = post.value.id;
    const currentUserEmail = Cookies.get('user_email'); // 쿠키에서 현재 사용자의 이메일을 가져옵니다.
    console.log(currentUserEmail);
    // 서버로 현재 사용자의 이메일을 보내서 확인
    const response = await axios.post(
      '/checkUserEmail',
      { email: currentUserEmail },
      { withCredentials: true },
    );

    if (response.status === 200) {
      router.push({ name: 'PostEdit', params: { id: postId } });
    } else {
      alert('권한이 없습니다.');
    }
  } catch (error) {
    console.error('Error deleting post:', error);
    alert('권한이 없습니다.');
  }
};

const deletePost = async () => {
  try {
    if (confirm('정말로 삭제하시겠습니까?')) {
      const postId = post.value.id;
      const currentUserEmail = Cookies.get('user_email'); // 쿠키에서 현재 사용자의 이메일을 가져옵니다.
      console.log(currentUserEmail);
      // 서버로 현재 사용자의 이메일을 보내서 확인
      const response = await axios.post(
        '/checkUserEmail',
        { email: currentUserEmail },
        { withCredentials: true },
      );

      if (response.status === 200) {
        // 사용자 이메일이 일치하면 삭제
        await axios.delete(`/posts/${postId}`, { withCredentials: true });
        router.push({ name: 'PostList' });
      } else {
        alert('권한이 없습니다.');
      }
    }
  } catch (error) {
    console.error('Error deleting post:', error);
    alert('권한이 없습니다.');
  }
};
</script>

<style scoped>
.to {
  width: 1100px;
  margin: 0 auto;
  margin-top: 150px;
}
</style>
