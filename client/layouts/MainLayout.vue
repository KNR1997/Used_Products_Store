<!-- components/HomePageLayout.vue -->
<template>
  <div>
    <Navbar />
    <router-view></router-view>
    <Footer />
  </div>
</template>

<script setup>
import Footer from '../src/components/Footer.vue'
import Navbar from '../src/components/Navbar.vue'

</script>
