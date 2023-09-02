<template>
    <h1>{{ msg }}</h1>
    <p>
        <a ref="https://vitejs.dev/guide/features.html" target="_blank">Vite Documentation</a>
        |
        <a ref="https://v3.vuejs.org/" target="_blank">Vue 3 Documentation</a>
    </p>
    <button type="button" @click="state.count++">couont is: {{ state.count }}</button>
    <p>
        Edit <code>components/Menu.vue</code> to test hot module replacement.
    </p>
    <div >
        <ul>
            <li><a><router-link to="/">首页</router-link></a></li>
            <li><a><router-link to="/">商品</router-link></a></li>
            <!-- <li><a href="" @click.prevent="goto('/publish')">Publish</a></li>
            <li><a><router-link to="/register">注册/登录</router-link></a></li> -->
        </ul>
    </div>
</template>

<script setup lang="ts">
// import { defineProps, reactive } from 'vue'
import {  reactive } from 'vue'

defineProps({
    msg: String
})

const state = reactive({ count: 0 })

</script>

<style scoped>
    div {
        border: 1px solid red;
    }
    ul {
        list-style: none;
    }
</style>