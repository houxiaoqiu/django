import { defineStore, createPinia } from 'pinia'
import piniaPluginPersist from 'pinia-plugin-persist'
import { reqLogin, reqLogout, reqUserProfile } from '@/api/user/users'   // 引入API接口
import { loginFormData, loginResult, userProfile } from '@/api/user/type'    // 引入API接口数据类型
import { GET_TOKEN, REMOVE_TOKEN, SET_TOKEN } from '@/utils/token' // 引入本地存储的工具方法


// const store = createPinia()
// store.use(piniaPluginPersist)

// 创建用户仓库
export const useUserStore = defineStore('User', {
    // 数据存储仓库
    state: () => {
        return {
            token: GET_TOKEN(),
            username: '',
            avatar: '',
        }
    },
    
    getters: {},
    
    // 异步/逻辑
    actions: {
        // 用户登录
        async userLogin(data: loginFormData) {
            //登录请求
            const result: loginResult = await reqLogin(data)
            //登录请求:成功200->token
            //登录请求:失败201->登录失败错误的信息
            if (result.code == 200) {
                //pinia仓库存储一下token
                //由于pinia|vuex存储数据其实利用js对象
                this.token = result.data
                //本地存储持久化存储一份
                SET_TOKEN(result.data)
                //能保证当前async函数返回一个成功的promise
                return 'ok'
            } else {
                return Promise.reject(new Error(result.data))
            }
        },
        // 用户信息
        async userProfile() {
            //获取用户信息进行存储仓库当中[用户头像、名字]
            const result: userProfile = await reqUserProfile()
            //如果获取用户信息成功，存储一下用户信息
            if (result.code == 200) {
            this.username = result.data.name
            this.avatar = result.data.avatar
            this.buttons = result.data.buttons
            // //计算当前用户需要展示的异步路由
            // const userAsyncRoute = filterAsyncRoute(
            //     cloneDeep(asnycRoute),
            //     result.data.routes,
            // )
            // //菜单需要的数据整理完毕
            // this.menuRoutes = [...constantRoute, ...userAsyncRoute, anyRoute]
            // //目前路由器管理的只有常量路由:用户计算完毕异步路由、任意路由动态追加
            // ;[...userAsyncRoute, anyRoute].forEach((route: any) => {
            //     router.addRoute(route)
            // })
            return 'ok'
            } else {
            return Promise.reject(new Error(result.message))
            }
        },
        // 退出登录
        async userLogout(data: any) {
            //退出登录请求
            const result: any = await reqLogout()
                if (result.code == 200) {
                    //目前没有mock接口:退出登录接口(通知服务器本地用户唯一标识失效)
                    this.token = ''
                    this.username = ''
                    this.avatar = ''
                    REMOVE_TOKEN()
                    return 'ok'
                } else {
                    return Promise.reject(new Error(result.message))
                }
        },
    },

});

export default useUserStore


