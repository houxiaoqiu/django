import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
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
      import(/* webpackChunkName: "CourseInfo" */ "../views/CourseInfo.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;