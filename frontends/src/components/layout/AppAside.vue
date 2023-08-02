<template>
  <el-scrollbar>
    <el-menu unique-opened router :collapse="isCollapse">
      <a href="/" class="logo">
        <img src="@/assets/img/vite.svg" alt="">
        <h1>Admin</h1>
      </a>
      <el-sub-menu index="1">
        <template #title>
          <el-icon><i-ep-location /></el-icon>
          <span>系统管理</span>
        </template>
        <el-menu-item-group>
          <template #title><span>Group One</span></template>
          <el-menu-item index="/shoppinglist">商品列表</el-menu-item>
          <el-menu-item index="/shoppingcart">购物车</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="Group Two">
          <el-menu-item index="/shopping">购物车示例</el-menu-item>
        </el-menu-item-group>
        <el-sub-menu index="1-4">
          <template #title><span>item four</span></template>
          <el-menu-item index="1-4-1">item one</el-menu-item>
        </el-sub-menu>
      </el-sub-menu>
      <el-menu-item index="2">
        <el-icon><i-ep-menu /></el-icon>
        <template #title>菜单列表</template>
      </el-menu-item>
      <el-menu-item index="3" disabled>
        <el-icon>
          <document />
        </el-icon>
        <template #title>功能管理</template>
      </el-menu-item>
      <el-menu-item index="/about">
        <el-icon><i-ep-setting /></el-icon>
        <template #title>关于</template>
      </el-menu-item>
    </el-menu>
  </el-scrollbar>
</template>
  
<script lang="ts" setup>
import { isCollapse } from './isCollapse'

  // const handleOpen = (key: string, keyPath: string[]) => {
  //   console.log(key, keyPath)
  // }
  // const handleClose = (key: string, keyPath: string[]) => {
  //   console.log(key, keyPath)
  // }
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
  