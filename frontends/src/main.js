import { createApp } from 'vue'
import App from './App.vue'

import router from "./router/index"
import store from './store'
// 全局引用
import ElementPlus from 'element-plus'
// 引用所有样式
import 'element-plus/dist/index.css'
import './assets/css/index.scss'
// 引入中文语言
import zhCn from 'element-plus/es/locale/lang/zh-cn'
// 
import * as ElementPlusIconsVue from '@element-plus/icons-vue'


const app = createApp(App)

// 全局注册el-icon
for (const [name, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(name, component);
}

app.use(router).use(store).use(ElementPlus).mount('#app');

// 调用 createApp 函数，创建 SPA 应用实例，
// 调用 mount() 把 App 组件的模板结构、渲染到指定的el区域中
//createApp(App).use(router).use(store).use(ElementPlus).mount('#app');
