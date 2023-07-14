<template>
  <div>
    <Home/>
    <Register/>
    <div  class="row">
      <Lyb/>
    </div>
  </div>
</template>

<script>
  import Lyb from './components/Lyb.vue'
  import Register from './views/Register.vue'
  import Home from './views/Home.vue'

  export default {
    name: 'App',
    components: {
      Home,
      Register,
      Lyb,
    },
  }
</script>


