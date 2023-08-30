// import { createRouter, createWebHistory } from "vue-router";
// import { useTokenStore } from "@/utils/token";

export const constantRoute = [
  {
    path: "/",
    redirect: "/admin", // 重定向
  },
  {
    path: "/login",
    name: "Login",
    component: () =>
      import(/* webpackChunkName: "login" */ "@/views/User.vue"),
      // import(/* webpackChunkName: "login" */ "@/views/admin/Login.vue"),
  },
  {
    path: "/register",
    name: "Register",
    component: () =>
      import(/* webpackChunkName: "register" */ "@/views/admin/Register.vue"),
  },
  {
    path: "/home",
    name: "Home",
    component: () =>
      import(/* webpackChunkName: "home" */ "@/views/public/Home.vue"),
    meta: { 
      title: '首页',
      hidden: false,
      icon: 'HomeFilled' 
    }, 
  },
  {
    path: "/admin",
    name: "Admin",
    component: () =>
      import(/* webpackChunkName: "admin" */ "@/views/admin/Admin.vue"),
    meta: { 
      title: '',
      hidden: false,
      icon: ''
    }, 
    children: [
      {
        path: "",
        component: () =>
          import(/* webpackChunkName: "publish" */ "@/views/Publish.vue"),
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
              import(
                /* webpackChunkName: "userprofile" */ "@/views/UserProfile.vue"
              ),
          },
        ],
      },
      {
        path: "/shopping",
        name: "Shopping",
        component: () =>
          import(
            /* webpackChunkName: "about" */ "@/components/shopping/Shopping.vue"
          ),
      },
      {
        path: "/shoppinglist",
        name: "ShoppingList",
        component: () =>
          import(
            /* webpackChunkName: "about" */ "@/components/shopping/ShoppingList.vue"
          ),
      },
      {
        path: "/shoppingcart",
        name: "ShoppingCart",
        component: () =>
          import(
            /* webpackChunkName: "about" */ "@/components/shopping/ShoppingCart.vue"
          ),
      },
      {
        path: "/about",
        name: "About",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/views/public/About.vue"),
      },
      {
        path: "/:xxx(.*)*",
        name: "Error",
        component: () =>
          import(
            /* webpackChunkName: "about" */ "@/components/common/Error.vue"
          ),
      },
      {
        path: "/contactOption",
        name: "ContactOption",
        component: () =>
          import(
            /* webpackChunkName: "contact" */ "@/views/contact/ContactOption.vue"
          ),
      },
      {
        path: "/contactorgnization",
        name: "ContactOrgnization",
        component: () =>
          import(
            /* webpackChunkName: "contact" */ "@/views/contact/ContactOrgnization.vue"
          ),
      },
      {
        path: "/contactperson",
        name: "ContactPerson",
        component: () =>
          import(
            /* webpackChunkName: "contact" */ "@/views/contact/ContactPerson.vue"
          ),
      },
      {
        path: "/hroption",
        name: "HrOption",
        component: () =>
          import(/* webpackChunkName: "wms" */ "@/views/hr/HrOption.vue"),
      },
      {
        path: "/hrorgnization",
        name: "HrOrgnitation",
        component: () =>
          import(/* webpackChunkName: "wms" */ "@/views/hr/hrOrgnization.vue"),
      },
      {
        path: "/hremployee",
        name: "HrEmployee",
        component: () =>
          import(/* webpackChunkName: "wms" */ "@/views/hr/hrEmployee.vue"),
      },
      {
        path: "/wmsoption",
        name: "WmsOption",
        component: () =>
          import(/* webpackChunkName: "wms" */ "@/views/wms/WmsOption.vue"),
      },
      {
        path: "/wmstransfer",
        name: "WmsTransfer",
        component: () =>
          import(/* webpackChunkName: "wms" */ "@/views/wms/WmsTransfer.vue"),
      },
      {
        path: "/wmsmaterial",
        name: "WmsMaterial",
        component: () =>
          import(/* webpackChunkName: "wms" */ "@/views/wms/WmsMaterial.vue"),
      },
      {
        path: "/wmsunit",
        name: "WmsUnit",
        component: () =>
          import(/* webpackChunkName: "wms" */ "@/views/wms/WmsUnit.vue"),
      },
      {
        path: "/wmswherehouse",
        name: "WmsWherehouse",
        component: () =>
          import(/* webpackChunkName: "wms" */ "@/views/wms/WmsWherehouse.vue"),
      },
      {
        path: "/wmsbom",
        name: "WmsBom",
        component: () =>
          import(/* webpackChunkName: "wms" */ "@/views/wms/WmsBom.vue"),
      },
      {
        path: "/aimregister",
        name: "AimRegister",
        component: () =>
          import(/* webpackChunkName: "wms" */ "@/views/aim/AimRegister.vue"),
      },
      {
        path: "/aimsetting",
        name: "AimSetting",
        component: () =>
          import(/* webpackChunkName: "wms" */ "@/views/aim/AimSetting.vue"),
      },
    ],
  },

  {
    path: "/publish",
    name: "Publish",
    component: () =>
      import(/* webpackChunkName: "publish" */ "@/views/Publish.vue"),
  },
  {
    path: "/userprofile",
    name: "UserProfile",
    component: () =>
      import(/* webpackChunkName: "userprofile" */ "@/views/UserProfile.vue"),
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

// const router = createRouter({
//   history: createWebHistory(),
//   routes,
// });

// // 注册方法（一）- 全局前置守卫：页面跳转之前执行（导航守卫）
// router.beforeEach((to, from, next) => {
//   const tokenStore = useTokenStore();
//   const isAuthenticated = tokenStore.token;
//   console.log("全局前置守卫-tokenStore.token", tokenStore.token);

//   if (to.name !== "Login" && !isAuthenticated) {
//     ElMessage.warning("未登录，请先登录！");
//     next({ name: "Login" });
//   } else next();
// });

// // 注册方法（二）- 全局解析守卫：在导航被确认之前、所有组件内守卫和异步路由组件被解析之后调用
// // 这里有一个例子，确保用户可以访问自定义 meta 属性 requiresCamera 的路由
// // router.beforeResolve(async to => {
// //     if (to.meta.requiresCamera) {
// //       try {
// //         await askForCameraPermission()
// //       } catch (error) {
// //         if (error instanceof NotAllowedError) {
// //           // ... 处理错误，然后取消导航
// //           return false
// //         } else {
// //           // 意料之外的错误，取消导航并把错误传给全局处理器
// //           throw error
// //         }
// //       }
// //     }
// // });

// // 后置守卫：
// router.afterEach((to, from, failure) => {
//   // if (!failure) sendToAnalytics(to.fullPath)
// });

//export default router;
