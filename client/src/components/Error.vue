<script setup>
import { onUpdated, ref, toRaw, watch } from "vue";
import { useMessage } from "naive-ui";
import { appStates } from "../store/store";

const message = useMessage();
const error = ref();

watch(
  () => appStates().getMessage(),
  (newError) => {
    const rawError = toRaw(newError); // Get the target object from the proxy
    error.value = "error occured";
    showMessage();
  }
);

const showMessage = () => {
  if (error.value) {
    message.error(error.value, {
      duration: 5e3,
    });
  }
};
</script>

<template> </template>
