<!-- components/DashboardLayout.vue -->
<template>
  <div>
    <Navbar />
    <router-view></router-view>
  </div>
</template>

<script setup>
import Sidebar from "../src/components/Sidebar.vue";
import Navbar from "../src/components/Navbar.vue";

</script>
