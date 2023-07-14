<template>
    <h1>注册</h1>
    <button @click="send">点击发送请求</button>
</template>

<script>
import httptool from '../http'
export default {
    name: "Register",
    components: {

    },
    methods: {
        send() {
          httptool.get(url: "http://127.0.0.1:8000/publishes/",config: {
            params: {
                ordering: "-id",
                age: 18,
            },
            headers: {"Company": "vue Company"},
          }).then(response=>{
            console.log(responese);
            console.log(response.data);
          }).catch(error=>{
            console.log(error);
            console.log(error.response);
          });  
        }
    }
}
</script>