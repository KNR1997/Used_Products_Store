<script setup>
import { defineComponent, onMounted, ref, h } from "vue";
import { NButton, NDataTable, NSpace } from "naive-ui";
import { productStore } from "./store";
import { authStore } from "../../../store/store";
import { useRouter } from "vue-router";

const data = ref([]);
const openAddEdit = ref(false);
const router = useRouter();

onMounted(async () => {
  const user = authStore().getUser();

  await fetchAllSellerProducts(user.user_id);
});

async function fetchAllSellerProducts(userId) {
  try {
    const response = await fetch(
      `http://127.0.0.1:8000/api/getProductsByUserId/${userId}`
    );
    let result = await response.json();
    data.value = result;
  } catch (error) {
    console.error(error);
  }
}

const columns = [
  {
    title: "Id",
    key: "id",
  },
  {
    title: "Name",
    key: "name",
  },
  {
    title: "Title",
    key: "title",
  },
  {
    title: "Price",
    key: "price",
  },
  // {
  //   title: "Description",
  //   key: "description",
  // },
  {
    title: "Stock",
    key: "quantity",
  },
  {
    title: "Rating",
    key: "rating",
  },
  {
    title: "Reviews",
    key: "reviews",
  },
  {
    title: "Sold",
    key: "sold",
  },
  {
    title: "Action",
    key: "actions",
    render(row) {
      return h(
        NButton,
        {
          strong: true,
          tertiary: true,
          size: "small",
          onClick: () => editProduct(row),
        },
        { default: () => "Edit" }
      );
    },
  },
  {
    title: "Show",
    key: "show",
    render(row) {
      return h(
        NButton,
        {
          strong: true,
          tertiary: true,
          size: "small",
          onClick: () => showReviews(row),
        },
        { default: () => "Reviews" }
      );
    },
  },
];

const editProduct = (row) => {
  productStore().setProductData(row);

  // Navigate to the productAddEdit route
  router.push({ name: "productAddEdit" });
};

const showReviews = (row) => {
  productStore().setProductData(row);

  // Navigate to the productAddEdit route
  router.push({ name: "productReviews" });
};

const addProduct = () => {
  productStore().clearProductData();

  router.push({ name: "productAddEdit" });
}
</script>

<template>
  <div class="mt-4 max-w-[1600px] mx-auto px-2">
    <div class="flex justify-between py-5">
      <h1 class="px-2 text-2xl">Products</h1>
      <div class="px-3">
        <n-button strong secondary type="info" @click="addProduct">
          Add
        </n-button>
      </div>
    </div>
    <n-data-table :columns="columns" :data="data" />
  </div>
</template>
