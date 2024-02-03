<template>
    <!-- 전체 페이지를 감싸는 컨테이너 -->
    <div class="card-page w-full" style="display: flex;">
      <!-- 이미지 페이지 컴포넌트 -->
      <Img-Page :style="{ flex: isBlankPageVisible ? '1 0 700px' : '1 0 0' }" @sampleImage="handleSampleImage" :imageUrl="currentImageUrl"></Img-Page>

      <!-- 서브 메뉴 컴포넌트 -->
      <Sub-Menu
        v-if="isBlankPageVisible"
        :style="{ flex: '1 0 1000px', 'padding-left': '5%' }"
        @imageClick="handleImageClick"
      ></Sub-Menu>
    </div>
</template>
  
<script>
  /**
  * 모델 데모 페이지 컨테이너 컴포넌트
  *
  * @component
  * @export
  */
  import ImgPage from './ImgPage.vue';
  import SubMenu from './SubMenu.vue';
  
  export default {
    components: {
      ImgPage,
      SubMenu,
    },
    data() {
      return {
        isBlankPageVisible: true,
        currentImageUrl: '',
        currentSampleUrl: '',
      };
    },

    /**
    * 컴포넌트가 마운트된 후에 실행되는 라이프사이클 훅
    * 창 크기 조절 이벤트를 수신하고, 초기에도 크기를 조절하는 역할
    *
    * @method
    */
    mounted() {
      window.addEventListener('resize', this.handleResize);
      this.handleResize();
    },

    /**
    * 컴포넌트가 파괴되기 전에 실행되는 훅
    * 창 크기 조절 이벤트 리스너를 제거하여 메모리 누수를 방지
    *
    * @method
    */
    beforeDestroy() {
      window.removeEventListener('resize', this.handleResize);
    },

    methods: {
      /**
      * 이미지 클릭 이벤트 핸들러
      *
      * 클릭한 이미지의 URL을 현재 이미지 URL 상태에 업데이트
      * 
      * @method
      * @param {String} url - 클릭한 이미지의 URL
      */
      handleImageClick(url) {
        this.currentImageUrl = url;
      },

      /**
      * 샘플 이미지 이벤트 핸들러
      *
      * 선택한 샘플 이미지의 URL을 현재 샘플 이미지 URL 상태에 업데이트
      * 
      * @method
      * @param {String} url - 선택한 샘플 이미지의 URL
      */
      handleSampleImage(url) {
        this.currentSampleUrl = url;
      },

      /**
      * 창 크기 조절 이벤트 핸들러
      *
      * 창의 너비가 1200px 이상이면 isBlankPageVisible 상태를 true로 설정
      * 않으면 false로 설정하여 블랭크 페이지를 표시 또는 숨김
      * 
      * @method
      */
      handleResize() {
        this.isBlankPageVisible = window.innerWidth > 1200;
      },
    },
  };
</script>