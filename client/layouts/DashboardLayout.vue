<!-- components/DashboardLayout.vue -->
<template>
  <div>
    <Navbar />
    <router-view></router-view>
    <Footer />
  </div>
</template>

<script setup>
import Navbar from "../src/components/Navbar.vue";
import Footer from '../src/components/Footer.vue'

</script>
