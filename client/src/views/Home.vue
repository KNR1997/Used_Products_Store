<script setup>
import ProductComponent from '../components/ProductComponent.vue';
import { onMounted, reactive } from 'vue'

const state = reactive({
  products: null,
});

onMounted(async () => {
  await fetchAllProducts();
});

async function fetchAllProducts() {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/getAllProducts');
    let result = await response.json();
    state.products = result

  } catch (error) {
    console.error(error);
  }
}
</script>

<template>
  <div v-if="state.products" id="IndexPage" class="mt-4 max-w-[1200px] mx-auto px-2">
      <div class="grid xl:grid-cols-6 lg:grid-cols-5 md:grid-cols-4 sm:grid-cols-3 grid-cols-2 gap-4">
        <div  v-for="product in state.products" :key="product.id">
          <ProductComponent :product="product"/>
        </div>
      </div>
  </div>
</template>