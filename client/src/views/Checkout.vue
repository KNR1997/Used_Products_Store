<script setup>
import { computed, onMounted, ref } from "vue";
import { cartStore } from "../store/store";
import CheckoutItem from '../components/CheckoutItem.vue'

let currentAddress = ref({})
let total = ref(0)

onMounted(async () => {
    try {
        const response = await fetch(`http://127.0.0.1:8000/api/get-address/2`);
        currentAddress.value = await response.json();
    } catch (error) {
        console.error(error);
    }

    cartStore().getItems().forEach(item => {
        total.value += parseInt(item.product.price * item.quantity)
    })
})

const addressDetails = computed(() => {
    return currentAddress;
})

const totalPrice = computed(() => {
    return total;
})
</script>

<template>
    <div>
        <div id="CheckoutPage" class="mt-4 max-w-[1200px] mx-auto px-2">
  
            <div class="md:flex gap-4 justify-between mx-auto w-full">
                <div class="md:w-[65%]">
                    <div class="bg-white rounded-lg p-4">

                        <div class="text-xl font-semibold mb-2">Shipping Address</div>

                        <div v-if="true">
                            <router-link 
                                to="/address"
                                class="flex items-center pb-2 text-blue-500 hover:text-red-400"
                            >
                                <Icon name="mdi:plus" size="18" class="mr-2"/>
                                Update Address
                            </router-link>

                            <div class="pt-2 border-t">
                                <div class="underline pb-1">Delivery Address</div>
                                <ul class="text-xs">
                                    <li class="flex items-center gap-2">
                                        <div>Contact name:</div> 
                                        <div class="font-bold">{{ addressDetails.value.contact_name}}</div>
                                    </li>
                                    <li class="flex items-center gap-2">
                                        <div>Address:</div> 
                                        <div class="font-bold">{{ addressDetails.value.address }}</div>
                                    </li>
                                    <li class="flex items-center gap-2">
                                        <div>Zip Code:</div> 
                                        <div class="font-bold">{{ addressDetails.value.zip_code }}</div>
                                    </li>
                                    <li class="flex items-center gap-2">
                                        <div>City:</div> 
                                        <div class="font-bold">{{ addressDetails.value.city }}</div>
                                    </li>
                                    <li class="flex items-center gap-2">
                                        <div>Country:</div> 
                                        <div class="font-bold">{{ addressDetails.value.country }}</div>
                                    </li>
                                </ul>
                            </div>
                        </div>

                        <router-link 
                            v-else
                            to="/address"
                            class="flex items-center text-blue-500 hover:text-red-400"
                        >
                            <Icon name="mdi:plus" size="18" class="mr-2"/>
                            Add New Address
                        </router-link>
                    </div>

                    <div id="Items" class="bg-white rounded-lg p-4 mt-4">
                        <div v-for="product in cartStore().getItems()" :key="product.id">
                            <CheckoutItem :product="product" />
                        </div>
                    </div>
                </div>

                <div class="md:hidden block my-4"/>
                <div class="md:w-[35%]">
                    <div id="PlaceOrder" class="bg-white rounded-lg p-4">

                        <div class="text-2xl font-extrabold mb-2">Summary</div>

                        <div class="flex items-center justify-between my-4">
                            <div class="">Total Shipping</div>
                            <div class="">Free</div>
                        </div>

                        <div class="border-t" />

                        <div class="flex items-center justify-between my-4">
                            <div class="font-semibold">Total</div>
                            <div class="text-2xl font-semibold">
                                $ <span class="font-extrabold">{{ totalPrice }}</span>
                            </div>
                        </div>

                        <form @submit.prevent="pay()">
                            <div 
                                class="border border-gray-500 p-2 rounded-sm" 
                                id="card-element" 
                            />

                            <p 
                                id="card-error" 
                                role="alert" 
                                class="text-red-700 text-center font-semibold" 
                            />

                            <button 
                                :disabled="isProcessing"
                                type="submit"
                                class="
                                mt-4
                                    bg-gradient-to-r 
                                  from-[#FE630C] 
                                  to-[#FF3200]
                                    w-full 
                                    text-white 
                                    text-[21px] 
                                    font-semibold 
                                    p-1.5 
                                    rounded-full
                                "
                                :class="isProcessing ? 'opacity-70' : 'opacity-100'"
                            >
                                <Icon v-if="isProcessing" name="eos-icons:loading" />
                                <div v-else>Place order</div>
                            </button>
                        </form>

                    </div>

                    <div class="bg-white rounded-lg p-4 mt-4">
                        <div class="text-lg font-semibold mb-2 mt-2">AliExpress</div>
                        <p class="my-2">
                            AliExpress keeps your information and payment safe
                        </p>

                    </div>
                </div>
            </div>
        </div>
    </div>
</template>