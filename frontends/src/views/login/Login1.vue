<script setup lang="ts">
import { login } from "@/utils/api/users"
import { useTokenStore } from "@/store/token"
import { ElMessage, FormRules, FormInstance } from "element-plus";
// import { reactive, ref } from "vue";
// import { useRouter } from "vue-router";

const router = useRouter();
// 调用 token 存储空间
const tokenStore = useTokenStore();

const state = reactive({
    username: "13464730744",
    password: "HyperNewBee363",
    role: "user",
    roleList: [
        {label: "管理员", value: "admin"},
        {label: "经理", value: "manager"},
        {label: "普通用户", value: "user"},
    ],
})

const onSubmit = async () => {
    // isLoading.value = ture
    // 表单验证
    await loginRef.value?.validate().catch((err) => {
        ElMessage.error('表单验证失败')
        throw err       // return new Promise(() => {})
    })
    //正式登录请求
    const data = login(state).then((res) => {
        if (!res.data.success) {
            ElMessage.error('登录信息有误')
            throw new Error("登录失败")
        }
        return res.data
    })

    console.log(data)   //后续存储处理

    // 保存 token
    tokenStore.saveToken(data.token)
    // tokenStore.saveToken(data.content)
    // isLoading.value = false
    ElMessage.success("登录成功")
    router.push("/admin")
}

// 伪代码
function doLogin() {
    const context = {
        token:"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.",
        role: state.role,

    };
    store.commit("login", context);     //保存vuex
    router.replace({ name: "/admin" })  //跳转
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
                <el-select clearable v-model="state.role" placeholder="请选择" >
                    <optin 
                        v-for="(item,index) in state.roleList" 
                        :key="index"
                        :label="item.label"
                        :value="item.value">
                        {{ item.label }}
                    </optin>
                </el-select> 
            </el-form-item>
            <el-form-item>
                <!-- <el-button type="primary" @click="onSubmit" >登录</el-button> -->
                <el-button type="primary" @click="onSubmit" >登录</el-button>
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

