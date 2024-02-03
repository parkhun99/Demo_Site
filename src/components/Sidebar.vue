<!--
  Sidebar 컴포넌트는 웹 애플리케이션의 사이드바를 구현

  @component
  @props {Array} categories - 카테고리 목록을 받아오는 prop
  @props {String} selectedItem - 현재 선택된 항목을 나타내는 prop

  @event sidebarToggle - 부모 컴포넌트(App.vue)로 사이드바 토글 이벤트를 전달
-->
<template>
  <div>
    <nav class="sidebar">
      <div class="sidebar-head">
        <router-link to="/" exact class="flex">
          <div class="image-container relative">
            <img class="w-40 ml-7" src="@/assets/logo/Matrix_W2.png" alt="logo Matrix" style="padding-top: 13px; padding-bottom: 13px;"/>
            <div class="gray-line"></div>
          </div>
        </router-link>
        <button class="lg:hidden block float-right -mt-10" @click="$emit('sidebarToggle')">
          <svg width="25px" height="25px" viewBox="0 0 32 32">
            <path fill="currentColor" d="M7.219 5.781L5.78 7.22L14.563 16L5.78 24.781l1.44 1.439L16 17.437l8.781 8.782l1.438-1.438L17.437 16l8.782-8.781L24.78 5.78L16 14.563z" />
          </svg>
        </button>
      </div>
      <div class="sidebar-list p-4 mt-2 divide-y">
        <div class="wrap-item">
          <div class="item">
            <menu-accordion v-for="category in categories" :key="category.name">
              <template v-slot:title>
                <div @click="fetchCategory(category.name)">{{ category.name }}</div>
              </template>
              <template v-slot:content>
                <div class="w-full text-left ml-1 block p-3" style="font-size: 14.5px;">
                  <ul>
                    <li
                      class="menu-item"
                      v-for="(item, index) in category.items"
                      :key="index"
                      @click.stop="handleItemClick(category.name, item)"
                      :class="{ 'font-bold': selectedItem === item }"
                    >
                      {{ item }}
                    </li>
                  </ul>
                </div>
              </template>
            </menu-accordion>
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
/**
* 이 파일은 다음과 같은 기능을 담당하는 Vue.js 컴포넌트 및 라이브러리를 import
*
* 1. @iconify/vue: 아이콘을 렌더링하기 위한 Vue.js용 아이콘 라이브러리
* 2. MenuAccordion.vue: 사용자 정의 메뉴 아코디언 컴포넌트
* 3. axios: HTTP 클라이언트 라이브러리를 사용하여 서버로 HTTP 요청을 보내는 기능
*
* @module
*/
import { Icon } from "@iconify/vue";
import MenuAccordion from "./MenuAccordion.vue";
import axios from 'axios';

export default {
  components: {
    Icon,
    MenuAccordion,
  },
  data() {
    return {
      categories: [],
      selectedItem: null,
    };
  },

  /**
  * 컴포넌트가 생성될 때 자동으로 호출되는 라이프사이클 훅
  *
  * @method
  * @async
  * @name created
  */
  async created() {
    await this.fetchCategories();
  },

  methods: {
    /**
    * 서버에 GET 요청을 보내어 카테고리 데이터를 가져오고, 컴포넌트의 상태를 업데이트하는 비동기 함수
    *
    * @async
    * @method
    * @name fetchCategories
    * @memberof SidebarComponent
    * @description
    * 이 함수는 서버로 GET 요청을 보내어 카테고리 데이터를 비동기적으로 가져오는 역할
    * 성공적으로 데이터를 받아오면 내부의 categories 상태가 업데이트되며, 각 카테고리는 이름과 해당 카테고리에 속하는 아이템들의 배열로 구성된 객체로 매핑
    * @throws {Error} - 데이터를 가져오는 중에 오류가 발생한 경우 에러를 던짐
    */
    async fetchCategories() {
      try {
        const response = await axios.get('http://192.168.0.32:8402/getCategory');
        const categoryData = response.data;
        if (categoryData?.data_from_first_app?.result) {
          this.categories = Object.entries(categoryData.data_from_first_app.result).map(([name, items]) => ({
            name,
            items,
          }));
        }
      } catch (error) {
        console.error('카테고리를 불러오는 중 오류 발생:', error);
      }
    },

    fetchCategory(category) {
      // 카테고리 처리
    },

    /**
    * 사이드바 메뉴에서 항목을 클릭할 때 호출되는 메서드입니다.
    *
    * @method
    * @name handleItemClick
    * @memberof SidebarComponent
    *
    * @param {string} category - 선택한 항목의 속한 카테고리 이름
    * @param {string} item - 선택한 항목의 이름
    *
    * @description
    * 이 메서드는 사용자가 사이드바 메뉴에서 항목을 클릭할 때 호출
    * 라우터를 사용하여 URL을 업데이트하여 해당 항목에 대한 페이지로 이동
    */
    handleItemClick(category, item) {
      this.selectedItem = item;
      this.$router.push({ path: '/components/ModelDemo', query: { category, item } });
    },
  },
};
</script>

<style scoped>
  .menu-item {
    padding: 5px 0;
  }
  .menu-item:hover {
    cursor: pointer;
    background-color: #cccccc;
    border-radius: 5px;
    transition: background-color 0.7s;
  }
  .gray-line {
    position: absolute;
    bottom: 0;
    margin-left: -15px;
    width: 283px;
    height: 2px; /* 높이 조절 가능 */
    background-color: #e7e6e6; /* 회색 색상 지정 */
  }
</style>