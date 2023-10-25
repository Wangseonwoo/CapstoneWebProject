import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import LoginView from '@/views/LoginView.vue';
import FindView from '@/views/FindView.vue';
import SignupView from '@/views/SignupView.vue';
import PosterView from '@/views/PosterView.vue';
import PostCreateView from '@/views/posts/PostCreateView.vue';
import PostDetailView from '@/views/posts/PostDetailView.vue';
import PostEditView from '@/views/posts/PostEditView.vue';
import PostListView from '@/views/posts/PostListView.vue';
import OtpView from '@/views/OtpView.vue';

const routes = [
  {
    path: '/',
    component: HomeView,
  },

  {
    path: '/login',
    name: 'Login',
    component: LoginView,
  },

  {
    path: '/find',
    name: 'Find',
    component: FindView,
  },

  {
    path: '/signup',
    component: SignupView,
  },

  {
    path: '/poster',
    component: PosterView,
  },

  {
    path: '/posts',
    name: 'PostList',
    component: PostListView,
  },
  {
    path: '/posts/create',
    name: 'PostCreate',
    component: PostCreateView,
  },

  {
    path: '/posts/:id',
    name: 'PostDetail',
    component: PostDetailView,
  },

  {
    path: '/posts/:id/edit',
    name: 'PostEdit',
    component: PostEditView,
  },

  {
    path: '/otp',
    name: 'Otp',
    component: OtpView,
  },
];

const router = createRouter({
  history: createWebHistory('/'),
  routes,
});

export default router;
