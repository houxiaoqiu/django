import { createRouter, createWebHistory } from "vue-router";

const routes = [
    {
        path: "/login",
        name: "Login",
        component: () =>
            import(/* webpackChunkName: "login" */ "../views/login/Login.vue")
    },
    {
        path: "/",
        name: "Home",
        component: () =>
            import(/* webpackChunkName: "home" */ "../views/Home.vue")
    },
    {
        path: "/register",
        name: "Register",
        component: () =>
            import(/* webpackChunkName: "register" */ "../views/Register.vue")
    },
    {
        path: "/admin",
        name: "Admin",
        component: () =>
            import(/* webpackChunkName: "admin" */ "../views/Admin.vue"),
        children: [
            {
                path: "",
                component: () =>
                    import(/* webpackChunkName: "publish" */ "../views/Publish.vue")
            },
            {
                path: "/shopping",
                name: "Shopping",
                component: () =>
                    import(/* webpackChunkName: "about" */ "../components/shopping/Shopping.vue"),
            },
            {
                path: "/shoppinglist",
                name: "ShoppingList",
                component: () =>
                    import(/* webpackChunkName: "about" */ "../components/shopping/ShoppingList.vue"),
            },
            {
                path: "/shoppingcart",
                name: "ShoppingCart",
                component: () =>
                    import(/* webpackChunkName: "about" */ "../components/shopping/ShoppingCart.vue"),
            },
            {
                path: "/about",
                name: "About",
                component: () =>
                    import(/* webpackChunkName: "about" */ "../views/About.vue"),
            },
            {
                path: "/:xxx(.*)*",
                name: "Error",
                component: () => 
                    import(/* webpackChunkName: "about" */ "../components/common/Error.vue"),
            },
        ],
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
    {
        path: "/course",
        name: "Course",
        component: () =>
            import(/* webpackChunkName: "course" */ "../views/Course.vue"),
    },
    {
        path: "/course-info/:id",
        name: "CourseInfo",
        component: () =>
            import(/* webpackChunkName: "courseinfo" */ "../views/CourseInfo.vue"),
    },
    {
        path: "/login1",
        name: "Login1",
        component: () =>
            import(/* webpackChunkName: "login" */ "../views/login/Login1.vue"),
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
    if (!failure) sendToAnalytics(to.fullPath)
})

export default router;