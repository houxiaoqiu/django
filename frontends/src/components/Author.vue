<template>
  <h1>作者</h1>
  <div class="row">
    <div class="col-md-8">
      <table class="table table-bordered">
        <thead>
          <tr>
            <th>姓名</th>
            <th>年龄</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in author_list" :key="item.url">
            <td>{{ item.name }}</td>
            <td>{{ item.age }}</td>
            <td>
              <button class="btn btn-success" title="编辑" @click="editAuthor(item)" style="margin: 0 10px;">
                <i class="glyphicon glyphicon-pencil"></i>
              </button>
              <button class="btn btn-danger" title="删除" @click="deleteAuthor(item)">
                <i class="glyphicon glyphicon-trash"></i>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div> 
    <div class="col-md-4">
      <input type="hidden">
      <div class="form-group">
        <label for="name">姓名：</label>
        <input type="text" id="name" class="form-control" v-model="author.name">
      </div>
      <div class="form-group">
        <label for="age">年龄：</label>
        <input type="text" id="age" class="form-control"  v-model="author.age">
      </div>
      <div class="form-group">
        <button class="btn btn-default" @click="saveAuthor">确定</button>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
  import {reactive, onMounted, toRefs} from 'vue';

  export default {
    name: 'Author',
    setup(){
      let base_url = "http://127.0.0.1:8000/api/author/";
      
      const author_blank = {url:'', name: '', age: ''}

      const state = reactive({
        author_list: [],
        author: Object.assign({}, author_blank)
      });

      const getAuthor = ()=>{
        axios.get(base_url).then(res=>{
          state.author_list = res.data;
          state.author = Object.assign({}, author_blank) 
        }).catch(err=>{
          console.log(err);
        })
      };

      const editAuthor = (item)=>{
        state.author.url = item.url;
        state.author.name = item.name;
        state.author.age = item.age;
      };

      const saveAuthor = ()=>{
        let newdata = {
          name:state.author.name,
          age:state.author.age,
        }
        if(state.author.url==""){
          //新增
          axios.post(base_url,newdata).then(()=>{
            getAuthor();
          }).catch(err=>{
            console.log(err);
          })
        }else{
          //编辑
          axios.put(state.author.url,newdata).then(()=>{
            getAuthor();
          }).catch(err=>{
            console.log(err);
          })
        }
      };

      const deleteAuthor = (item)=>{
        axios.delete(item.url).then(()=>{
            getAuthor();
          }).catch(err=>{
            console.log(err);
          });
      };

      onMounted(()=>{
        getAuthor();
      });

      return{
        ...toRefs(state),
        editAuthor,
        saveAuthor,
        deleteAuthor,
      };
    }
  }

</script>
