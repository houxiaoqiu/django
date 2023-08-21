<template>
    <div>
        <h2>商品列表</h2>
        <br/>
        <ul>
            <li v-for="item in productsStore.all">
                {{ item.title }} - {{ item.price }} - {{ item.inventory }} 
                <button 
                    :disabled="!item.inventory" 
                    @click="cartStore.addProductToCart(item)"
                    >添加到购物车
                </button>
                <br />
            </li>
        </ul>
    </div>
</template>

<script setup lang="ts">
import { useProductsStore } from '@/store/shopping'
import { useCartStore } from '@/store/cart'

const productsStore = useProductsStore()
const cartStore = useCartStore()

// 加载所有数据
productsStore.loadAllProducts()

</script>