<script setup>
import { computed, onMounted, reactive, watch } from "vue";
import { authStore, cartStore } from "../store/store";
import eventBus from "../EventBus";
import {
  ShoppingCartIcon,
  MagnifyingGlassIcon,
  PhoneIcon,
  EyeDropperIcon,
} from "@heroicons/vue/24/solid";
import { useRouter } from "vue-router";
import { NDropdown, NIcon } from "naive-ui";

const state = reactive({
  isAccountMenu: false,
  isCartHover: false,
  user: false,
  onSellingPage: false,
});
const options = [
  {
    label: "Sports",
    key: "Sports",
    disabled: true,
  },
  {
    label: "Electronics",
    key: "Electronics",
  },
  {
    label: "Fashion",
    key: "Fashion",
  },
  {
    label: "Home & Garden",
    key: "Home & Garden",
  },
];

const router = useRouter();

onMounted(() => {
  getUserStatus();

  // Create a watcher for the user state
  watch(
    () => authStore().getUser(),
    (newUser) => {
      state.user = newUser;
    }
  );
});

const getUserStatus = () => {
  const store = authStore();
  state.user = store.getUser();
};

const signOut = () => {
  const store = authStore();
  store.logoutUser(); // Call the logoutUser action from the store
};

const navigateToSelling = () => {
  state.onSellingPage = true;
  router.push({ name: "productSearch" });
};

const renderIcon = () => {
  return h(NIcon, null, {
    default: () => h(EyeDropperIcon),
  });
};
</script>

<template>
  <div id="MainLayout" class="w-full z-50">
    <div id="TopMenu" class="w-full bg-[#FAFAFA] border-b md:block hidden">
      <ul
        class="flex items-center justify-end text-xs text-[#333333] font-light px-2 h-10 bg-[#FAFAFA] max-w-[1200px]"
      >
        <li
          class="border-r border-r-gray-400 px-3 hover:text-[#FF4646] cursor-pointer"
        >
          Sell on AliExpress
        </li>
        <li
          class="border-r border-r-gray-400 px-3 hover:text-[#FF4646] cursor-pointer"
        >
          Cookie Preferences
        </li>
        <li
          class="border-r border-r-gray-400 px-3 hover:text-[#FF4646] cursor-pointer"
        >
          <h2>Hi {{ state.user?.username }}</h2>
        </li>
        <li
          class="border-r border-r-gray-400 px-3 hover:text-[#FF4646] cursor-pointer"
        >
          Help
        </li>
        <li
          class="border-r border-r-gray-400 px-3 hover:text-[#FF4646] cursor-pointer"
        >
          Buyer Protection
        </li>
        <li class="flex px-3 hover:text-[#FF4646] cursor-pointer">
          <PhoneIcon class="icon" style="width: 15px; padding-right: 5px;" />
          App
        </li>
        <li
          @mouseenter="state.isAccountMenu = true"
          @mouseleave="state.isAccountMenu = false"
          class="relative flex items-center px-2.5 hover:text-[#FF4646] h-full cursor-pointer"
          :class="
            state.isAccountMenu
              ? 'bg-white border z-40 shadow-[0_15px_100px_40px_rgba(0,0,0,0.3)]'
              : 'border border-[#FAFAFA]'
          "
        >
          Account
          <div
            id="AccountMenu"
            v-if="state.isAccountMenu"
            class="absolute bg-white w-[220px] text-[#333333] z-40 top-[38px] -left-[100px] border-x border-b"
          >
            <div v-if="!state.user">
              <div class="text-semibold text-[15px] my-4 px-3">
                Welcome to AliExpress!
              </div>
              <div class="flex items-center gap-1 px-3 mb-3">
                <router-link
                  to="/auth"
                  class="bg-[#FF4646] text-center w-full text-[16px] rounded-sm text-white font-semibold p-2"
                >
                  Login / Register
                </router-link>
              </div>
            </div>
            <div class="border-b" />
            <ul class="bg-white">
              <router-link to="/orders">
                <li class="text-[13px] py-2 px-4 w-full hover:bg-gray-200">
                  My Orders
                </li>
              </router-link>
              <li
                @click="navigateToSelling"
                class="text-[13px] py-2 px-4 w-full hover:bg-gray-200"
              >
                My Selling
              </li>
              <li
                v-if="state.user"
                @click="signOut()"
                class="text-[13px] py-2 px-4 w-full hover:bg-gray-200"
              >
                Sign out
              </li>
            </ul>
          </div>
        </li>
      </ul>
    </div>
    <div
      v-if="state.onSellingPage"
      id="BottomMenu"
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
    <div id="MainHeader" class="flex items-center w-full bg-white">
      <div
        class="flex lg:justify-start justify-between gap-10 max-w-[1150px] w-full px-3 py-5 mx-auto"
      >
        <router-link to="/" class="max-w-[100px]">
          <img src="../assets/e-commerce_logo.png" />
        </router-link>

        <n-dropdown trigger="click" :options="options" @select="handleSelect">
          <n-button :render-icon="renderIcon"
            >Shop by <br />
            Category</n-button
          >
        </n-dropdown>

        <div class="max-w-[700px] w-full md:block hidden">
          <div class="relative">
            <div
              class="flex items-center border-4 border-gray rounded-md w-full"
            >
              <input
                class="w-full placeholder-gray-400 text-sm pl-3"
                placeholder="kitchen accessories"
                type="text"
                v-model="searchItem"
              />
              <MagnifyingGlassIcon
                class="icon"
                style="
                  height: 40px;
                  width: 40px;
                  color: white;
                  background-color: red;
                "
              />
            </div>
          </div>
        </div>

        <router-link :to="`/shoppingcart`" class="flex items-center">
          <button
            class="relative md:block hidden"
            @mouseenter="isCartHover = true"
            @mouseleave="isCartHover = false"
          >
            <span
              class="absolute flex items-center justify-center -right-[3px] top-0 bg-[#FF4646] h-[17px] min-w-[17px] text-xs text-white px-0.5 rounded-full"
            >
              {{ cartStore().getItems().length }}
            </span>
            <div class="min-w-[40px]">
              <ShoppingCartIcon class="icon" />
            </div>
          </button>
        </router-link>
      </div>
    </div>
  </div>
</template>
