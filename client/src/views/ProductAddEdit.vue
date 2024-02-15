<script setup>
import { onMounted, reactive, ref } from "vue";
import { NForm, NFormItem, NInput, NButton } from "naive-ui";
import { productStore } from "../store/store";

const formValue = reactive({
  name: null,
  title: null,
  stock: null,
  price: null,
  rating: null,
  reviews: null,
  sold: null,
  description: null
});

onMounted(() => {
  // Access the selected product data from the store
  const selectedProduct = productStore().getProductData();
  if (selectedProduct) {
    formValue.name = selectedProduct.name;
    formValue.title = selectedProduct.title;
    formValue.stock = selectedProduct.quantity;
    formValue.price = selectedProduct.price;
    formValue.description = selectedProduct.description;
  }
})
</script>

<template>
  <div class="mt-4 max-w-[1200px] mx-auto px-2">
    <n-form
      ref="formRef"
      inline
      :label-width="80"
      :model="formValue"
      :rules="rules"
      :size="size"
    >
      <n-form-item label="Name" path="user.name">
        <n-input v-model:value="formValue.name" placeholder="Input Name" />
      </n-form-item>
      <n-form-item label="Title" path="user.age">
        <n-input v-model:value="formValue.title" placeholder="Input Title" />
      </n-form-item>
      <n-form-item label="Price" path="user.price">
        <n-input v-model:value="formValue.price" placeholder="Input Price" />
      </n-form-item>
      <n-form-item label="Stock" path="stock">
        <n-input v-model:value="formValue.stock" placeholder="Stock" />
      </n-form-item>
      <n-form-item label="Description" path="description">
        <n-input v-model:value="formValue.description" placeholder="Description" />
      </n-form-item>
      <n-form-item>
        <n-button @click="handleValidateClick">
          Validate
        </n-button>
      </n-form-item>
    </n-form>
  </div>
</template>
