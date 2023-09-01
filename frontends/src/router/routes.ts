// import { createRouter, createWebHistory } from "vue-router";
// import { useTokenStore } from "@/utils/token";

export const constantRoute = [
  {
    path: "/login",
    name: "Login",
    component: () =>
      import(/* webpackChunkName: "login" */ "@/views/login/index.vue"),
      // import(/* webpackChunkName: "login" */ "@/views/admin/Login.vue"),
    meta: {
      title: '登录', //菜单标题
      hidden: true, //代表路由标题在菜单中是否隐藏  true:隐藏 false:不隐藏
      icon: 'Promotion', //菜单文字左侧的图标,支持element-plus全部图标
    },
  },
  // {
  //   path: "/register",
  //   name: "Register",
  //   component: () =>
  //     import(/* webpackChunkName: "register" */ "@/views/admin/Register.vue"),
  // },
  // {
  //   path: "/home",
  //   name: "Home",
  //   component: () =>
  //     import(/* webpackChunkName: "home" */ "@/views/public/Home.vue"),
  //   meta: { 
  //     title: '首页',
  //     hidden: false,
  //     icon: 'HomeFilled' 
  //   }, 
  // },
  {
    path: "/",
    name: "Home",
    component: () =>
      import(/* webpackChunkName: "admin" */ "@/views/admin/Admin.vue"),
    meta: { 
      title: '首页',
      hidden: false,
      icon: 'HomeFilled'
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

  // {
  //   path: "/publish",
  //   name: "Publish",
  //   component: () =>
  //     import(/* webpackChunkName: "publish" */ "@/views/Publish.vue"),
  // },
  // {
  //   path: "/userprofile",
  //   name: "UserProfile",
  //   component: () =>
  //     import(/* webpackChunkName: "userprofile" */ "@/views/UserProfile.vue"),
  // },
  // {
  //   path: "/course",
  //   name: "Course",
  //   component: () =>
  //     import(/* webpackChunkName: "course" */ "@/views/Course.vue"),
  // },
  // {
  //   path: "/course-info/:id",
  //   name: "CourseInfo",
  //   component: () =>
  //     import(/* webpackChunkName: "courseinfo" */ "@/views/CourseInfo.vue"),
  // },
];

//异步路由
export const asnycRoute = [
  {
    path: '/acl',
    component: () => import('@/layout/index.vue'),
    name: 'Acl',
    meta: {
      title: '系统管理',
      icon: 'Lock',
    },
    redirect: '/acl/user',
    children: [
      {
        path: '/acl/user',
        component: () => import('@/views/acl/user/index.vue'),
        name: 'User',
        meta: {
          title: '用户管理',
          icon: 'User',
        },
      },
      {
        path: '/acl/role',
        component: () => import('@/views/acl/role/index.vue'),
        name: 'Role',
        meta: {
          title: '角色管理',
          icon: 'UserFilled',
        },
      },
      {
        path: '/acl/permission',
        component: () => import('@/views/acl/permission/index.vue'),
        name: 'Permission',
        meta: {
          title: '菜单管理',
          icon: 'Monitor',
        },
      },
    ],
  },
  {
    path: '/product',
    component: () => import('@/layout/index.vue'),
    name: 'Product',
    meta: {
      title: '商品管理',
      icon: 'Goods',
    },
    redirect: '/product/trademark',
    children: [
      {
        path: '/product/trademark',
        component: () => import('@/views/product/trademark/index.vue'),
        name: 'Trademark',
        meta: {
          title: '品牌管理',
          icon: 'ShoppingCartFull',
        },
      },
      {
        path: '/product/attr',
        component: () => import('@/views/product/attr/index.vue'),
        name: 'Attr',
        meta: {
          title: '属性管理',
          icon: 'ChromeFilled',
        },
      },
      {
        path: '/product/spu',
        component: () => import('@/views/product/spu/index.vue'),
        name: 'Spu',
        meta: {
          title: 'SPU管理',
          icon: 'Calendar',
        },
      },
      {
        path: '/product/sku',
        component: () => import('@/views/product/sku/index.vue'),
        name: 'Sku',
        meta: {
          title: 'SKU管理',
          icon: 'Orange',
        },
      },
    ],
  },
  // {
  //   path: '/hr',
  //   component: () => import('@/layout/index.vue'),
  //   name: 'Product',
  //   meta: {
  //     title: '机构人员',
  //     icon: 'Goods',
  //   },
  //   redirect: '/production',
  //   children: [
  //     {
  //       path: '/production',
  //       component: () => import('@/views/product/trademark/index.vue'),
  //       name: 'Spu',
  //       meta: {
  //         title: '机构人员选项',
  //         icon: 'ShoppingCartFull',
  //       },
  //     },
  //     {
  //       path: '/product/attr',
  //       component: () => import('@/views/product/attr/index.vue'),
  //       name: 'Spu',
  //       meta: {
  //         title: '机构',
  //         icon: 'ChromeFilled',
  //       },
  //     },
  //     {
  //       path: '/product/spu',
  //       component: () => import('@/views/product/spu/index.vue'),
  //       name: 'Spu',
  //       meta: {
  //         title: '人员',
  //         icon: 'Calendar',
  //       },
  //     },
  //     {
  //       path: '/product/sku',
  //       component: () => import('@/views/product/sku/index.vue'),
  //       name: 'Sku',
  //       meta: {
  //         title: '人员',
  //         icon: 'Orange',
  //       },
  //     },
  //   ],
  // },
];

//任意路由
export const anyRoute = {
  //任意路由
  path: '/:pathMatch(.*)*',
  redirect: '/404',
  name: 'Any',
  meta: {
    title: '任意路由',
    hidden: true,
    icon: 'DataLine',
  },
}