<script setup lang="ts">
import { isCollapse } from '../../components/layout/isCollapse'

</script>

<template>
    <div class="common-layout">
        <el-container>
            <el-aside :width="isCollapse ? '60px' : '200px'">   
                <AppAside />
            </el-aside>
            <el-container class="header-and-main">
                <AppHeader />
                <el-main>
                    <el-scrollbar>
                        <router-view></router-view>
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
    background-color: #e9e9eb;
    height: 100vh;
}
</style>

