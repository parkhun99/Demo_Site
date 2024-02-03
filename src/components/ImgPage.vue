<!-- 모델 정보를 표시하고 관련된 이미지와 샘플 이미지를 렌더링 -->
<template>
  <div class="card-page lg:h-screen h-auto">
    <div class="white-box">
    <!-- 좌측 상단 현재 위치 표시 -->
    <nav class="flex" aria-label="Breadcrumb">
      <ol class="inline-flex items-center space-x-1 md:space-x-1 text-sm text-gray-500" style="font-weight: 400;">
        <li class="inline-flex items-center" style="margin-left: 4%; white-space: nowrap;">
          {{ category }}
        </li>
        <li>
          <div class="flex items-center">
           <svg
              class="w-7 h-6 text-gray-500"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
              style="transform: translateX(3px);"
            >
              <path
                fill-rule="evenodd"
                d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                clip-rule="evenodd"
              ></path>
            </svg>   
            <p style="margin-left: 4%; white-space: nowrap;">{{ item }}</p>
          </div>
        </li>
      </ol>
    </nav>
  </div>
    <!-- 배너 이미지 세션 -->
    <div style="padding-left: 5%; margin-top: -20px;">
      <h1 class="text-xl text-gray-700 font-bold italic underline-style">Model Description</h1>
      <div class="card w-full p-5 text-center bg-white banner-container flex items-start">
        <img :src="thumnailData" alt="Thumbnail Image" v-if="thumnailData" class="responsive-image" style="object-fit: cover; width: 150px; height: 150px; margin-left: 1%;">
        <div class="flex-grow text-left" style="margin-left: 4%;">
          <h1 class="text-lg text-gray-700 font-bold mt-1" style="margin-bottom: 0.5%;">
            {{ item }}
          </h1>
          <p class="text-gray-500" style="margin-left: 12px; font-size: 13px;">{{ description }}</p>
          <h2 class="text-md text-gray-700 font-medium" style="margin-top: 10px;">사용 방법</h2>
          <p class="text-gray-500" style="margin-left: 12px; font-size: 13px;">- 파일 선택, 예시 이미지를 드래그 또는 클릭하여 이미지 파일을 업로드한다. <br>- 전송 버튼을 누르고 결과를 기다립니다.</p>
          <div class="text-blue-800 cursor-pointer font-medium" style="display: flex; justify-content: flex-end; font-size: 0.8rem;">
          <button @click="openDescriptionPage" style="display: flex; align-items: center; margin-bottom: -20px;">
            <svg width="16px" height="16px" viewBox="0 0 48.00 48.00" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="#003366" stroke-width="1.104" style="margin-left: 8px;">
              <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
              <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
              <g id="SVGRepo_iconCarrier">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M29.2045 31.5594C26.8468 33.1027 24.0282 34 21 34C12.7157 34 6 27.2843 6 19C6 10.7157 12.7157 4 21 4C29.2843 4 36 10.7157 36 19C36 23.1233 34.3363 26.858 31.6436 29.5695L33.114 29.4062L39 36.5L34.7322 40.1773L28.7988 33.0271L29.2045 31.5594ZM33 19C33 25.6274 27.6274 31 21 31C14.3726 31 9 25.6274 9 19C9 12.3726 14.3726 7 21 7C27.6274 7 33 12.3726 33 19Z" fill="#0074CC"></path>
                <path d="M36.1246 41.7577L40.3924 38.0804L41.7191 39.6614C42.4291 40.5076 42.3187 41.7691 41.4726 42.4791L40.2216 43.5288C39.3754 44.2388 38.1139 44.1284 37.4039 43.2823L36.1246 41.7577Z" fill="#0074CC"></path>
                <path fill-rule="evenodd" clip-rule="evenodd" d="M20.7382 11.5658C18.955 11.6352 17.3157 12.2705 16.4177 13.1687C16.1248 13.4616 15.6499 13.4617 15.357 13.1688C15.0641 12.8759 15.064 12.4011 15.3569 12.1081C16.5972 10.8676 18.6412 10.1463 20.6799 10.067C22.7288 9.98724 24.9392 10.5499 26.477 12.088C26.7699 12.3809 26.7699 12.8558 26.4769 13.1487C26.184 13.4415 25.7091 13.4415 25.4163 13.1486C24.2614 11.9935 22.5112 11.4968 20.7382 11.5658Z" fill="#0074CC"></path>
              </g>
            </svg>
            모델 설명 더보기
          </button>
          <button @click="openInquiryPage" style="display: flex; align-items: center; margin-left: 20px; margin-bottom: -20px;">
            <svg width="16px" height="16px" viewBox="0 0 32 32" fill="#003366" xmlns="http://www.w3.org/2000/svg">
              <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
              <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
              <g id="SVGRepo_iconCarrier">
                <title>pencil</title>
                <path d="M0 32l12-4 20-20-8-8-20 20zM4 28l2.016-5.984 4 4zM8 20l12-12 4 4-12 12z"></path>
              </g>
            </svg>
            솔루션 문의하기
          </button>
        </div>
        </div>
      </div>
      <h1 class="text-xl text-gray-700 font-bold italic underline-style" style="padding-top: 5px;">Demo</h1>
      <Img-Result :key="loadedImageUrl" :category="category" :item="item" :imageUrl="loadedImageUrl" :sampleUrl="customImg" style="margin-top: -50px;"></Img-Result>
        <h1 class="text-xl text-gray-700 font-bold italic underline-style">Sample Image</h1>
        <Sample-Img @sampleImage="handleImage" :category="category" :item="item"></Sample-Img>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ImgResult from "@/components/ImgResult.vue";
