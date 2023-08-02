import { defineStore, createPinia } from 'pinia'
import piniaPluginPersist from 'pinia-plugin-persist'

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

