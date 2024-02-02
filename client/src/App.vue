<script setup>
import Footer from './components/Footer.vue'
import Navbar from './components/Navbar.vue'
import Home from './views/Home.vue';

</script>

<template>
  <div>
    <Navbar />
    <router-view />
    <Footer />
  </div>
</template>

<style scoped>
</style>
