<template>
  <div>
    <Home/>
    <div  class="row">
      <Lyb/>
    </div>
  </div>
</template>

<script>
  import Lyb from './components/Lyb.vue'
  import Home from './components/Home.vue'

  export default {
    name: 'App',
    components: {
      Home,
      Lyb
    }
  }
</script>


