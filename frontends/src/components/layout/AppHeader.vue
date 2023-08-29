<script setup lang="ts">
import { isCollapse } from './isCollapse'
import { getUserProfile } from '@/api/user/users'

const userProfile = ref({ name: "", avatar: "" })

getUserProfile().then((res) => {
    // userProfile.value = res.data
    console.log("getUserProfile", res.data.data)
})

const router = useRouter();

const handleDropDownCommand = (command: string | number | object, row: any) => {
    console.log("command的命令是：", command)
    console.log("userProfile ：", userProfile)
    console.log("==========================================")
    switch (command) {
        case "userProfile":
            router.push("/user");
            break;
        case "login":
            router.push("/login");
            break;
        case 'chargePassword':
            // 修改密码
            ElMessage('点击修改密码');
            break;
        case 'logout':
            // 退出系统
            // token为登录时保存的信息
            // 先获取保存的用户信息
            // localStorage.getItem("msm-user");
            // localStorage.getItem("msm-token");
            // logout(localStorage.getItem('msm-token')).then(response => {
            // 接收返回的数据
            const res = window.localStorage.getItem('TokenInfo');
            if (res) {
                // 退出成功
                // 清除本地用户数据
                localStorage.removeItem("TokenInfo");
                // 回到登录页面
                router.push("/login");
            } else {
                ElMessage({
                    message: res,
                    type: "warning",
                    duration: 2000  // 弹出停留时间
                });
            }
            // });
            break;
        default:
            break;
    }
};

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
            <el-breadcrumb-item><a href="/">promotion management</a></el-breadcrumb-item>
            <el-breadcrumb-item>promotion list</el-breadcrumb-item>
            <el-breadcrumb-item>promotion detail</el-breadcrumb-item>
        </el-breadcrumb>
        <!-- 下拉菜单 -->
        <el-dropdown @command="handleDropDownCommand">
            <span class="el-dropdown-link">
                <!-- <el-avatar :size="32" :src="'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png'" /> -->
                <el-avatar :size="32" :src="userProfile.avatar" />
                <el-icon class="el-icon--right">
                    <arrow-down />
                </el-icon>
            </span>
            <template #dropdown>
                <el-dropdown-menu>
                    <el-dropdown-item command="userProfile">{{ userProfile.username }}</el-dropdown-item>
                    <!-- <el-dropdown-item ><a href="/login">登录</a></el-dropdown-item> -->
                    <el-dropdown-item command="login">登录</el-dropdown-item>
                    <el-dropdown-item command="logout" divided>退出</el-dropdown-item>
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
@/api/xiaoluxian/users@/api/user/users