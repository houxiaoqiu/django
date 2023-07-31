<template>
  <el-scrollbar>
    <el-menu 
      unique-opened 
      :collapse="isCollapse" 
      :router="true" 
      :default-active="activeRouter">
      <a href="/" class="logo">
        <img src="@/assets/img/vite.svg" alt="">
        <h1>Admin</h1>
      </a>
      <el-sub-menu v-for="item in menuList" :index="item.title" :key="item.title">
        <template #title>
          <el-icon>
            <!-- <component :is="item.icon"></component> /> -->
          </el-icon>
          <span>{{ item.title }}</span>
        </template>

        <el-menu-item 
          v-for="ele in item.children" 
          :index="ele.name" 
          :key="ele.id"
          :route="{name:ele.name}">{{ ele.title }}
        </el-menu-item>

      </el-sub-menu>
    </el-menu>
  </el-scrollbar>
</template>
  
<script lang="ts" setup>
import { isCollapse } from './isCollapse'
import store from '@/store';
import { computed } from 'vue';
// import { useStore } from 'vuex';
import { useRoute } from 'vue-router';

const route = useRoute();
// const store = useStore();

const activeRouter = computed( () => route.name);
// const menuList = computed(() => store.getters.nemus);
</script>
  
<style>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
.logo {
  display: flex;
  justify-content: center;
  align-items: center;
  text-decoration: none;
  color: black;
  height: 60px;

  img {
    width: 32px;
    height: 32px;
  }
}

/* 设置菜单样式 */
.el-menu {
  background-color: #e9e9eb;
  border-right: none;
  width: 200px;

  &.el-menu--collapse {
    width: 60px;
    &h1 {
      display: none;
    }
  }
}
</style>
  