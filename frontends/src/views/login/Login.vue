<script setup lang="ts">
import { login } from "@/utils/api/users"

const form = reactive({
    phone: "13464730744",
    password: "123",
})

const onSubmit = async () => {
    await loginRef.value?.validate().catch((err) => {
        ElMessage.error('表单验证失败')
        throw err       // return new Promise(() => {})
    })
    //正式登录请求
    //const res = login(form)
    const data = login(form).then((res) => {
        if (!res.data.success) {
            ElMessage.error('登录信息有误')
            throw new Error("登录失败")
        }
        return res.data
    })

    console.log(data)   //后续存储处理
}

//验证规则
const rules = reactive<FormRules>({
    phone: [
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
        <el-form :model="form" :rules="rules" ref="loginRef" label-width="120px" label-position="top" size="large">
            <h1>登录</h1>
            <el-form-item label="手机号" prop="phone">
                <el-input v-model="form.phone" />
            </el-form-item>
            <el-form-item label="密码" prop="password">
                <el-input type="password" v-model="form.password" />
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

