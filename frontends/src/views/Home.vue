<template>
    <h1>Home  {{ num }}</h1>
    <button @click="total++">{{ total }}</button>
    <Menu :home_total="total" @add_num="get_data"></Menu>
</template>

<script>
import Menu from '../components/Menu.vue'
export default {
    name: "Home",
    data() {
        return {
            total: 10,
        }
    },
    components: {
        Menu,
    },
    methods: {
        get_data(num,message) {
            console.log(num,message);
        }
    }
}
</script>

<style  scoped>
    ul {
        list-style: none;
    }
</style>