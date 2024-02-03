<template>
  <!-- 메인 페이지 css -->
  <div class="flex bg-gray-50">
    <div
      v-if="!$route.meta.hideNav"
      class="lg:block"
      :class="{ 'lg:block hidden': !sidebar, block: sidebar }"
    >
      <!-- 사이드바 항목 css -->
      <div
        class="lg:flex-auto w-sidebar bg-white border-r-2 lg:z-0 z-20 overflow-auto lg:relative fixed"
        >
        <perfect-scrollbar class="h-screen">
          <Sidebar
            v-if="!$route.meta.hideNav"
            @sidebarToggle="close"
          />
        </perfect-scrollbar>
      </div>
    </div>
    <div
      class="flex-auto w-full overflow-auto h-screen transition-colors"
      id="body-scroll"
    >
      <Header
        v-if="!$route.meta.hideNav"
        @sidebarToggle="open"
        :isMainPage="$route.meta.isMainPage" />
      <transition
        name="slide-up"
        mode="out-in" >
        <router-view />
      </transition>
    </div>
  </div>
  <!-- End app -->
</template>

<script>
  // Vue components
  import Sidebar from "@/components/Sidebar";
  import Header from "@/components/Header";

  // npm-js
  import Scrollbar from "smooth-scrollbar";

  export default {
    name: "App",
    data() {
      return {
        sidebar: false,
      };
    },
    components: {
      Header,
      Sidebar,
    },
    methods: {
      open() {
        this.sidebar = true;
      },
      close() {
        this.sidebar = false;
      },
    },
    watch: {
      $route() {
        this.sidebar = false;
      },
    },
    mounted() {
      Scrollbar.init(document.querySelector("#body-scroll"));
    },
  };
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,400;0,700;1,400&family=Khand:wght@400&display=swap');
/* Khand 폰트 추가 */
body {
  font-family: 'Khand', sans-serif;
}
/* Open Sans 이탤릭체로 변경 */
body {
  font-family: 'Khand', sans-serif;
}
/* 영어에는 italic 스타일 적용 */
body:lang(en) {
  font-style: italic;
}
/* 한글에는 기본 스타일 유지 */
body:lang(ko) {
  font-style: normal;
}
  .slide-up-enter-active {
    transition: all 0.3s ease-out;
  }
  .slide-up-leave-active {
    transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
  }
  .slide-up-enter-from,
  .slide-up-leave-to {
    transform: translateY(20px);
    opacity: 0;
  }
  .w-sidebar {
    width: 240px !important;
  }
</style>