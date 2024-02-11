<script setup>
import { StarIcon, HandThumbUpIcon } from "@heroicons/vue/24/solid";

</script>

<template>
  <div class="flex-column">
    
    <div class="flex justify-between">
      <div class="flex">
        <StarIcon class="icon" style="width: 25px;"/>
        <StarIcon class="icon" style="width: 25px;"/>
        <StarIcon class="icon" style="width: 25px; color: transparent; stroke: black;"/>
      </div>
      <p>Date</p>
    </div>

    <div class="flex justify-between">
      <h2 class="text-zinc-500">This is the comment</h2>
      <p>Customer name</p>
    </div>

    <div class="flex mt-4">
      <HandThumbUpIcon class="icon" style="width: 25px;"/>
      <p class="px-5">Helpful(3)</p>
    </div>

  </div>
</template>