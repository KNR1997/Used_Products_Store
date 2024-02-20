import {defineStore} from 'pinia'
import { jwtDecode } from "jwt-decode";
import { toRefs } from 'vue';

export const authStore = defineStore('authStore', {
    state: () => ({
        user: (localStorage.getItem('user') ? JSON.parse(localStorage.getItem('user')) : null),
    }),
    actions: {
        getUser() {
            return this.user;
        },
        setUser(userData) {
            this.user = jwtDecode(userData.access);
            localStorage.setItem('token', JSON.stringify(userData));
            localStorage.setItem('user', JSON.stringify(jwtDecode(userData.access)));
        },
        logoutUser() {
            this.user = null;
            localStorage.removeItem('token');
            localStorage.removeItem('user');
        }
    }
})

export const cartStore = defineStore('cartStore', {
    state: () => ({
        // items: (localStorage.getItem('items') ? JSON.parse(localStorage.getItem('items')) : null),
        items: []
    }),
    actions: {
        getItems() {
            const { items } = toRefs(this);
            return items.value;
        },
        addItem(item) {
            this.items.push(item);
        },
        clearCart() {
            this.items = []
        }
    }
})

export const appStates = defineStore('appStates', {
    state: () => ({
        // items: (localStorage.getItem('items') ? JSON.parse(localStorage.getItem('items')) : null),
        sellerView: false
    }),
    actions: {
        openSellerView() {
            this.sellerView = true;
        },
        closeSellerView() {
            this.sellerView = false
        },
        getSellerView() {
            return this.sellerView
        }
    }
})