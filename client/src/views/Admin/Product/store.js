import {defineStore} from 'pinia'

export const productStore = defineStore('productStore', {
    state: () => ({
        product: {},
        productId: 0 
    }),
    actions: {
        getProductData() {
            return this.product;
        },
        setProductData(product) {
            this.product = product;
        },
        clearProductData() {
            this.product = null;
        }
    }
})