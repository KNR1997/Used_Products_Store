<script setup>
import { computed, onMounted, reactive, watch } from "vue";
import { authStore, cartStore } from "../store/store";
import eventBus from "../EventBus";
import {
  ShoppingCartIcon,
  MagnifyingGlassIcon,
  EyeDropperIcon,
} from "@heroicons/vue/24/solid";
import { useRouter } from "vue-router";
import { NDropdown, NIcon, NSpace, NButton } from "naive-ui";
import TopMenuBar from "./TopMenuBar.vue";
import BottomMenuBar from "./BottomMenuBar.vue";

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
    <TopMenuBar
      :state="state"
      @navigate-ToSelling="navigateToSelling"
      @sign-out="signOut"
    />

    <BottomMenuBar :state="state" />

    <div id="MainHeader" class="flex items-center w-full bg-white">
      <div
        class="flex lg:justify-start justify-between gap-10 max-w-[1150px] w-full px-3 py-5 mx-auto"
      >
        <router-link to="/" class="max-w-[100px]">
          <img src="../assets/e-commerce_logo.png" />
        </router-link>

        <n-space>
          <n-dropdown
            v-bind:trigger="click"
            :options="options"
            @select="handleSelect"
          >
            <n-button :bordered="false"> Shop by <br />category</n-button>
          </n-dropdown>
        </n-space>

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
