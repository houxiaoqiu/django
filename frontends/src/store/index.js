import { defineStore, createPinia } from 'pinia'
import piniaPluginPersist from 'pinia-plugin-persist'
// import { createStore } from 'vuex'

const store = createPinia()
store.use(piniaPluginPersist)

export default store

export const useMainStore = defineStore('main', {
    state: () => {
        return {
            count: 100,
            foo: "bar",
            arr: [1,2,3],
        }
    },
    
    getters: {
        count10 (state) {
            console.log('count10 被调用了')
            return state.count +10
        }
    },
    
    actions: {
        changeState (num) {
            // this.$patch( state =>{
            //     this.count += num
            //     this.foo = 'hello'
            //     this.arr.push(4)
            // }) 
            this.count += num
            this.foo = 'hello'
            this.arr.push(num)           
        }
    },

})

const createStore = {
    state: {
        token: localStorage.getItem("token") || "",
        routers: localStorage.getItem("tourters") || "",
        menus: localStorage.getItem("menus") || "",
        permissions: localStorage.getItem("permissions") || "",
    },
    getters: {
        routers(state) {
            if (state.routers) {
                return JSON.parse(state.routers);
            }
        },
        menus(state) {
            if (state.menus) {
                return JSON.parse(state.menus);
            }
        },
        permissions(state) {
            if (state.permissions) {
                return JSON.parse(state.permissions);
            }
        }
    },
    mutations: {
        login(state, {routers, menus, permissions, token}) {
            state.token = token;
            localStorage.setItem('token', token);

            state.routers = Json.stringify(routers);
            localStorage.setItem('routers', state.routers);

            state.role = role;
            localStorage.setItem('role', role);
        }
    },
    actions: {

    },
    modules: {

    },
}

