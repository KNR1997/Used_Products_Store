<script setup>
import { computed } from 'vue';

const props = defineProps(['product'])
const product = props.product;
let url = 'https://picsum.photos/id/1/200/300';

const priceComputed = computed(() => {
    return (product.price - product.price*0.05).toFixed(2)
})

</script>

<template>
    <div 
        :id="`ProductComponent${product.id}`"
        class="
            bg-white 
            inline-block 
            rounded 
            hover:shadow-[0_0_10px_3px_rgba(0,0,0,0.15)] 
            cursor-pointer
        "
    >
        <router-link :to="`/product/${product.id}`">
            <img 
                class="rounded-t "
                :src="url"
            >

            <div id="ProductDetails">
            
                <span class="flex items-center justify-start gap-3 px-1 pt-1">
                    <span class="text-[#FF6674] font-semibold">${{ priceComputed }}</span>
                    <span class="text-gray-500 text-sm text-light line-through">${{ product.price }}</span>
                </span>

                <span class="px-1 relative -top-1.5 text-[#FF6674] text-xs font-semibold">
                    Extra 5% off
                </span>

                <div>
                    {{  user }}
                </div>

                <div class="flex items-center gap-1 px-1 relative -top-1">
                    <span class="bg-[#FD374F] text-white text-[9px] font-semibold px-1.5 rounded-sm">Welcome Deal</span>
                    <span class="bg-[#F5F5F5] border text-[#C08562] text-[9px] font-semibold px-1.5 rounded-sm">Top Selling</span>
                </div>

                <p class="flex items-center px-1 pt-0.5 text-xs text-[#252525]">
                    5,000+ sold <Icon name="material-symbols:star-rate" color="#757575" class="ml-1.5"/> 4.7
                </p>

                <p class="px-1 pt-0.5 text-xs text-[#252525]">
                    {{ product.title.substring(0,60) }}
                </p>

                <p class="px-1 pb-1">
                    <span class="text-[#009A66] text-xs font-semibold">Free Shipping</span>
                </p>

            </div>
        </router-link>
    </div>
</template>