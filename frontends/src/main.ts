import { createApp } from 'vue'
import App from '@/App.vue'
import router from '@/router/index'  //引入路由
import ElementPlus from 'element-plus'; // 插件样式
import 'element-plus/dist/index.css';   // 插件样式
import "./assets/css/reset200802.css";  // 引用模板样式
import './assets/css/index.scss';       // 引用模板样式
import 'element-plus/theme-chalk/dark/css-vars.css'; //暗黑模式需要的样式
// //svg插件需要配置代码
// import 'virtual:svg-icons-register';
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
// //引入自定义插件对象:注册整个项目全局组件
// import gloalComponent from '@/components'
// 配置element-plus国际化
import zhCn from 'element-plus/es/locale/lang/zh-cn'
//引入仓库(大仓库)
import pinia from '@/store'

// 根实例对象
const app = createApp(App)

// 全局注册el-icon
for (const [name, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(name, component);
};
//安装element-plus插件
app.use(ElementPlus, {
    locale: zhCn, //element-plus国际化配置
});
//安装仓库
app.use(pinia);
//注册模板路由
app.use(router);

//引入路由鉴权文件
// import './permisstion'
//引入自定义指令文件
import { isHasButton } from '@/directive/has'
isHasButton(app);

//将应用挂载到挂载点上
app.mount('#app');

