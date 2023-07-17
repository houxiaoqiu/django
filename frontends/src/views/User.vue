<template>

    <p>用户中心公共代码[页面头部]</p>
    <p>{{ user.name }}</p>
    <p>{{ user.age }}</p>
    <router-view></router-view>

</template>

<script>
import { ref, reactive } from 'vue';

export default {
    name: "User",
    setup(){
        let data = {name: "张三", age: 18,};
        let user = reactive(data);     //响应式数据，保持全局一致性
        return {
            user,       // user: user,
        }
    }
}
</script>