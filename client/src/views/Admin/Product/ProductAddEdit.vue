<script setup>
import { onMounted, reactive, ref } from "vue";
import { NForm, NFormItem, NInput, NButton, useMessage } from "naive-ui";
import { authStore } from "../../../store/store";
import { productStore } from "./store";
import { putData } from "../../../api/fetch";
import { useRouter } from "vue-router";

const formRef = ref(null);
const formStatus = ref("Add");
const router = useRouter();
const message = useMessage();

const formValue = reactive({
  id: null,
  name: null,
  title: null,
  price: null,
  quantity: null || 0,
  rating: null || 0,
  reviews: null || 0,
  sold: null || 0,
  description: null,
  user_id: null,
});

onMounted(() => {
  // Access the selected product data from the store
  const selectedProduct = productStore().getProductData();
  const user = authStore().getUser();

  formValue.user_id = user.user_id;

  if (selectedProduct && user) {
    formStatus.value = "Edit";
    formValue.id = selectedProduct.id;
    formValue.name = selectedProduct.name;
    formValue.title = selectedProduct.title;
    formValue.quantity = selectedProduct.quantity;
    formValue.price = selectedProduct.price;
    formValue.description = selectedProduct.description;
    formValue.rating = selectedProduct.rating;
    formValue.sold = selectedProduct.sold;
    formValue.reviews = selectedProduct.reviews;
  }
});

const rules = {
  name: {
    required: true,
    message: "Please input your Product name",
    trigger: "blur",
  },
  title: {
    required: true,
    message: "Please input Product title",
    trigger: ["input", "blur"],
  },
  price: {
    required: true,
    message: "Please input Product price",
    trigger: ["input"],
  },
  quantity: {
    required: true,
    message: "Please input available stock",
    trigger: ["input"],
  },
  description: {
    required: true,
    message: "Please input Product description",
    trigger: ["input"],
  },
};

const handleSaveClick = (e) => {
  e.preventDefault();
  formRef.value?.validate((errors) => {
    if (!errors) {
      console.log("no errors");
      saveProduct();
      // message.success("Valid");
    } else {
      console.log(errors);
    }
  });
};

const saveProduct = async () => {
  const url = "http://127.0.0.1:8000/api/saveProduct";

  let response = putData(url, formValue);
  if (response) {
    message.success(
      "Product Save!!!"
    );
    setTimeout(() => {
      router.push({ name: "productSearch" });
    }, 2000)
  }
};
</script>

<template>
  <div class="mt-4 max-w-[1600px] mx-auto px-2">
    <div class="flex justify-between py-5">
      <h1 class="px-2 text-2xl">Product - {{ formStatus }}</h1>
    </div>
    <n-form
      ref="formRef"
      :label-width="100"
      :model="formValue"
      label-placement="left"
      :rules="rules"
    >
      <n-form-item label="Name" path="name">
        <n-input v-model:value="formValue.name" placeholder="Input Name" />
      </n-form-item>
      <n-form-item label="Title" path="title">
        <n-input v-model:value="formValue.title" placeholder="Input Title" />
      </n-form-item>
      <n-form-item label="Price" path="price">
        <n-input v-model:value="formValue.price" placeholder="Input Price" />
      </n-form-item>
      <n-form-item label="Quantity" path="quantity">
        <n-input v-model:value="formValue.quantity" placeholder="Quantity" />
      </n-form-item>
      <n-form-item label="Description" path="description">
        <n-input
          v-model:value="formValue.description"
          placeholder="Description"
        />
      </n-form-item>
      <n-form-item>
        <n-button strong secondary type="primary" @click="handleSaveClick">
          Save
        </n-button>
      </n-form-item>
      <n-form-item>
        <!-- <n-button strong secondary type="error" @click="handleStatusClick">
          Inactive
        </n-button> -->
      </n-form-item>
    </n-form>
  </div>
</template>
