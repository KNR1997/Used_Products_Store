<script setup>
import { onMounted, ref } from "vue";
import { authStore } from "../store/store";

let orderDetails = ref();
let url = 'https://picsum.photos/id/1/800/800';

onMounted(async () => {
  let user = authStore().getUser();

  try {
    const response = await fetch(
      `http://127.0.0.1:8000/api/getUserOrders/${user.user_id}`
    );
    orderDetails.value = await response.json();
    console.log(orderDetails.value.user_address);
  } catch (error) {
    console.error(error);
  }
});
</script>

<template>
  <div>
    <div id="OrdersPage" class="mt-4 max-w-[1200px] mx-auto px-2 min-h-[50vh]">
      <div class="bg-white w-full p-6 min-h-[150px]">
        <div class="flex items-center text-xl">
          <Icon name="carbon:delivery" color="#5FCB04" size="35" />
          <span class="pl-4">Orders</span>
        </div>
        <div
          v-if="orderDetails"
          class="text-sm pl-[50px]"
        >
          <div class="border-b py-1">
            <p>Stripe ID: {{ orderDetails.user_address.id }}</p>

            <div class="pt-2"></div>

            <div v-for="item in orderDetails.user_orders" :key="item.id">
              <router-link
                class="flex items-center gap-3 p-1 hover:underline hover:text-blue-500"
                :to="`/item/${item.productId}`"
              >
                <img width="40" :src="url" />
                {{ item.product }}
              </router-link>
            </div>

            <div class="pt-2 pb-5">
              Delivery Address: {{ orderDetails.user_address.address }},
              {{ orderDetails.user_address.zipcode }},
              {{ orderDetails.user_address.city }},
              {{ orderDetails.user_address.country }}
            </div>
          </div>
        </div>

        <div v-else class="flex items-center justify-center">
          You have no order history
        </div>
      </div>
    </div>
  </div>
</template>
