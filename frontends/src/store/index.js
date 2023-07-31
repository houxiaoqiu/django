import { createPinia } from 'pinia'
import piniaPluginPersist from 'pinia-plugin-persist'
import { createStore } from 'vuex'

const store = createPinia()
store.use(piniaPluginPersist)

export default store

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

        }
    }
}

