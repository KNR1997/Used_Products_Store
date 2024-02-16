<script setup>
import MainLayout from "../layouts/MainLayout.vue";
import DashboardLayout from "../layouts/DashboardLayout.vue";
import { NMessageProvider } from "naive-ui";
</script>

<template>
  <n-message-provider>
    <DashboardLayout />
  </n-message-provider>
</template>

<style scoped></style>
