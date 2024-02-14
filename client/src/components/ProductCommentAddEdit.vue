<script setup>
import { TrashIcon } from "@heroicons/vue/24/solid";

import { onMounted, ref } from "vue";

const title = ref('');
const comment = ref('');
const rating = ref(4);
const emit = defineEmits(['post-comment', 'close', 'delete-review']);
const props = defineProps(['userReview']);

onMounted(() => {
    if(props.userReview != null) {
        comment.value = props.userReview.review
    }
})

const postComment = () => {
    let data = {
        title: title.value,
        comment: comment.value, 
        rating: rating.value
    }
    emit('post-comment', data)
}

const closeBox = () => {
    emit('close')
}

const deleteReview = () => {
    emit('delete-review', props.userReview.id)
}

</script>

<template>
    <form @submit.prevent="handleSubmit" method="post">
        <div class="w-full mb-4 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-700 dark:border-gray-600">
            <div class="px-4 py-2 bg-white rounded-t-lg dark:bg-gray-800">
                <label for="comment" class="sr-only">Your comment</label>
                <textarea v-model="title" id="title" rows="1" class="w-full px-0 text-sm text-gray-900 font-bold bg-white border-0 dark:bg-gray-800 focus:ring-0 dark:text-white dark:placeholder-gray-400" placeholder="Title..." required></textarea>
                <textarea v-model="comment" id="comment" rows="4" class="w-full px-0 text-sm text-gray-900 bg-white border-0 dark:bg-gray-800 focus:ring-0 dark:text-white dark:placeholder-gray-400" placeholder="Write a comment..." required></textarea>
            </div>
            <div class="flex items-center justify-between px-3 py-2 border-t dark:border-gray-600">
                <button @click="postComment" class="inline-flex items-center py-2.5 px-4 text-xs font-medium text-center text-white bg-blue-700 rounded-lg focus:ring-4 focus:ring-blue-200 dark:focus:ring-blue-900 hover:bg-blue-800">
                    Post comment
                </button>
                <section class="flex justify-between">
                    <button @click="deleteReview" class="px-5">
                        <TrashIcon class="icon" style="height: 20px;"/>
                    </button>
                    <button @click="closeBox" class="inline-flex items-center py-2.5 px-4 text-xs font-medium text-center text-white bg-red-700 rounded-lg focus:ring-4 focus:ring-blue-200 dark:focus:ring-blue-900 hover:bg-red-800">
                        Cancel
                    </button>
                </section>
            </div>
        </div>
    </form>
</template>