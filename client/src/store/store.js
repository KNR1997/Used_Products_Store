import {defineStore} from 'pinia'

export const authStore = defineStore('authStore', {
    state: () => ({
        user: (localStorage.getItem('token') ? JSON.parse(localStorage.getItem('token')) : null)
    }),
    actions: {
        getUser() {
            return this.user;
        },
        setUser(userData) {
            this.user = userData;
            localStorage.setItem('token', JSON.stringify(userData));
        }
    }
})