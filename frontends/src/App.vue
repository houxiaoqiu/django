<template>
  <router-view />
</template>

<script setup lang="ts">
import "./assets/css/reset200802.css";
import server from "./utils/api/request"

// 接口测试
// server({
//   method: "GET",
//   url: "publish",
// }).then((res) => {
//   console.log(res)
// })
</script>