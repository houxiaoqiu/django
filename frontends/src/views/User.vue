<template>
    <p>用户中心公共代码[页面头部]</p>
</template>

<script setup>
import  drfdemo  from '@/utils/api/request';


drfdemo({
  method: "GET",
  // http://localhost:8000/drfdemo/login/
  url: "/drfdemo/address/",
}).then((res) => {
  console.log(res)

})
console.log("tttt")
</script>