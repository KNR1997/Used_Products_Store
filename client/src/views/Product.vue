<script setup>
import { computed, onMounted, ref, watch } from "vue";
import { useRoute } from "vue-router";
import { cartStore, authStore } from "../store/store";
import { StarIcon, HeartIcon, HandThumbUpIcon } from "@heroicons/vue/24/solid";
import ProductCommentBox from "../components/ProductCommentBox.vue";
import ProductCommentInput from "../components/ProductCommentInput.vue";

let product = ref({});
let reviews = ref([]);
let items = ref([]);
let currentImage = ref(null);
let addNewReview = ref(false);
let userReview = ref("");

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
    let data = await response.json();
    product.value = data.product;
    reviews.value = data.reviews;
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

const addReview = () => {
  addNewReview.value = true;
};

const postComment = async (data) => {
  try {
    const user = authStore().getUser();

    console.log("data: ", data);

    const payload = {
      user_id: user.user_id,
      product_id: product.value.id,
      review: data,
    };

    const endpoint = `http://127.0.0.1:8000/api/save-review`;

    const response = await fetch(endpoint, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    // Check if the request was successful
    if (response.ok) {
      addNewReview.value = false;
      // Optionally, update the state or perform other actions upon successful submission
    } else {
      console.error("Failed to submit review");
    }
  } catch (error) {
    console.log("Error during review submission", error);
  }
};

const closeCommentBox = () => {
  addNewReview.value = false;
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

const reviewdByUser = computed(() => {
  const user = authStore().getUser();

  if (Array.isArray(reviews.value) && reviews.value.length > 0) {
    return reviews.value.some((review) => {
      if (review.user === user.user_id) {
        userReview.value = review.review; // update userReview
        return true;
      }
      return false;
    });
  }
  return false;
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

    <div class="border-b" />

    <div id="comment">
      <div id="top" class="md:flex gap-4 justify-between mx-auto w-full pb-8">
        <div id="left">
          <p class="text-2xl font-bold py-10">Customer Reviews (3298)</p>
          <p class="text-6xl font-bold pb-4">4.7</p>
          <div id="stars" class="flex">
            <StarIcon class="icon" style="height: 30px;" />
            <StarIcon class="icon" style="height: 30px;" />
            <StarIcon class="icon" style="height: 30px;" />
          </div>
          <p>All reviews come from verified purchasers</p>
        </div>
        <div id="right">
          <div class="py-10">
            <button
              @click="addReview()"
              class="px-6 py-2 rounded-lg text-white text-lg font-semibold bg-gradient-to-r from-[#e6a67c] to-[#cea05c]"
            >
              <div v-if="reviewdByUser">Edit</div>
              <div v-else>Add Comment</div>
            </button>
          </div>
        </div>
      </div>
      <div v-for="review in reviews" :key="review.id">
        <ProductCommentBox :review="review" />
      </div>
      <section v-if="addNewReview" class="py-5">
        <ProductCommentInput
          @post-comment="postComment"
          @close="closeCommentBox"
          :userReview="userReview"
        />
      </section>
    </div>
  </div>
</template>
