<script>
import axios from 'axios';

export default {
  name: 'Register',
  
  data() {
    return {
      username: '',
      email: '',
      password: ''
    }
  },

  methods: {
    async handleSubmit(){
      const response = await axios.post('api/register/', {
        username: this.username,
        email: this.email,
        password: this.password
      });

      if(response.status === 200 || 201){
        this.$router.push('/auth');

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

        <div class="mb-4">
          <label for="email" class="block text-gray-700 text-sm font-bold mb-2">Email</label>
          <input
            type="email"
            id="email"
            name="email"
            v-model="email"
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
          class="w-full bg-red-600 text-white font-bold py-2 px-4 rounded-md hover:bg-red-700 focus:outline-none focus:shadow-outline-indigo active:bg-indigo-800"
        >
          Register
        </button>
      </form>
    </div>
</template>