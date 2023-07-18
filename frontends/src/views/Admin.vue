<script setup lang="ts">
import { isCollapse } from '../components/layout/isCollapse'
</script>

<template>
    <div class="common-layout">
        <el-container>
            <el-aside :width="isCollapse ? '64px' : '200px'">
                <AppAside />
            </el-aside>
            <el-container class="header-and-main">
                <AppHeader />
                <el-main>Main</el-main>
            </el-container>
        </el-container>
    </div>
</template>
  

<style lang="scss" scoped>
.header-and-main {
    flex-direction: column;
}
</style>