import SampleImg from "@/components/SampleImg.vue";

export default {
  /**
 * @typedef {Object} ModelPageProps
 * @property {string} imageUrl - sub-Menu.vue image URL
 * @property {string} sampleUrl - Sampleimage.vue image URL
 */
  props: {
    imageUrl: String,
    sampleUrl: String,
  },

  // 자식 컴포넌트로 ImgResult 및 SampleImg를 등록
  components: {
    ImgResult,
    SampleImg,
  },

  /**
  * @typedef {Object} ModelPageData
  * @property {String} category - 현재 페이지의 모델 카테고리
  * @property {String} item - 현재 페이지의 모델 아이템
  * @property {String|null} thumnailData - 모델 썸네일 이미지 URL
  * @property {String|null} description - 모델 설명
  * @property {String|null} site - 부가 설명 페이지 URL
  * @property {String} customImg - 사용자가 선택한 이미지 URL
  */
  // 컴포넌트 내에서 사용할 데이터를 초기화
  data() {
    return {
      category: this.$route.query.category,
      item: this.$route.query.item,
      thumnailData: null,
      description: null,
      site: null,
      customImg: '',
    };
  },
  watch: {
    
    imageUrl(newUrl, oldUrl) {
      this.loadedImageUrl = newUrl;
    },
    // 라우터의 변경을 감지하는 워치
    $route(to, from) {
      this.category = to.query.category;
      this.item = to.query.item;
      this.fetchData(); // 데이터를 비동기로 가져옵니다.
      this.fetchSite(); // 부가 정보 페이지의 URL을 가져옵니다.
    },
  },
  // 컴포넌트가 생성될 때 초기 데이터 로딩을 수행
  created() {
    this.fetchData();
    this.fetchSite();
  },
  methods: {
    /**
     * 사용자가 이미지를 선택했을 때 호출되는 메서드.
     *
     * @param {String} newUrl - 사용자가 선택한 샘플 이미지의 URL
     * @emits {String} sampleImage - 사용자가 선택한 샘플 이미지 ImgResult.vue로 전달
     */
    handleImage(newUrl) {
      this.customImg = newUrl;
      this.$emit('sampleImage', newUrl);
    },

    /**
    * fetchData - 서버에서 서브 카테고리 데이터를 비동기적으로 요청하여 받아오는 메서드.
    *
    * @throws {Error} - 데이터를 가져오는 중에 발생한 오류
    * 
    * @returns {Promise<void>} - 데이터를 가져와서 컴포넌트 상태를 업데이트하는 Promise
    * 
    * @description
    * 서버 응답에서 썸네일 이미지(thumnail_url), 모델 설명(model_Description) 변수에 할당,
    * 데이터를 가져오는 중에 오류가 발생하면 오류 메시지를 출력하고, 예외를 throw하여 처리
    */
    async fetchData() {
      try {
        const response = await axios.get("http://192.168.0.32:8402/modelCategory", {
          item: this.item,
        });
        if (response.data && response.data.data_from_first_app && response.data.data_from_first_app.result) {
          this.thumnailData = response.data.data_from_first_app.result[this.item]?.thumnail_url;
          this.description = response.data.data_from_first_app.result[this.item]?.model_Description;
        } 
      } catch (error) {
        console.error("데이터 가져오기 중 오류:", error);
      }
    },

    /**
    * fetchSite - 서버에서 서브 카테고리 데이터를 비동기적으로 요청하여 받아오는 메서드.
    *
    * @throws {Error} - 데이터를 가져오는 중에 발생한 오류
    * 
    * @returns {Promise<void>} - 데이터를 가져와서 컴포넌트 상태를 업데이트하는 Promise
    * 
    * @description
    * 서버 응답에서 사이트(site_url)을 변수에 할당,
    * 데이터를 가져오는 중에 오류가 발생하면 오류 메시지를 출력하고, 예외를 throw하여 처리
    */
    async fetchSite() {
      try {
        const response = await axios.get("http://192.168.0.32:8402/sampleImg", {
          item: this.item,
        });
        this.site = response.data.data_from_first_app.result[this.item].site_url;
      } catch (error) {
        console.error("부가 설명 페이지 가져오기 오류:", error);
      }
    },

     // 모델 설명 페이지를 새 창에서 오픈
    openDescriptionPage() {
      window.open(this.site, "_blank");
    },

    // 솔루션 문의 페이지를 새 창에서 오픈
    openInquiryPage() {
      window.open('https://www.m47rix.com/21', '_blank');
    },
  },
};
</script>

<style scoped>
.underline-style {
    display: inline-block;
    position: relative;
    padding-top: 80px;
  }
.white-box {
  width: 100%;
  background-color: white;
  border-bottom: 2px solid #e7e6e6;
  display: flex;
  height: 58px;
  position: fixed;
  left: 0;
}
.banner-container {
  max-width: 800px;
  margin-right: 40%;
  border-radius: 20px;
  border: 2px solid #e7e6e6;
}
.responsive-image {
  border-radius: 20%;
  padding: 5px; /* 테두리와 이미지 사이의 간격을 조절 */
  box-shadow: 0 0 0 1px #fff, 0 0 0 5px rgb(179, 195, 249);;
}
</style>