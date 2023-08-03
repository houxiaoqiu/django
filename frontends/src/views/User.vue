<template>
    <p>用户中心公共代码[页面头部]</p>
    <RouterView></RouterView>
</template>

<script setup>
import  drfdemo  from '@/utils/api/request';

drfdemo({
  method: "GET",
  // http://localhost:8000/drfdemo/login/
  url: "/drfdemo/users/1/",
}).then((res) => {
  console.log(res)
  console.log(URL)
})
console.log(drfdemo.getUri)
</script>