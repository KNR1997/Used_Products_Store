<script setup>
const props = defineProps(['product'])
let url = 'https://picsum.photos/id/1/200/200';

</script>

<template>
    <div class="flex justify-start my-2">
        <img 
            class="rounded-md md:w-[150px] w-[90px]" 
            :src="url"
        >

        <div class="overflow-hidden pl-2">
            <div class="flex items-center">
                <span class="bg-[#FD374F] text-white text-[9px] font-semibold px-1.5 rounded-sm min-w-[80px]">Welcome Deal</span>
                <div class="truncate pl-2">{{ product.product.title }} </div>
            </div>

            <div class="text-lg font-semibold mt-2">
                $ <span class="font-bold">{{ product.product.price }} * {{ product.quantity }}</span>
            </div>
        </div>
    </div>
</template>