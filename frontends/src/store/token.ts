import { defineStore } from 'pinia'

interface Token {
    refresh: string
    access: string
    success: boolean
    massage: string
    id: number
    username: string
}

export const useTokenStore = defineStore('usertoken', () => {
    // ref 相当于 state
    const tokenJson = ref("")
    // computed 相当于 getters
    const token = computed(() => {
        try {
            return (tokenJson.value || window.localStorage.getItem("TokenInfo") || "")
        } catch (err) {
            ElMessage.error("json字符串格式有误,对象转换失败...")
            window.localStorage.setItem("TokenInfo","")
            throw err
        }
    })
    // function 相当于 actions
    function saveToken (data: string) {
        tokenJson.value = data
        window.localStorage.setItem("TokenInfo", data)  // 本地存储
    }
    // 向外暴露
    return { token, saveToken }
})