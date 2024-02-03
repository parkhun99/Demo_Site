import { createRouter, createWebHistory } from "vue-router";

//Detection Pages
import DImgPage from "../components/ImgPage.vue";
import DMainPage from "../components/MainPage.vue";
import DModelDemoPage from "../components/ModelDemo.vue";

var appname = "The Matrix - ";

const routes = [
  //components/Detection
  {
    path: "/",
    name: "DMainPage",
    component: DMainPage,
    meta: { title: appname + "MainPage", hideNav: false, isMainPage: true },
  },
  {
    path: "/components/ImgPage",
    name: "DImgPage",
    component: DImgPage,
    meta: { title: appname + "ImgPage", hideNav: false, isMainPage: false },
  },
  {
    path: "/components/ModelDemo",
    name: "DModelDemoPage",
    component: DModelDemoPage,
    meta: { title: appname + "DemoPage", hideNav: false, isMainPage: false },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,

  linkExactActiveClass: "exact-active",
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title;
  next();
});

export default router;
