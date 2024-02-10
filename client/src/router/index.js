import { createRouter, createWebHistory} from 'vue-router'
import Home from '../views/Home.vue'
import Product from '../views/Product.vue'
import Auth from '../views/Auth.vue'
import Shoppingcart from '../views/Shoppingcart.vue'
import Address from '../views/Address.vue'
import Checkout from '../views/Checkout.vue'
import Orders from '../views/Orders.vue'

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
    },
    {
        path: '/checkout',
        name: 'checkout',
        component: Checkout
    },
    {
        path: '/orders',
        name: 'orders',
        component: Orders
    }
];

const router = createRouter({
    // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
    history: createWebHistory(),
    routes, // short for `routes: routes`
})

export default router;