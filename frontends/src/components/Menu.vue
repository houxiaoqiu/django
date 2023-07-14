<template>
    <div >
        <p>home_total={{ home_total }}</p>
        <p>要发送给父组件的数据：num={{ num }}</p>
        <button @click="add">{{ num }}</button>
        <ul>
            <li><a href="">首页</a></li>
            <li><a href="">商品</a></li>
            <li><a href="">服务</a></li>
            <li><a href="">注册/登录</a></li>
        </ul>
    </div>
</template>

<script>
export default {
    name: "Menu",
    props: {
        home_total: {
            type: Number,
            default: 99
        }
    },
    data() {
        return {
            num: 100,
            message: "Hello,我来自Menu组件。"
        }
    },
    methods: {
        add() {
            this.num++;
            this.$emit("add_num",this.num,this.message);
        }
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