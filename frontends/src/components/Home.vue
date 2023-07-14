<template>
    <div>
        <button @click="num--">-</button>
        <input type="text" v-model="num" />
        <button @click="num++">+</button>
    </div>
</template>

<script>
    const Home = {
        name: "Home",
        data() {
            return {
                num: 10
            }
        }
    }
    export default Home;
</script>

<style scoped>
    button {
        color: red;
    }
    input {
        text-align: center;
    }
</style>