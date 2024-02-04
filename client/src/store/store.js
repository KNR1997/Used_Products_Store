import {defineStore} from 'pinia'

export const authStore = defineStore('authStore', {
    state: () => ({
        user: (localStorage.getItem('token') ? JSON.parse(localStorage.getItem('token')) : null),
        username: null
    }),
    actions: {
        getUser() {
            return this.username;
        },
        setUser(userData) {
            // this.user = userData;
            this.username = 'kethaka'
            localStorage.setItem('token', JSON.stringify(userData));
        }
    }
})