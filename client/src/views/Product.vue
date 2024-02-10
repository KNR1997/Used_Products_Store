<script setup>
import { computed, onMounted, ref, watch } from "vue";
import { useRoute } from "vue-router";
import { cartStore } from "../store/store";
import { StarIcon, HeartIcon } from "@heroicons/vue/24/solid";

let product = ref({});
let items = ref([]);
let currentImage = ref(null);

let url = "https://picsum.photos/id/1/800/800";

const images = ref([
  "",
  "https://picsum.photos/id/212/800/800",
  "https://picsum.photos/id/233/800/800",
  "https://picsum.photos/id/165/800/800",
  "https://picsum.photos/id/99/800/800",
  "https://picsum.photos/id/144/800/800",
]);

onMounted(async () => {
  const route = useRoute();
  const productId = route.params.id;

  try {
    const response = await fetch(
      `http://127.0.0.1:8000/api/getProduct/${productId}`
    );
    product.value = await response.json();
    console.log(product.value);
  } catch (error) {
    console.error(error);
  }
});

watch(() => {
  if (product.value) {
    currentImage.value = url;
    images.value[0] = url;
  }
});

const addToCart = () => {
  cartStore().addItem({
    product: product.value,
    quantity: 1,
  });
};

const watchedItems = computed(() => cartStore().getItems());
items.value = watchedItems;

const isInCart = computed(() => {
  let res = false;
  cartStore()
    .getItems()
    .forEach((prod) => {
      if (product.value.id == prod.product.id) {
        res = true;
      }
    });
  return res;
});

const priceComputed = computed(() => {
  return (product.value.price - product.value.price * 0.05).toFixed(2);
});
</script>

<template>
  <div id="ItemPage" class="mt-4 max-w-[1200px] mx-auto px-2">
    <div class="md:flex gap-4 justify-between mx-auto w-full">
      <div class="md:w-[40%]">
        <img
          v-if="currentImage"
          class="rounded-lg object-fit"
          :src="currentImage"
        />
        <div
          v-if="images[0] !== ''"
          class="flex items-center justify-center mt-2"
        >
          <div v-for="image in images" :key="image.id">
            <img
              @mouseover="currentImage = image"
              @click="currentImage = image"
              width="70"
              class="rounded-md object-fit border-[3px] cursor-pointer"
              :class="currentImage === image ? 'border-[#FF5353]' : ''"
              :src="image"
            />
          </div>
        </div>
      </div>
      <div class="md:w-[60%] bg-white p-3 rounded-lg">
        <div v-if="product">
          <div class="flex items-center justify-start gap-2 my-2">
            <div class="text-xl font-bold text-red-500">LKR</div>
            <div class="text-4xl font-bold text-red-500">
              {{ priceComputed }}
            </div>
          </div>

          <div class="flex items-center justify-start gap-2 my-2">
            <div class="font-bold text-base line-through">
              LKR {{ product.price }}
            </div>
            <span
              class="bg-[#F5F5F5] border text-[#C08562] text-[9px] font-semibold px-1.5 rounded-sm"
              >5% off</span
            >
          </div>

          <!-- <p class="mb-2">{{ product.title }}</p> -->
          <p class="font-light text-[16px] mb-2">{{ product.description }}</p>
        </div>

        <div class="flex items-center pt-1.5">
          <span class="h-4 min-w-4 rounded-full p-0.5 bg-[#FFD000] mr-2">
            <StarIcon class="icon" />
          </span>
          <p class="text-[#FF5353]">Extra 5% off</p>
        </div>

        <div class="flex items-center justify-start my-2">
          <span class="h-5 min-w-5 rounded-full p-0.5 bg-[#FFFF] mr-2">
            <StarIcon class="icon" style="color: red;" />
          </span>
          <div class="text-[13px] font-light ml-2">{{ product.rating }}</div>
          <div class="text-[13px] font-light ml-2">
            {{ product.reviews }} Reviews | {{ product.sold }}+ sold
          </div>
        </div>

        <div class="border-b" />

        <p class="text-[#009A66] text-xs font-semibold pt-1">
          Free 11-day delivery over ￡8.28
        </p>

        <p class="text-[#009A66] text-xs font-semibold pt-1">
          Free Shipping
        </p>

        <div class="py-2" />

        <div class="flex align-bottom">
          <button
            @click="addToCart()"
            :disabled="isInCart"
            class="px-6 py-2 rounded-lg text-white text-lg font-semibold bg-gradient-to-r from-[#FF851A] to-[#FFAC2C]"
          >
            <div v-if="isInCart">Is Added</div>
            <div v-else>Add to Cart</div>
          </button>
          <HeartIcon
            class="icon"
            style="
              color: transparent;
              height: 30px;
              margin-top: 8px;
              margin-left: 20px;
              stroke: black;
            "
          />
        </div>
      </div>
    </div>
  </div>
</template>
