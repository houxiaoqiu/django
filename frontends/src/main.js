import { createApp } from 'vue';
import App from './App.vue';

import router from "./router/index";

// 调用 createApp 函数，创建 SPA 应用实例，
// 调用 mount() 把 App 组件的模板结构、渲染到指定的el区域中
createApp(App).use(router).mount('#app');
