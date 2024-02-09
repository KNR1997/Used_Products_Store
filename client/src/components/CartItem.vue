<script setup>
import { computed, ref } from 'vue';
import { TrashIcon, PlusIcon, MinusIcon } from "@heroicons/vue/24/solid";
import { cartStore } from "../store/store";

const props = defineProps(['product', 'selectedArray'])

const emit = defineEmits(['selectedRadio'])

let isHover = ref(false)
let isSelected = ref(false)
let quantity = ref(props.product.quantity)

let url = 'https://picsum.photos/id/1/200/200';

const removeFromCart = () => {
    cartStore().getItems().forEach((prod, index) => {
        if (prod.id === props.product.id) {
            cartStore().getItems().splice(index, 1);
        }
    })
}

const increment = () => {
    quantity.value++;
    console.log('increment')

    // Find the item in cartStore and increment its quantity
    const cartItems = cartStore().getItems();
    const cartItemIndex = cartItems.findIndex(item => item.product.id === props.product.product.id);

    if (cartItemIndex !== -1) {
        // If the item is found in cartStore, increment its quantity
        cartItems[cartItemIndex].quantity++;
    }
}

const decrement = () => {
    if(quantity.value != 1) {
        quantity.value--;
        console.log('decrease')

        // Find the item in cartStore and increment its quantity
        const cartItems = cartStore().getItems();
        const cartItemIndex = cartItems.findIndex(item => item.product.id === props.product.product.id);

        if (cartItemIndex !== -1) {
            // If the item is found in cartStore, increment its quantity
            cartItems[cartItemIndex].quantity--;
        }
    }
}

const quantityValue = computed(() => {
    return quantity;
});

</script>

<template>
    <div class="flex justify-start my-2">
        <div class="my-auto">
            <div 
                @mouseenter="isHover = true"
                @mouseleave="isHover = false"
                class="flex items-center justify-start p-0.5 cursor-pointer"
            >
                <div 
                    @click="isSelected = !isSelected"
                    class=" flex items-center justify-center h-[20px] w-[20px] rounded-full border mr-5 ml-2"
                    :class="[
                        isHover ? 'border-[#FD374F]' : 'border-gray-300',
                        isSelected ? 'bg-[#FD374F]' : ''
                    ]"
                >
                    <div class="h-[8px] w-[8px] rounded-full bg-white" />
                </div>
            </div>
        </div>

        <img 
            class="rounded-md md:w-[150px] w-[90px]" 
            :src="url"
        >

        <div class="overflow-hidden pl-2 w-full">
            <div class="flex items-center justify-between w-full">
                <div class="flex items-center justify-between truncate">
                    <span class="sm:block hidden bg-[#FD374F] text-white text-[9px] font-semibold px-1.5 rounded-sm min-w-[80px]">Welcome Deal</span>
                    <div class="truncate sm:pl-2">{{ product.product.title }}</div>
                </div>
                <button 
                    @click="removeFromCart()"
                    class="mx-3 sm:block hidden -mt-0.5 hover:text-red-500"
                >
                    <Icon name="material-symbols:delete-outline" size="20" />
                </button>
            </div>

            <div class="text-xl font-semibold">
                $ <span class="font-bold">{{ product.product.price }}</span>
            </div>

            <p class="text-[#009A66] text-xs font-semibold pt-1">
                Free 11-day delivery over ￡8.28
            </p>

            <p class="text-[#009A66] text-xs font-semibold pt-1">
                Free Shipping
            </p>
        </div>

        <div>
            <div class="flex items-center justify-end">
                <button @click="removeFromCart()" class="hover:text-red-500">
                    <span class="h-9 min-w-9 rounded-full p-1 bg-[#FFFF] mr-2">
                        <TrashIcon class="icon" />
                    </span>
                </button>
            </div>
            <div class="flex justify-start items-center">
                <button>
                    <span class="h-9 min-w-9 p-1 bg-[#FFFF] mr-2">
                        <MinusIcon @click="decrement" class="icon" style="background-color: rgb(219, 219, 219)"/>
                    </span>
                </button>
                <div class="p-2">
                    <h2>{{ product.quantity }}</h2>
                </div>
                <button>
                    <span class="h-9 min-w-9 rounded-full p-1 bg-[#FFFF] mr-2">
                        <PlusIcon @click="increment" class="icon" style="background-color: rgb(219, 219, 219)"/>
                    </span>
                </button>
            </div>
        </div>
    </div>
</template>