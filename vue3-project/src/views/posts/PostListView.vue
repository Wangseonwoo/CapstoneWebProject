<template>
  <TheHeader></TheHeader>
  <div class="to">
    <h2>게시글 목록</h2>
    <hr class="my-4" />

    <!-- 검색 기능을 위한 입력 필드 -->
    <div class="row g-3">
      <div class="col-3">
        <input
          v-model="searchQuery"
          type="text"
          class="form-control"
          placeholder="게시글 검색"
        />
      </div>
    </div>

    <!-- 게시글 목록 -->
    <div class="row g-3">
      <div v-for="post in filteredPosts" :key="post.id" class="col-12">
        <router-link :to="{ name: 'PostDetail', params: { id: post.id } }">
          <PostItem
            :title="post.title"
            :content="post.content"
            :created-at="post.createdAt"
          ></PostItem>
        </router-link>
      </div>
    </div>
    <div class="pagination">
      <button
        @click="changePage(currentPage - 1)"
        :disabled="currentPage === 1"
      >
        &lt;&lt;
      </button>
      <button
        @click="changePage(page)"
        v-for="page in totalPages"
        :key="page"
        :class="{ active: page === currentPage }"
      >
        {{ page }}
      </button>
      <button
        @click="changePage(currentPage + 1)"
        :disabled="currentPage === totalPages"
      >
        &gt; &gt;
      </button>
    </div>
    <div class="ml-auto">
      <div class="col-3">
        <select v-model="postsPerPage" class="form-select">
          <option value="3">3개씩 보기</option>
          <option value="6">6개씩 보기</option>
          <option value="9">9개씩 보기</option>
        </select>
      </div>
      <button @click="ButtonClick" class="btn ml-auto">게시글 작성</button>
    </div>
  </div>
</template>

<script setup>
import PostItem from '@/components/posts/PostItem.vue';
import TheHeader from '@/layouts/TheHeader.vue';
import { ref, onMounted, computed, watch } from 'vue';
import axios from '@/api/axioscall.js';
import Cookies from 'js-cookie';
import { useRouter } from 'vue-router';

const posts = ref([]);
const postsPerPage = ref(3); // 한 페이지에 보여줄 게시글 수
const currentPage = ref(1);
const searchQuery = ref(''); // 검색어 입력값
const router = useRouter();

const isLoggedIn = computed(() => Cookies.get('isLoggedIn') === 'true');
const ButtonClick = () => {
  if (isLoggedIn.value) {
    router.push('/posts/create');
  } else {
    alert('로그인이 필요합니디. ');
  }
};

const fetchPosts = async () => {
  try {
    const response = await axios.get('/posts', { withCredentials: true });
    posts.value = response.data;
  } catch (error) {
    console.error('Error fetching posts:', error);
  }
};

onMounted(fetchPosts);

const totalPages = computed(() =>
  Math.ceil(posts.value.length / postsPerPage.value),
);

const filteredPosts = computed(() => {
  const startIndex = (currentPage.value - 1) * postsPerPage.value;
  const endIndex = startIndex + postsPerPage.value;

  return posts.value
    .filter(post => post.title.includes(searchQuery.value)) // 검색어로 필터링
    .slice(startIndex, endIndex);
});

const changePage = page => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
  }
};

// 검색어가 변경될 때마다 게시글을 다시 필터링
watch(searchQuery, () => {
  currentPage.value = 1; // 검색어 변경 시 페이지 초기화
});
</script>

<style scoped>
.to {
  width: 1100px;
  margin: 0 auto;
  margin-top: 150px;
}
.pagination {
  margin-top: 20px;
  display: flex;
  justify-content: center;
}
.pagination button {
  margin: 0 5px;
  border: none;
  background-color: transparent;
  cursor: pointer;
  padding: 5px 10px;
}
.pagination button.active {
  background-color: #007bff;
  color: white;
}

.form-control {
  margin-bottom: 30px;
}
</style>
