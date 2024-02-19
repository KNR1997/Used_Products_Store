<script setup>
import { NCarousel} from "naive-ui";

</script>

<template>
  <n-carousel autoplay>
    <img
      class="carousel-img"
      src="../assets/carousel-1.png"
    />
    <img
      class="carousel-img"
      src="../assets/carousel-2.png"
    />
    <img
      class="carousel-img"
      src="../assets/carousel-2.png"
    />
    <img
      class="carousel-img"
      src="../assets/carousel-4.png"
    />
  </n-carousel>
</template>

<style scoped>
.carousel-img {
  width: 100%;
  height: 380px;
  object-fit: cover;
}
</style>
