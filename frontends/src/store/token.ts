import { defineStore, createPinia } from 'pinia'

interface Token {
    access_token: string
    token_type: string
    refresh_token: string
    expires_in: number
    user_id: string
}

export const useTokenStore = defineStore('token', () => {
    // ref 相当于 state
    const tokenJson = ref("")
    // computed 相当于 getters
    try {
        const token = computed(() => {
            return JSON.parse(tokenJson.value || window.localStorage.getItem("TokenInfo") || "{}")
        })
    } catch (err) {
        ElMessage.error("字符转化json格式失败...")
        window.localStorage.setItem("TokenInfo","")
        throw err
    }
    // function 相当于 actions
    function saveToken (data: string) {
        tokenJson.value = data
        // 本地存储
        window.localStorage.setItem("TokenInfo", data)
    }
    // 向外暴露
    return { token, saveToken }
})