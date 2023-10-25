<template>
  <swiper
    :spaceBetween="30"
    :centeredSlides="true"
    :autoplay="{
      delay: 4000,
      disableOnInteraction: false,
    }"
    :pagination="{
      clickable: true,
    }"
    :navigation="true"
    :modules="modules"
    class="mySwiper"
  >
    <swiper-slide>
      <img src="../images/qna.png" alt="문의사항" />
      <div class="swiper_inner">
        문의 사항 <RouterLink to="/posts" class="btn">자세히 보기</RouterLink>
      </div>
    </swiper-slide>
    <swiper-slide>
      <img src="../images/telephone.png" alt="전화 상담" />
      <div class="swiper_inner">
        전화 상담
        <a href="javascript:void(0)" class="btn consult_btn">자세히 보기</a>
      </div>
    </swiper-slide>
    <swiper-slide>
      <img src="../images/faq.jpg" alt="기술 설명" />
      <div class="swiper_inner">
        기술 설명 <RouterLink to="/poster" class="btn">자세히 보기</RouterLink>
      </div>
    </swiper-slide>
  </swiper>
</template>
<script>
// Import Swiper Vue.js components
import { Swiper, SwiperSlide } from 'swiper/vue';

// Import Swiper styles
import 'swiper/css';

import 'swiper/css/pagination';
import 'swiper/css/navigation';

// import required modules
import { Autoplay, Pagination, Navigation } from 'swiper/modules';

export default {
  components: {
    Swiper,
    SwiperSlide,
  },
  setup() {
    return {
      modules: [Autoplay, Pagination, Navigation],
    };
  },
};
</script>

<style scoped>
@import '@/assets/swiper.css';
@import '@/assets/common.css';
</style>
