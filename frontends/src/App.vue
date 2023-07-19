<template>
  <router-view />
</template>

<script setup lang="ts">
import "./assets/css/reset200802.css";
import service from "./utils/api/request"

//接口测试
service({
  method: "GET",
  url: "/front/ad/getAdList",   //http://39.97.218.60/front/ad/getAdList
}).then((res) => {
  console.log(res)
})
</script>