<template>
  <div class="card w-full p-2 text-center bg-white banner-container flex flex-wrap justify-around" style="cursor: pointer; ">
    <!-- 이미지 배열을 순회하며 렌더링 -->
    <img
      v-for="(url, index) in imgUrl"
      :key="index"
      :src="url"
      alt="Image"
      @dragstart="handleDragStart($event, url)"
      @click="handleImage(url)" 
      draggable="true"
      class="sample-image"
    />
  </div>
</template>

<script>
import axios from "axios";

export default {
  /**
  * Vue 컴포넌트의 데이터 속성을 정의하는 객체
  *
  * @returns {Object} - 데이터 속성 객체
  * - {String} item: 현재 라우트의 "item" 쿼리 파라미터 값을 저장하는 변수
  * - {Array|null} imgUrl: 렌더링할 이미지 URL 배열을 저장하는 변수
  */
  data() {
    return {
      item: this.$route.query.item,
      imgUrl: null,
    };
  },

  /**
  * Vue 컴포넌트의 라우터 변경을 감시하는 watch
  *
  * @property {Function} $route - 라우트 객체의 변경을 감시하는 함수
  * @param {Object} to - 변경된 라우트의 정보
  * @param {Object} from - 이전 라우트의 정보
  * @method
  *   - 변경된 라우트의 "item" 쿼리 파라미터가 이전과 다를 경우:
  *     - 현재 컴포넌트의 "item" 데이터 속성 업데이트
  *     - 이미지를 다시 가져오는 fetchImg 메서드 호출
  *     - handleImage 메서드 호출하여 이미지 초기화
  */
  watch: {
    $route(to, from) {
      if (to.query.item !== from.query.item) {
        this.item = to.query.item;
        this.fetchImg();
        this.handleImage(null);
      }
    },
  },

  /**
  * Vue 컴포넌트가 마운트된 후 자동으로 실행되는 라이프사이클 훅
  *
  * @async
  * @method
  *   - fetchImg 메서드를 호출하여 이미지를 비동기적으로 가져옴
  */
  async mounted() {
    await this.fetchImg();
  },

  methods: {
    /**
    * 이미지를 가져오는 비동기 함수
    *
    * @async
    * @method
    * @throws {Error} 이미지 가져오기에 실패한 경우 에러를 던짐
    * @returns {Promise<void>} - Promise를 반환하며, 성공적으로 이미지를 가져온 경우 imgUrl 상태를 업데이트
    */
    async fetchImg() {
      try {
        // 서버에 GET 요청을 보내어 해당 아이템에 대한 이미지 URL을 가져옴
        const response = await axios.get("http://192.168.0.32:8402/sampleImg", {
          params: { item: this.item },
        });
        this.imgUrl = response.data.data_from_first_app.result[this.item].img_url;
      } catch (error) {
        console.error("이미지 가져오기 오류:", error);
      }
    },

    /**
    * 드래그 시작 이벤트를 처리하는 함수
    *
    * @method
    * @param {DragEvent} event - 드래그 이벤트 객체
    * @param {String} url - 드래그할 이미지의 URL
    */
    handleDragStart(event, url) {
      event.dataTransfer.setData("text/plain", url);
    },

    /**
    * 이미지 클릭 이벤트를 처리하고, 부모 컴포넌트에 선택된 이미지의 URL을 전달
    *
    * @method
    * @param {String} url - 클릭한 이미지의 URL
    * @param {Event} event - 클릭 이벤트 객체
    * @emits sampleImage - 선택된 이미지의 URL을 부모 컴포넌트(MainPage.vue)로 전송
    * @emits imageUrl - null을 부모 컴포넌트(MainPage.vue)로 전송하여 현재 이미지 URL을 초기화
    */
    handleImage(url, event) {
      this.$emit('sampleImage', url);
      this.$emit('imageUrl', null);
    },
  },
};
</script>
  
<style scoped>
.sample-image {
  object-fit: cover;
  max-width: calc(30% - 55px);
  max-height: 150px;
  width: 100%;
  border-radius: 20px;
  border: 2px solid #e7e6e6;
}
</style>