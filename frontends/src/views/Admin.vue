<script setup lang="ts">
import { isCollapse } from '../components/layout/isCollapse'
//import { RouterView } from 'vue-router'
</script>

<template>
    <div class="common-layout">
        <el-container>
            <el-aside :width="isCollapse ? '64px' : '200px'">
                <AppAside />
            </el-aside>
            <el-container class="header-and-main">
                <AppHeader />
                <el-main>
                    <el-scrollbar>
                        <router-view></router-view>
                        <!-- <RouterView /> -->
                    </el-scrollbar>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>
  

<style lang="scss" scoped>
.header-and-main {
    flex-direction: column;
    height: 100vh;
}
.el-main {
    background-color: #f4f4f5;
    padding-right: 0;
}
.el-aside {
    height: 100vh;
}
</style>

