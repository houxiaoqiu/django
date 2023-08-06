<script setup lang="ts">
import { isCollapse } from './isCollapse'

</script>

<template>
    <el-header>
        <el-icon @click="isCollapse = !isCollapse">
            <i-ep-Expand v-show="isCollapse" />
            <i-ep-Fold v-show="!isCollapse" />
        </el-icon>
        <!-- 面包屑 -->
        <el-breadcrumb separator="/">
            <el-breadcrumb-item :to="{ path: '/' }">homepage</el-breadcrumb-item>
            <el-breadcrumb-item
            ><a href="/">promotion management</a></el-breadcrumb-item
            >
            <el-breadcrumb-item>promotion list</el-breadcrumb-item>
            <el-breadcrumb-item>promotion detail</el-breadcrumb-item>
        </el-breadcrumb>
        <!-- 下拉菜单 -->
        <el-dropdown >
            <span class="el-dropdown-link">
                <el-avatar :size="32" :src="'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png'" />
            <el-icon class="el-icon--right">
                <arrow-down />
            </el-icon>
            </span>
            <template #dropdown>
            <el-dropdown-menu>
                <el-dropdown-item>用户</el-dropdown-item>
                <el-dropdown-item ><a href="/login">登录</a></el-dropdown-item>
                <el-dropdown-item divided >退出</el-dropdown-item>
            </el-dropdown-menu>
            </template>
        </el-dropdown>
    </el-header>
</template>

<style lang="scss" scoped>
.el-header {
    display: flex;
    align-items: center;
    background-color: #dedfe0;
    .el-icon {
        margin-right: 15px;
    }
}
.el-dropdown {
    margin-left: auto;
    .el-dropdown-link {
        display: flex;
        justify-content: center;
        align-items: center;
    }
}
</style>
