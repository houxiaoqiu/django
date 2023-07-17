import { createRouter, createWebHistory } from "vue-router";

const routes = [
    {
        path: "/",
        name: "Home",
        component: () =>
            import(/* webpackChunkName: "home" */ "../views/Home.vue")
    },
    {
        path: "/login",
        name: "Login",
        component: () =>
            import(/* webpackChunkName: "login" */ "../views/Login.vue")
    },
    {
        path: "/register",
        name: "Register",
        component: () =>
            import(/* webpackChunkName: "register" */ "../views/Register.vue")
    },
    {
        path: "/publish",
        name: "Publish",
        component: () =>
            import(/* webpackChunkName: "publish" */ "../views/Publish.vue")
    },
    {
        path: "/userprofile",
        name: "UserProfile",
        component: () =>
            import(/* webpackChunkName: "userprofile" */ "../views/UserProfile.vue")
    },
    {
        path: "/user",
        name: "User",
        component: () =>
            import(/* webpackChunkName: "user" */ "../views/User.vue"),
        children: [
            {
                path: "userprofile",
                name: "UserProfile",
                component: () =>
                    import(/* webpackChunkName: "userprofile" */ "../views/UserProfile.vue")
            },
        ],
    },

];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

//导航守卫：页面跳转之前执行
router.beforeEach((to, from, next) => {
    next();
});

//后置守卫：
router.afterEach((to, from, failure) => {
    if(!failure) sendToAnalytics(to.fullPath)
})

export default router;