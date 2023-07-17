import { createRouter, createWebHistory } from "vue-router";

import Home from "../views/Home.vue";
import Resister from "../views/Register.vue";
import Publish from "../views/Publish.vue";
import User from "../views/User.vue";
import UserProfile from "../views/UserProfile.vue";
import Login from "../views/Login.vue";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: "/",
            component: Home,
        },
        {
            path: "/login",
            component: Login,
        },
        {
            path: "/register",
            component: Resister,
        },
        {
            path: "/publish",
            component: Publish,
        },
        {
            path: "/userprofile",
            component: UserProfile,
        },
        {
            path: "/user",
            component: User,
            children: [
                {
                    path: "/userprofile",
                    component: UserProfile,
                },
            ],
        },
    ]
});

//导航守卫：页面跳转之前执行
router.beforeEach((to, from, next) => {
    //return to();      //下一个页面的路由对象
    //return from();    //当前页面的路由对象
    //return next();    // 允许跳转
    //return next(false);   // 拒绝跳转
    // if(to.path !== "/" && to.path !== "/login"){
    //     if(to.query.user == "xiaoming"){
            next();
    //     }else {
    //         next({ path: "/login"} );
    //     }
    // }
    
});

//后置守卫：
router.afterEach((to, from, failure) => {
    if(!failure) sendToAnalytics(to.fullPath)
})

//独享守卫
const routes = [
    {
        path: '/users/:id',
        component: UserProfile,
        beforeEnter: (to, from) => {
            return false;
        },
    },
]

export default router;

// // 1. 定义路由组件.
// // 也可以从其他文件导入
// const Home = { template: '<div>Home</div>' }
// const About = { template: '<div>About</div>' }

// // 2. 定义一些路由
// // 每个路由都需要映射到一个组件。
// // 我们后面再讨论嵌套路由。
// const routes = [
//   { path: '/', component: Home },
//   { path: '/about', component: About },
// ]

// // 3. 创建路由实例并传递 `routes` 配置
// // 你可以在这里输入更多的配置，但我们在这里
// // 暂时保持简单
// const router = VueRouter.createRouter({
//   // 4. 内部提供了 history 模式的实现。为了简单起见，我们在这里使用 hash 模式。
//   history: VueRouter.createWebHashHistory(),
//   routes, // `routes: routes` 的缩写
// })

// // 5. 创建并挂载根实例
// const app = Vue.createApp({})
// //确保 _use_ 路由实例使
// //整个应用支持路由。
// app.use(router)

// app.mount('#app')

// // 现在，应用已经启动了！