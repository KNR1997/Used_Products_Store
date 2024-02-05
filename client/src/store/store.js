import {defineStore} from 'pinia'
import { jwtDecode } from "jwt-decode";

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
            return this.items;
        },
        addItem(item) {
            console.log('in cartStore, going to push: ', item)
            this.items = [...this.items, item];
            console.log(this.items)
        }
    }
})