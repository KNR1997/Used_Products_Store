<script setup>
const props = defineProps(['state'])

</script>

<template>
  <div
    id="BottomMenu"
    v-if="state.onSellingPage"
    class="w-full bg-[#FAFAFA] border-b md:block hidden"
  >
    <ul
      class="flex items-center justify-end text-xs text-[#333333] font-light px-2 h-10 bg-[#FAFAFA] max-w-[1200px]"
    >
      <router-link to="productSearch">
        <li
          class="border-r border-r-gray-400 px-3 hover:text-[#FF4646] cursor-pointer"
        >
          Overview
        </li>
      </router-link>
      <router-link to="productAddEdit">
        <li
          class="border-r border-r-gray-400 px-3 hover:text-[#FF4646] cursor-pointer"
        >
          Sell an item
        </li>
      </router-link>
      <router-link to="#">
        <li
          class="border-r border-r-gray-400 px-3 hover:text-[#FF4646] cursor-pointer"
        >
          Drafts
        </li>
      </router-link>
      <router-link to="#">
        <li
          class="border-r border-r-gray-400 px-3 hover:text-[#FF4646] cursor-pointer"
        >
          Scheduled
        </li>
      </router-link>
      <router-link to="#">
        <li
          class="border-r border-r-gray-400 px-3 hover:text-[#FF4646] cursor-pointer"
        >
          Active
        </li>
      </router-link>
      <router-link to="#">
        <li
          class="border-r border-r-gray-400 px-3 hover:text-[#FF4646] cursor-pointer"
        >
          Sold
        </li>
      </router-link>
      <router-link to="#">
        <li
          class="border-r border-r-gray-400 px-3 hover:text-[#FF4646] cursor-pointer"
        >
          Unsold
        </li>
      </router-link>
      <router-link to="productSearch">
        <li
          class="border-r border-r-gray-400 px-3 hover:text-[#FF4646] cursor-pointer"
        >
          Products
        </li>
      </router-link>
    </ul>
  </div>
</template>
