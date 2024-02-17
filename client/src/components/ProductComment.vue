<script setup>
import { StarIcon, HandThumbUpIcon } from "@heroicons/vue/24/solid";
import { NRate } from "naive-ui";
import { ref } from "vue";

const props = defineProps(['review'])
const rating = ref(0);

const formatDate = (fullDate) => {
  const date = new Date(fullDate);
  const formattedDate = date.toISOString().split('T')[0];
  return formattedDate;
}
</script>

<template>
  <article>
      <div class="flex items-center mb-4">
          <img class="w-10 h-10 me-4 rounded-full" src="../assets/profile_pic.jpg" alt="">
          <div class="font-medium dark:text-white">
              <p> {{ props.review.user_details.username }} <time datetime="2014-08-16 19:00" class="block text-sm text-gray-500 dark:text-gray-400">Joined on August 2014</time></p>
          </div>
      </div>
      <div class="flex items-center mb-1 space-x-1 rtl:space-x-reverse">
        <n-rate allow-half :value="props.review.rating" />
        <h3 class="ms-2 text-sm font-semibold text-gray-900 dark:text-white">{{ props.review.title }}</h3>
      </div>
      <p class="mb-2 text-gray-500 dark:text-gray-400">{{ props.review.review }}</p>
      <footer class="mb-5 text-sm text-gray-500 dark:text-gray-400"><p>Reviewed on <time datetime="{{ props.review.date }}">{{ formatDate(props.review.date) }}</time></p></footer>
      <a href="#" class="block mb-5 text-sm font-medium text-blue-600 hover:underline dark:text-blue-500">Read more</a>
      <!-- <aside>
          <p class="mt-1 text-xs text-gray-500 dark:text-gray-400">19 people found this helpful</p>
          <div class="flex items-center mt-3">
              <a href="#" class="text-gray-900 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 font-medium rounded-lg text-xs px-2 py-1.5 dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700">Helpful</a>
              <a href="#" class="ps-4 text-sm font-medium text-blue-600 hover:underline dark:text-blue-500 border-gray-200 ms-4 border-s md:mb-0 dark:border-gray-600">Report abuse</a>
          </div>
      </aside> -->
  </article>
</template>