<template>
  <h1>this is an about page</h1>
  <hr/>
  <p>mainStore.count: {{ mainStore.count }}</p>
  <p>mainStore.foo: {{ mainStore.foo }}</p>
  <hr/>
  <p> count: {{  count }}</p>
  <p> foo: {{  foo }}</p>
  <p> foo: {{  mainStore.arr }}</p>
  <hr/>
  <p>
    <button @click="handleChangeState">修改数据</button>
  </p>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia'
import { useMainStore } from '@/store'

const mainStore = useMainStore()

const { count, foo } = storeToRefs(mainStore)

console.log(mainStore.count)

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
  
  mainStore.changeState(10)

}

</script>

<style>

</style>