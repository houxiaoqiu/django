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
        <el-menu-item index="/publish">
            <el-icon><i-ep-setting /></el-icon>
            <span>系统选项</span>
          </el-menu-item>
        <el-sub-menu index="1-4">
          <template #title>
            <el-icon><i-ep-menu /></el-icon>
            <span>用户权限</span>
          </template>
          <el-menu-item index="/publish">
            <el-icon><document /></el-icon>
            <span>用户</span>
          </el-menu-item>
          <el-menu-item index="/publish">
            <el-icon><document /></el-icon>
            <span>角色</span>
          </el-menu-item>
          <el-menu-item index="/publish">
            <el-icon><document /></el-icon>
            <span>权限</span>
          </el-menu-item>
        </el-sub-menu>
      </el-sub-menu>
      <el-sub-menu index="2">
        <template #title>
          <el-icon><i-ep-menu /></el-icon>
          <span>往来机构人员</span>
        </template>
        <el-menu-item index="/publish">
            <el-icon><i-ep-setting /></el-icon>
            <span>往来机构人员选项</span>
        </el-menu-item>
        <el-menu-item index="/publish">
            <el-icon><i-ep-document /></el-icon>
            <span>机构</span>
        </el-menu-item>
        <el-menu-item index="/publish">
            <el-icon><i-ep-document /></el-icon>
            <span>人员</span>
        </el-menu-item>
      </el-sub-menu>
      <el-sub-menu index="3">
        <template #title>
          <el-icon><i-ep-menu /></el-icon>
          <span>人力资源</span>
        </template>
        <el-menu-item index="/publish">
            <el-icon><i-ep-setting /></el-icon>
            <span>人力资源选项</span>
        </el-menu-item>
        <el-sub-menu index="3-1">
          <template #title>
            <el-icon><i-ep-menu /></el-icon>
            <span>机构人员</span>
          </template>
          <el-menu-item index="/publish">
            <el-icon><i-ep-document /></el-icon>
            <span>机构</span>
        </el-menu-item>
        <el-menu-item index="/publish">
            <el-icon><i-ep-document /></el-icon>
            <span>人员</span>
        </el-menu-item>
        </el-sub-menu>
      </el-sub-menu>
      <el-sub-menu index="4">
        <template #title>
          <el-icon><i-ep-menu /></el-icon>
          <span>财务管理</span>
        </template>
        <el-menu-item index="/publish">
          <el-icon><i-ep-setting /></el-icon>
          <span>财务选项</span>
        </el-menu-item>
        <el-menu-item index="/publish">
          <el-icon><i-ep-document /></el-icon>
          <span>会计科目</span>
        </el-menu-item>
        <el-menu-item index="/publish">
          <el-icon><i-ep-document /></el-icon>
          <span>会计凭证</span>
        </el-menu-item>
        <el-menu-item index="/publish">
          <el-icon><i-ep-document /></el-icon>
          <span>会计核算</span>
        </el-menu-item>
        <el-menu-item index="/publish">
          <el-icon><i-ep-document /></el-icon>
          <span>财务报表</span>
        </el-menu-item>
      </el-sub-menu>
      <el-sub-menu index="5">
        <template #title>
          <el-icon><i-ep-menu /></el-icon>
          <span>仓储管理</span>
        </template>
        <el-menu-item index="/wmsOption">
          <el-icon><i-ep-setting /></el-icon>
          <span>仓储选项</span>
        </el-menu-item>
        <el-sub-menu index="5-1">
          <template #title>
            <el-icon><i-ep-menu /></el-icon>
            <span>物资</span>
          </template>
          <el-menu-item index="/shopping">
          <el-icon><i-ep-document /></el-icon>
          <span>计量单位</span>
          </el-menu-item>
          <el-menu-item index="/shopping">
          <el-icon><i-ep-document /></el-icon>
          <span>物料</span>
          </el-menu-item>
          <el-menu-item index="/shopping">
          <el-icon><i-ep-document /></el-icon>
          <span>物料清单</span>
          </el-menu-item>
        </el-sub-menu>
        <el-menu-item index="/shopping">
          <el-icon><i-ep-document /></el-icon>
          <span>仓库</span>
        </el-menu-item>
        <el-menu-item index="/shopping">
          <el-icon><i-ep-document /></el-icon>
          <span>仓储业务</span>
        </el-menu-item>
      </el-sub-menu>
      <el-sub-menu index="6">
        <template #title>
          <el-icon><i-ep-menu /></el-icon>
          <span>销售管理</span>
        </template>
        <el-menu-item index="/shoppinglist">
          <el-icon><i-ep-setting /></el-icon>
          <span>销售选项</span>
        </el-menu-item>
        <el-menu-item index="/shoppingcart">
          <el-icon><i-ep-document /></el-icon>
          <span>销售业务</span>
        </el-menu-item>
      </el-sub-menu>
      <el-sub-menu index="7">
        <template #title>
          <el-icon><i-ep-menu /></el-icon>
          <span>采购管理</span>
        </template>
        <el-menu-item index="/shoppinglist">
          <el-icon><i-ep-setting /></el-icon>
          <span>采购选项</span>
        </el-menu-item>
        <el-menu-item index="/shoppingcart">
          <el-icon><i-ep-document /></el-icon>
          <span>采购业务</span>
        </el-menu-item>
      </el-sub-menu>
      <el-sub-menu index="8">
        <template #title>
          <el-icon><i-ep-menu /></el-icon>
          <span>生产制造</span>
        </template>
        <el-menu-item index="/shoppinglist">
          <el-icon><i-ep-setting /></el-icon>
          <span>制造选项</span>
        </el-menu-item>
        <el-menu-item index="/shoppingcart">
          <el-icon><i-ep-document /></el-icon>
          <span>生产计划</span>
        </el-menu-item>
        <el-menu-item index="/shopping">
          <el-icon><i-ep-document /></el-icon>
          <span>生产订单</span>
        </el-menu-item>
        <el-menu-item index="/shopping">
          <el-icon><i-ep-document /></el-icon>
          <span>生产排程</span>
        </el-menu-item>
        <el-menu-item index="/shopping">
          <el-icon><i-ep-document /></el-icon>
          <span>生产报工</span>
        </el-menu-item>
      </el-sub-menu>
      <el-sub-menu index="9">
        <template #title>
          <el-icon><i-ep-menu /></el-icon>
          <span>应用集成</span>
        </template>
        <el-menu-item index="/publish">
          <el-icon><i-ep-document /></el-icon>
          <span>应用注册</span>
        </el-menu-item>
        <el-menu-item index="/publish">
          <el-icon><i-ep-document /></el-icon>
          <span>应用设置</span>
        </el-menu-item>
      </el-sub-menu>
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
  