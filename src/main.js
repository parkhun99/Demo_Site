import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import VueApexCharts from "vue3-apexcharts";
import PerfectScrollbar from "vue3-perfect-scrollbar";
import "vue3-perfect-scrollbar/dist/vue3-perfect-scrollbar.css";
import { createPinia } from "pinia";
import "./assets/style.css";
import vClickOutside from "click-outside-vue3";

const app = createApp(App);
app.use(router);
app.use(createPinia());
app.use(VueApexCharts);
app.use(PerfectScrollbar);
app.use(vClickOutside);

// 경고 메시지를 비활성화
app.config.warnHandler = () => {};

app.mount("#app");