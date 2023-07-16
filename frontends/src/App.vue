<template>
  <div>
    <Home/>
    <hr/>
    <Register/>
    <hr/>
    <div class="row">
      <Author/>
    </div>
    <hr/>
    <!-- <x/> -->
    <div  class="row">
      <Lyb/>
    </div>
  </div>
</template>

<script>
  import Home from './views/Home.vue'
  import Register from './views/Register.vue'
  import Author from './components/Author.vue'
  import Lyb from './components/Lyb.vue'
  

  export default {
    name: 'App',
    components: {
      Home,
      Register,
      Author,
      Lyb,
    },
  }
</script>


