<script>
import { onMounted, onUnmounted, ref } from 'vue';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

export default {
  emits: ['scrollTo'],
  setup(props, { emit }) {
    const main = ref();
    let smoother;
    let ctx;
    let stx;
    const scrollTo = () => {
      smoother.scrollTo('.visual', true, 'center center');
      emit('scrollTo');
    };

    onMounted(() => {
      ctx = gsap.context(self => {
        const boxes = self.selector('.box');
        boxes.forEach(box => {
          gsap.to(box, {
            x: 700,
            opacity: 1,
            scrollTrigger: {
              trigger: box,
              start: 'bottom bottom',
              end: 'top 20%',
              delay: 3,
              scrub: true,
            },
          });
        });
      }, main.value);

      stx = gsap.context(self => {
        const boxes = self.selector('.box1');
        boxes.forEach(box1 => {
          gsap.to(box1, {
            x: -1350,
            opacity: 1,
            scrollTrigger: {
              trigger: box1,
              start: 'bottom bottom',
              end: 'top 20%',
              scrub: true,
            },
          });
        });
      }, main.value); // <- Scope!
    });
    onUnmounted(() => {
      ctx.revert();
      stx.revert(); // <- Easy Cleanup!
    });
    return { main, scrollTo };
  },
};
</script>

<template>
  <main>
    <!-- TOUCH -->
    <div class="section flex-center column" ref="main">
      <section class="touch-product scroll-spy">
        <div class="inner">
          <img src="../images/toch.jpg" alt="" class="box" />

          <div class="text-gruop">
            <img src="../images/touch_text1.png" alt="" class="box1" />
            <img src="../images/touch_text2.png" alt="" class="box1" />
          </div>
        </div>
      </section>

      <!-- OTP -->
      <section class="otp-product scroll-spy">
        <div class="inner">
          <div class="text-gruop">
            <img src="../images/otp_text.png" alt="" class="box" />
            <img src="../images/otp_text2.png" alt="" class="box" />
          </div>

          <img
            src="../images/otp.jpg"
            width="500px"
            height="400px"
            alt=""
            class="inner1 box1"
          />
        </div>
      </section>

      <!-- SIGIN -->
      <section class="sigin-product scroll-spy">
        <div class="inner">
          <img src="../images/sigin.jpg" alt="" class="box" />

          <div class="text-gruop">
            <img src="../images/sigin_text.png" alt="" class="box1" />
            <img src="../images/sigin_text2.png" alt="" class="box1" />
          </div>
        </div>
      </section>
    </div>
  </main>
</template>

<style scoped>
@import '@/assets/gsap.css';
@import '@/assets/common.css';
</style>
