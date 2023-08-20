<template>
    <h1>注册</h1>
    <table class="table table-bordered">
      <thead>
        <tr>
          <th>出版社</th>
          <th>邮箱</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in register_list" :key="item.url">
          <td>{{ item.name }}</td>
          <td>{{ item.email }}</td>
        </tr>
      </tbody>
    </table>
</template>

<script>
import axios from 'axios';
import {reactive, onMounted, toRefs} from 'vue'

// import httptool from '../http'
export default {
    name: 'Register',
    setup(){
      let base_url = "http://127.0.0.1:8000/api/publish/";
      
      const register_blank = {url:'', name: '', email: ''};

      const state = reactive({
        register_list: [],
        register: Object.assign({}, register_blank)
      });

      const getRegister = ()=>{
        axios.get(base_url).then(res=>{
          state.register_list = res.data;
          state.register = Object.assign({}, register_blank)
        }).catch(err=>{
          console.log(err);
        })
      };

      const editRegister = (item)=>{
        state.register.url = item.url;
        state.register.name = item.name;
        state.register.email = item.email;
      };

      onMounted(()=>{
        getRegister();
      });

      return{
        ...toRefs(state),
        editRegister,

      };
    }

}
</script>