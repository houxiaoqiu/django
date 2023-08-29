import { defineStore } from 'pinia'

interface Token {
    refresh: string
    access: string
    success: boolean
    massage: string
    id: number
    username: string
};

const tokenJson = ref("");

// 本地存储：存储数据
export const SET_TOKEN = (token: string) => {
    localStorage.setItem("TokenInfo",token )  // 本地存储
};
// 本地存储：获取数据
export const GET_TOKEN = () => {
    try {
            return (tokenJson.value || localStorage.getItem("TokenInfo") || "")
    } catch (err) {
        ElMessage.error("json字符串格式有误,对象转换失败...")
        localStorage.setItem("TokenInfo","")
        throw err
    }
};
// 本地存储：删除数据
export const REMOVE_TOKEN = () => {
    localStorage.removeItem("TokenInfo")  
};

export const useTokenStore = defineStore('usertoken', () => {
    // ref 相当于 state
    // const tokenJson = ref("")
    // 本地存储：获取数据 computed 相当于 getters
    const token = computed(() => {
        try {
            return (tokenJson.value || window.localStorage.getItem("TokenInfo") || "")
        } catch (err) {
            ElMessage.error("json字符串格式有误,对象转换失败...")
            window.localStorage.setItem("TokenInfo","")
            throw err
        }
    });
    // 存储数据 function 相当于 actions
    function saveToken (data: string) {
        tokenJson.value = data
        window.localStorage.setItem("TokenInfo", data)  // 本地存储
    };

    // 向外暴露
    return { token, saveToken, GET_TOKEN, SET_TOKEN, REMOVE_TOKEN }
});