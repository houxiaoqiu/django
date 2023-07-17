<template>
    <div >
        <ul>
            <li><a><router-link to="/">首页</router-link></a></li>
            <li><a><router-link to="/">商品</router-link></a></li>
            <li><a href="" @click.prevent="goto('/publish')">Publish</a></li>
            <li><a><router-link to="/register">注册/登录</router-link></a></li>
        </ul>
    </div>
</template>

<script>
export default {
    name: "Menu",
    methods: {
        goto(url){
            this.$router.push(url);
            // this.$router.back();
            // this.$router.go(1);
            // this.$router.forward();
        },
    }
}    
</script>

<style scoped>
    div {
        border: 1px solid red;
    }
    ul {
        list-style: none;
    }
</style>