<script setup>
import { defineComponent, onMounted, ref, h } from "vue";
import { NButton, NDataTable, NSpace } from "naive-ui";
import { productStore } from "./store";
import { authStore } from "../../../store/store";
import { useRouter } from "vue-router";

const reviews = ref([]);
const product = ref({});
const openAddEdit = ref(false);
const router = useRouter();

onMounted(async () => {
  const selectedProduct = productStore().getProductData();
  product.value = selectedProduct;
  await fetchProductReviews(selectedProduct.id);
});

async function fetchProductReviews(product_id) {
  try {
    const response = await fetch(
      `http://127.0.0.1:8000/api/getReviewsByProductId/${product_id}`
    );
    let result = await response.json();
    reviews.value = result;
  } catch (error) {
    console.error(error);
  }
}

const columns = [
  {
    title: "Product_Id",
    key: "id",
  },
  {
    title: "UserName",
    key: "user_details.username"
  },
  {
    title: "Title",
    key: "title",
  },
  {
    title: "Review",
    key: "review",
  },
  {
    title: "Rating",
    key: "rating",
  }
];
</script>

<template>
  <div class="mt-4 max-w-[1600px] mx-auto px-2">
    <div class="flex justify-between py-5">
      <h1 class="px-2 text-2xl">Reviews - {{ product.name }}</h1>
    </div>
    <n-data-table :columns="columns" :data="reviews" />
  </div>
</template>
