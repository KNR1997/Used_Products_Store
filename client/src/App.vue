<script setup>
import MainLayout from "../layouts/MainLayout.vue";
import DashboardLayout from "../layouts/DashboardLayout.vue";
import Error from './components/Error.vue';

import {
  NMessageProvider,
  NDialogProvider,
  NConfigProvider,
  darkTheme,
} from "naive-ui";

const themeOverrides = {
  common: {
    primaryColor: "red",
  },
  Button: {
    textColor: "black",
  },
  Select: {
    peers: {
      InternalSelection: {
        textColor: "black",
      },
    },
  },
};
</script>

<template>
  <n-config-provider :theme-overrides="themeOverrides">
    <n-dialog-provider>
      <n-message-provider placement="top-right">
        <DashboardLayout />
        <Error />
      </n-message-provider>
    </n-dialog-provider>
  </n-config-provider>
</template>

<style scoped></style>
