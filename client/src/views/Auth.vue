<script>
import axios from 'axios';
import { authStore } from '../store/store';
import eventBus from '../EventBus';

export default {
  name: 'Signin',
  
  data() {
    return {
      username: '',
      password: ''
    }
  },

  methods: {
    async handleSubmit(){
      const response = await axios.post('api/token/', {
        username: this.username,
        password: this.password
      });

      if(response.status === 200){
        authStore().setUser(response.data);
        this.$router.push('/');

        // Emit the custom event to trigger Navbar refresh
        eventBus.emit('refreshNavbar');
      }else{
        alert('Something went wrong!')
      }
    }
  },
}
</script>

<template>
    <div id="AuthPage" class="w-full h-[55vh] bg-white flex justify-center items-center">
      <form @submit.prevent="handleSubmit" method="post" class="max-w-md p-6 bg-gray-100 rounded-md shadow-md">
        <div class="mb-4">
          <label for="username" class="block text-gray-700 text-sm font-bold mb-2">Username</label>
          <input
            type="text"
            id="username"
            name="username"
            v-model="username"
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-indigo-500"
          />
        </div>
  
        <div class="mb-6">
          <label for="password" class="block text-gray-700 text-sm font-bold mb-2">Password</label>
          <input
            type="password"
            id="password"
            name="password"
            v-model="password"
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-indigo-500"
          />
        </div>
  
        <button
          class="w-full bg-indigo-500 text-white font-bold py-2 px-4 rounded-md hover:bg-indigo-700 focus:outline-none focus:shadow-outline-indigo active:bg-indigo-800"
        >
          Sign In
        </button>
      </form>
    </div>
</template>