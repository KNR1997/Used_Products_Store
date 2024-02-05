import { createRouter, createWebHistory} from 'vue-router'
import Home from '../views/Home.vue'
import Product from '../views/Product.vue'
import Auth from '../views/Auth.vue'
import Shoppingcart from '../views/Shoppingcart.vue'
import Address from '../views/Address.vue'

const routes = [
    {
        path: '/',
        name: 'home',
        component: Home
    },
    {
        path: '/product/:id',
        name: 'product',
        component: Product
    },
    {
        path: '/auth',
        name: 'auth',
        component: Auth
    },
    {
        path: '/shoppingcart',
        name: 'shoppingcart',
        component: Shoppingcart
    },
    {
        path: '/address',
        name: 'address',
        component: Address
    }
];

const router = createRouter({
    // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
    history: createWebHistory(),
    routes, // short for `routes: routes`
})

export default router;