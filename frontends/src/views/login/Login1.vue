<script setup lang="ts">
import { login } from "@/utils/api/users"
import { ElMessage, FormRules, FormInstance } from "element-plus";
import { reactive, ref } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";

const store = useStore();
const router = useRouter();

const state = reactive({
    username: "13464730744",
    password: "HyperNewBee363",
    role: "user",
    roleList: [
        {text: "管理员", value: "admin"},
        {text: "经理", value: "manager"},
        {text: "普通用户", value: "user"},
    ]
})

const onSubmit = async () => {
    await loginRef.value?.validate().catch((err) => {
        ElMessage.error('表单验证失败')
        throw err       // return new Promise(() => {})
    })
    //正式登录请求
    //const res = login(form)
    const data = login(state).then((res) => {
        if (!res.data.success) {
            ElMessage.error('登录信息有误')
            throw new Error("登录失败")
        }
        return res.data
    })

    console.log(data)   //后续存储处理
}

// 伪代码
function doLogin() {
    const context = {
        token:"https://vben.vvbin.cn/assets/header-1b5fa5f8.jpg",
        role: state.role,

    };
    store.commit("login", context);
    router.replace({ name: "/admin" })
}

//验证规则
const rules = reactive<FormRules>({
    username: [
        {
            require: true,
            message: "电话号码不能为空",
            trigger: "blur",
        },
        {
            pattern: /^1\d{10}$/,
            message: "手机号码必须是11位数字",
            trigger: "blur",
        },
    ],
    password: [
        {
            require: true,
            message: "密码不能为空",
            trigger: "blur",
        },
        {
            min: 6,
            max: 18,
            message: "要求密码长度6~18位字符",
            trigger: "blur",
        },
    ],
})

const loginRef = ref<FormInstance>()

</script>

<template>
    <div class="login">
        <el-form 
            :model="state" 
            :rules="rules" 
            ref="loginRef" 
            label-width="120px" 
            label-position="top" 
            size="large"
        >
            <h1>登录</h1>
            <el-form-item label="帐号" prop="username">
                <el-input v-model="state.username" />
            </el-form-item>
            <el-form-item label="密码" prop="password">
                <el-input type="password" v-model="state.password" />
            </el-form-item>
            <el-form-item label="角色" prop="role">
                <el-input type="text" v-model="state.role" />
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="onSubmit">登录</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<style lang="scss" scoped>
.login {
    background-color: #e9e9eb;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.el-form {
    width: 300px;
    background-color: #fff;
    padding: 30px;
    border-radius: 10px;
}

.el-form-item {
    margin-top: 20px;
}

.el-button {
    width: 100%;
    margin-top: 30px;
}
</style>

