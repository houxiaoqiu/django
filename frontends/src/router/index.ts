import { createRouter, createWebHistory } from "vue-router";
import { useTokenStore } from "@/store/token";

const routes = [
    {
        path: "/login",
        name: "Login",
        component: () =>
            import(/* webpackChunkName: "login" */ "@/views/login/Login.vue")
    },
    {
        path: "/register",
        name: "Register",
        component: () =>
            import(/* webpackChunkName: "register" */ "@/views/Register.vue")
    },
    {
        path: "/",
        name: "Home",
        component: () =>
            import(/* webpackChunkName: "home" */ "@/views/Home.vue"),
        // meta: { requiresAuth: true}     // 要求验证
    },
    {
        path: "/admin",
        name: "Admin",
        component: () =>
            import(/* webpackChunkName: "admin" */ "@/views/Admin.vue"),
        meta: { requiresAuth: true},     // 要求验证
        children: [
            {
                path: "",
                component: () =>
                    import(/* webpackChunkName: "publish" */ "@/views/Publish.vue")
            },
            {
                path: "/shopping",
                name: "Shopping",
                component: () =>
                    import(/* webpackChunkName: "about" */ "@/components/shopping/Shopping.vue"),
            },
            {
                path: "/shoppinglist",
                name: "ShoppingList",
                component: () =>
                    import(/* webpackChunkName: "about" */ "@/components/shopping/ShoppingList.vue"),
            },
            {
                path: "/shoppingcart",
                name: "ShoppingCart",
                component: () =>
                    import(/* webpackChunkName: "about" */ "@/components/shopping/ShoppingCart.vue"),
            },
            {
                path: "/about",
                name: "About",
                component: () =>
                    import(/* webpackChunkName: "about" */ "@/views/About.vue"),
            },
            {
                path: "/:xxx(.*)*",
                name: "Error",
                component: () => 
                    import(/* webpackChunkName: "about" */ "@/components/common/Error.vue"),
            },
        ],
    },
    {
        path: "/publish",
        name: "Publish",
        component: () =>
            import(/* webpackChunkName: "publish" */ "@/views/Publish.vue")
    },
    {
        path: "/userprofile",
        name: "UserProfile",
        component: () =>
            import(/* webpackChunkName: "userprofile" */ "@/views/UserProfile.vue")
    },
    {
        path: "/user",
        name: "User",
        component: () =>
            import(/* webpackChunkName: "user" */ "@/views/User.vue"),
        children: [
            {
                path: "userprofile",
                name: "UserProfile",
                component: () =>
                    import(/* webpackChunkName: "userprofile" */ "@/views/UserProfile.vue")
            },
        ],
    },
    {
        path: "/course",
        name: "Course",
        component: () =>
            import(/* webpackChunkName: "course" */ "@/views/Course.vue"),
    },
    {
        path: "/course-info/:id",
        name: "CourseInfo",
        component: () =>
            import(/* webpackChunkName: "courseinfo" */ "@/views/CourseInfo.vue"),
    },


];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

//前置守卫：页面跳转之前执行（导航守卫）
router.beforeEach((to, from, next) => {

    if (to.path === '/login') return next();
    //判断其他页面是否有token
    const tokenStore = useTokenStore()
    //存在继续往后走
    if (tokenStore) return next();
    // this.$router.push(name:‘login‘) #没有this,无法使用
    ElMessage.warning('未登录，请先登录！')
    router.push({name: 'login'})
        


    // if (to.matched.some(r=>r.meta?.requiresAuth)) {
    //     const tokenStore = useTokenStore()
    //     if (tokenStore.token) {
    //         console.log("tokenStore.token:",tokenStore.token)
    //         next({ name: "Login", query: { redirect: to.fullPath } })
    //     }else{
    //         alert('refresh值不正确')
    //         next({name: "Login"})
    //     }
    // }else{
    //     next();
    // }
});

//后置守卫：
router.afterEach((to, from, failure) => {
    if (!failure) sendToAnalytics(to.fullPath)
})

export default router;