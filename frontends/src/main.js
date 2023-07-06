// 按需导入 createApp 函数
import { createApp } from 'vue'
// 导入待渲染的 App.vue 组件
import App from './App.vue'

// 调用 createApp 函数，创建 SPA 应用实例，
// 调用 mount() 把 App 组件的模板结构、渲染到指定的el区域中
createApp(App).mount('#app')
