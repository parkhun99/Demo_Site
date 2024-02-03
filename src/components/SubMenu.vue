<template>
  <div class="blank-page">
    <h1 class="text-xl text-gray-700 font-bold italic underline-style" style="padding-left: 1%;">Sub Menu</h1>
    <div class="white-box" style="margin-left: -70px; display: flex; flex-direction: column;">
      <button class="button-font ml-3 mb-6" @click="openHomePage">홈페이지</button>
      <button class="button-font ml-3 mb-3" @click="openInquiryPage">솔루션 문의하기</button>
      <MenuAccordion :open="showImages" @toggleAccordion="toggleImagesDropdown">
        <template v-slot:title>
          <div class="text-font">샘플 이미지</div>
        </template>
        <!-- 드롭다운 이미지 표시 -->
        <template v-slot:content>
          <div @click.stop>
            <div v-for="(url, index) in imgUrls" :key="index">
              <img :src="url" alt="솔루션 이미지" class="sample-image" @click="handleImageClick(url)">
            </div>
          </div>
        </template>
      </MenuAccordion>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import MenuAccordion from "./MenuAccordion.vue";

export default {
  props: {
    sampleUrl: String,
  },
  components: {
    MenuAccordion,
  },

  /**
 * 컴포넌트의 초기 데이터 상태를 정의하는 객체입니다.
 *
 * @typedef {Object} ImgPageData
 * @property {String} item - 현재 페이지의 모델 아이템 정보
 * @property {Boolean} showImages - 이미지 목록을 표시할지 여부를 나타내는 상태
 * @property {String[]} imgUrls - 이미지 목록의 URL을 담은 배열
 */

/**
 * 현재 페이지의 데이터 상태를 초기화하는 메서드입니다.
 *
 * @method
 * @memberof Components.ImgPage
 * @returns {ImgPageData} - 초기화된 데이터 상태 객체
 */
  data() {
    return {
      item: this.$route.query.item,
      showImages: false,
      imgUrls: [],
    };
  },
  /**
  * 컴포넌트가 마운트된 후에 실행되는 라이프사이클 훅
  *
  * @method
  * @async
  * @memberof Components.ImgPage
  *
  * @description
  * 컴포넌트가 마운트된 후에 자동으로 호출, fetchImg 메서드를 실행
  * 샘플 이미지를 가져옴. 이미지를 가져오기 위해 비동기로 처리되므로 await 키워드를 사용
  * 
  * @see {@link fetchImg}
  */
  async mounted() {
    await this.fetchImg();
  },

  watch: {
    /**
    * sampleUrl 프로퍼티의 변경을 감시하는 워치
    *
    * @method
    * @memberof Components.ImgPage
    * @param {String} newSampleUrl - 새로운 sampleUrl 값
    * @param {String} oldSampleUrl - 변경 전의 sampleUrl 값
    *
    * @description
    * 이 워치어는 sampleUrl 값이 변경될 때마다 호출되며, 변경 시 handleImageClick 메서드를 실행하여
    * 이미지 클릭 이벤트를 처리, sampleUrl 값이 변경되면 선택된 이미지를 초기화
    * 
    * @see {@link handleImageClick}
    */
    sampleUrl: function(newSampleUrl, oldSampleUrl) {
      this.handleImageClick(null); 
    },

    /**
    * 라우트 변경을 감시하는 워치
    *
    * @async
    * @method
    * @memberof VueComponent
    * @param {Object} to - 이동할 라우트 객체
    * @param {Object} from - 현재 라우트 객체
    *
    * @description
    * 이 워치어는 라우트의 쿼리 파라미터 중 item 값이 변경될 때마다 호출,
    * 변경 시 해당 라우트의 item 값을 가져와 fetchImg 메서드를 실행
    * 새로운 이미지 데이터를 가져옴, showImages 상태를 false로 설정하여
    * 이미지를 감추는 효과 실행
    * 
    * @see {@link fetchImg}
    */
    async $route(to, from) {
      if (to.query.item !== from.query.item) {
        this.item = to.query.item;
        this.fetchImg();
        this.showImages = false;
      }
    },
  },

  methods: {
    /**
    * sampleImg 앤드포인트에서 샘플 이미지를 가져오는 비동기 함수
    *
    * @async
    * @method
    * @memberof Components.ImgPage
    *
    * @description
    * 서버의 '/sampleImg' 엔드포인트에 GET 요청을 보냄
    * 현재 컴포넌트의 item(sub_category) 값을 기반으로 샘플 이미지 데이터를 받아옴
    * 받아온 이미지 데이터는 imgUrls 상태에 업데이트, showImages 상태를 false로 설정
    * 이미지를 감추며, handleImageClick 메서드를 실행하여 선택된 이미지를 초기화
    *
    * @throws {Error} 서버 요청이 실패한 경우 에러를 던짐
    *
    * @see {@link handleImageClick}
    */
    async fetchImg() {
      try {
        const response = await axios.get("http://192.168.0.32:8402/sampleImg", {
          params: { item: this.item },
        });
        this.imgUrls = response.data.data_from_first_app.result[this.item].img_url;
        this.showImages = false;
        this.handleImageClick(null); 
      } catch (error) {
        console.error("이미지 가져오기 오류:", error);
      }
    },

    /**
    * 이미지 드롭다운의 표시 여부를 토글하는 함수
    *
    * @method
    * @memberof Components.ImgPage
    *
    * @description
    * 현재 컴포넌트의 showImages 상태를 반전시켜 이미지 드롭다운의 표시 여부를 변경
    * 이 메서드를 호출하면 이미지 드롭다운이 표시되었다면 숨겨지고, 숨겨져 있었다면 표시
    */
    toggleImagesDropdown() {
      this.showImages = !this.showImages;
    },

    /**
    * 새 창에서 홈페이지를 열기 위한 함수
    *
    * @method
    * @memberof Components.ImgPage
    *
    * @description
    * 현재 창이나 새 탭이 아닌 새로운 브라우저 창에서 (https://www.m47rix.com/) 주소를 염
    */
    openHomePage() {
      window.open('https://www.m47rix.com/', '_blank');
    },
    /**
    * 새 창에서 홈페이지를 열기 위한 함수
    *
    * @method
    * @memberof Components.ImgPage
    *
    * @description
    * 현재 창이나 새 탭이 아닌 새로운 브라우저 창에서 (https://www.m47rix.com/21) 주소를 염
    */
    openInquiryPage() {
      window.open('https://www.m47rix.com/21', '_blank');
    },

    /**
    * 이미지 클릭 이벤트를 처리하는 함수
    *
    * @method
    * @memberof Components.ImgPage
    * 
    * @param {String} url - 클릭된 이미지의 URL
    * @param {Event} event - 클릭 이벤트 객체
    *
    * @description
    * 클릭된 이미지의 URL을 이벤트를 통해 부모 컴포넌트(ModelDemo.vue)로 전달
    */
    handleImageClick(url, event) {
      this.$emit('imageClick', url); // 이미지 클릭 이벤트를 발생시킴   
    },
  },
};
</script>

<style scoped>
.button-font,
.text-font {
  font-size: 14px;
  color: #414141;
  font-weight: bold;
}
.sample-image {
  object-fit: cover;
  width: 100%;
  height: 100%;
  max-width: 200px;
  max-height: 200px;
  border-radius: 20px;
  border: 2px solid #e7e6e6;
  margin-top: 10px;
  margin-left: 2.5%;
  cursor: pointer;
}
.underline-style {
  display: inline-block;
  position: relative;
}
.blank-page {
  display: flex;
  align-items: flex-start;
  padding-top: 60px;
}
.white-box {
  background-color: white;
  padding: 10px; /* 필요에 따라 패딩 조정 */
  margin-top: 27px; /* 필요에 따라 마진 조정 */
  border: 2px solid #e7e6e6;
  border-radius: 20px;
  width: 250px;
  display: flex;
  align-items: flex-start;
}
</style>