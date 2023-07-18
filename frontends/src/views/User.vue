<template>
    <p>用户中心公共代码[页面头部]</p>
    <p>{{ user }}</p>
    <p>{{ msg }}</p>
    <router-view></router-view>
</template>

<script setup>
    let data = {name: "张三", age: 18,};
    let user = reactive(data);     //响应式数据，保持全局一致性
    let message = "Hello";
    let msg = ref(message);
</script>