<template>
  <h1>this is an about page</h1>
  <hr />
  <p>mainStore.count: {{ mainStore.count }}</p>
  <p>mainStore.foo: {{ mainStore.foo }}</p>
  <hr />
  <p> count: {{ count }}</p>
  <p> foo: {{ foo }}</p>
  <p> foo: {{ mainStore.arr }}</p>
  <hr />
  <p>
    <button @click="handleChangeState">修改数据</button>
  </p>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia'
import { useUserStore } from '@/store/user/index'
import drfdemo from '@/utils/request';

drfdemo({
  method: "GET",
  // http://localhost:8000/drfdemo/login/
  url: "/drfdemo/users/1/",
}).then((res) => {
  console.log(res.status)
})

const userStore = useUserStore()

const { username, avatar } = storeToRefs(userStore)

console.log(userStore.username)

// const handleChangeState = () => {
//   mainStore.$patch({
//     count: mainStore.count + 1,
//     foo: 'hello',
//   })
// }

// const handleChangeState = () => {
//   mainStore.$patch(state => {
//     mainStore.count++
//     mainStore.foo = 'hello'
//     mainStore.arr.push(4)
//   })
//}

const handleChangeState = () => {

  userStore.userProfile

}

</script>

<style></style>