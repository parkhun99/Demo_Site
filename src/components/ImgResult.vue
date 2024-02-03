<template>
  <div class="card-page p-3" style="margin-left: -10px;">
    <!-- 파일 업로드 Section -->
    <div class="grid grid-cols-2 mt-9 gap-10">
      <div class="card p-2 bg-white" style="border: 2px solid #e7e6e6; border-radius: 20px;">
        <h2 class="text-font">Choose a file</h2>
        <div class="wrapper-button mt-2">
          <!-- 파일 업로드를 위한 입력 필드 -->
          <input ref="fileInput" type="file" @change="handleImageUpload" accept="image/*" style="border: 2px solid #ccc; padding: 3px; width: 100%; margin-bottom: -10px; font-size: small;">
          <!-- 드랍 이미지 Section -->
          <div @dragover.prevent @drop="handleDrop" class="bg-gray-50" style="height: 270px; margin-top: 20px; border-radius: 20px; border: 2px dashed #cccccc; text-align: center; display: flex; flex-direction: column; justify-content: center;">
            <text v-if="!(uploadedImage || droppedImageUrl || imageUrl || sampleUrl)" class="text-font" style="color: #999;">Image Drop</text>
            <!-- 업로드 또는 드랍된 이미지 표시 -->
            <img v-if="uploadedImage || droppedImageUrl" :src="uploadedImage || droppedImageUrl" alt="Uploaded/Dropped Image">
            <!-- 서브 메뉴에서 가져온 이미지 표시 -->
            <img v-else-if="imageUrl" :src="imageUrl" alt="결과 이미지" @load="logImageURL($event, 'uploadedImage')">
            <!-- 샘플 이미지에서 져온 이미지 표시 -->
            <img v-else-if="sampleUrl" :src="sampleUrl" alt="결과 이미지">
          </div>
        </div>
        <button class="box-button" @click="submitImage" style="margin-top: 15px;">이미지 전송</button>
      </div>
      <!-- 결과 Section -->
      <div class="card p-2 bg-white" style="border: 2px solid #e7e6e6; border-radius: 20px;">
        <h2 class="text-font">Result</h2>
        <div>
          <div class="bg-gray-50 center-image" style="height: 270px; margin-top: 55px; border-radius: 20px; border: 2px dashed #cccccc;">
            <!-- 로딩 중일 때 표시되는 스피너 -->
            <div v-if="isLoading" class="spinner-container">
              <div class="spinner"></div>
            </div>
            <!-- 결과 이미지 표시 -->
            <img v-else-if="resultImage" :src="resultImage" alt="Result Image" :key="Date.now()">
            <!-- 결과 텍스트가 있을 때 표시 -->
            <div v-if="resultText" style="display: block; margin: 0 auto; object-fit: contain; width: 100%; height: 100%; max-width: 100%; max-height: 100%; border-radius: 20px;">
              <img :src="uploadedImage" alt="Uploaded Image" v-if="uploadedImage">
            </div>            
          </div>
          <!-- 결과 텍스트 영역 -->
          <div class="bg-gray-50" style="height: 40px; margin-top: 15px; border-radius: 10px; border: 2px solid #e7e6e6;">
            <div class="result-text" v-if="resultText">
              텍스트 내용 : {{ Array.isArray(resultText) ? resultText.join(' ') : resultText }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/**
 * Axios와 MenuAccordion 컴포넌트를 가져오는 스크립트
 *
 * @module
 * @requires axios
 * @requires MenuAccordion
 */
import axios from "axios";
import MenuAccordion from "./MenuAccordion.vue";

/**
 * 이미지 결과를 표시하는 컴포넌트
 *
 * @component
 */
export default {
  /**
  * @typedef {Object} ModelPageProps
  * @property {String} imageUrl - 모델 이미지 URL
  * @property {String} sampleUrl - 샘플 이미지 URL
  */
  // 부모 컴포넌트에서 전달받은 이미지 및 샘플 이미지의 URL을 속성으로 정의
  props: {
    imageUrl: String,
    sampleUrl: String,
  },

  // 자식 컴포넌트로 MenuAccordion을 등록
  components: { 
    MenuAccordion,
  },

  /**
  * 컴포넌트의 데이터 상태를 나타내는 객체
  *
  * @typedef {Object} ComponentData
  * @property {String|null} uploadedImage - 업로드된 이미지 URL
  * @property {String|null} resultImage - 결과 이미지 URL
  * @property {String|null} resultText - 결과 텍스트
  * @property {Array} data_list - 데이터 리스트
  * @property {String|null} category - 현재 모델의 카테고리
  * @property {String|null} sub_category - 현재 모델의 서브 카테고리
  * @property {Number|null} port - 모델의 포트 번호
  * @property {String} droppedImageUrl - 드롭된 이미지 URL
  * @property {Boolean} showImage - 이미지 표시 여부
  * @property {Boolean} isLoading - 데이터 로딩 상태
  */
  data() {
    return {
      uploadedImage: null,
      resultImage: null,
      resultText: null,
      data_list: [],
      category: null,
      sub_category: null,
      port: null,
      droppedImageUrl: '',
      showImage: true,
      isLoading: false,
    };
  },
  watch: {
    /**
     * sampleUrl 프로퍼티의 변경을 감지하여 로컬 상태에 반영
     *
     * @event
     * @param {String} newSampleUrl - 새로운 샘플 이미지의 URL.
     * @param {String} oldSampleUrl - 이전 샘플 이미지의 URL.
     */
    sampleUrl: function(newSampleUrl, oldSampleUrl) {
    this.uploadedImage = newSampleUrl;
    this.droppedImageUrl = null;
    this.resultImage = null;
    this.resultText = null;
    this.$emit('sampleImage', newSampleUrl);
  },
    /**
     * 라우트 변경을 감지하여 상태를 초기화
     *
     * @event
     * @param {Object} to - 이동할 라우트 객체.
     * @param {Object} from - 현재 라우트 객체.
     */
    $route(to, from) {
      this.resetState();
    },
  },

  /**
     * 컴포넌트 생성 시 실행
     */
  created() {
    this.initComponent();
    
  },
  methods: {
     /**
     * 이미지 URL을 로깅
     *
     * @method
     * @param {Event} event - 이미지 로드 이벤트
     * @param {String} target - 로깅할 대상 (uploadedImage)
     * uploadedImage에 할당하는 로직 추가
     */
    logImageURL(event, target) {
      if (target === 'uploadedImage') {
        this.uploadedImage = event.target.src;
      }
    },

    /**
     * 컴포넌트를 초기화하는 메서드
     *
     * 라우트 쿼리 파라미터에서 카테고리와 서브 카테고리 정보를 가져와 설정하며,
     * 모델타입 엔드포인트에 POST 요청을 보내 포트 정보를 설정
     *
     * @method
     */
    initComponent() {
      this.category = this.$route.query.category;
      this.sub_category = this.$route.query.item;
      this.modelType_post();
    },

    /**
    * 컴포넌트 상태를 초기화하는 메서드
    *
    * @method
    * 현재 컴포넌트의 상태를 초기화. 초기화되는 상태는 다음과 같습니다:
    * sub_category: 현재 라우트 쿼리 파라미터에서 가져온 아이템 정보
    * uploadedImage: 업로드된 이미지
    * droppedImageUrl: 드롭된 이미지 URL
    * resultImage: 결과 이미지
    * resultText: 결과 텍스트
    * data_list: 데이터 리스트
    * $refs.fileInput.value: 파일 입력 필드의 값 (null로 설정)
    */
    resetState() {
      this.sub_category = this.$route.query.item;
      this.uploadedImage = null;
      this.droppedImageUrl = null;
      this.resultImage = null;
      this.resultText = null;
      this.data_list = [];
      this.$refs.fileInput.value = null;
    },

    /**
    * 파일 선택 이벤트에 대한 이미지 업로드를 처리하는 메서드
    *
    * @method
    * @param {Event} event - 파일 선택 이벤트.
    *   파일 선택 이벤트에서 전달된 파일을 사용하여 이미지 업로드를 수행
    *   파일이 선택되면 해당 파일의 URL을 생성하여 `uploadedImage`에 할당
    *   기존에 설정된 `droppedImageUrl`, `data_list`, `resultImage`, `resultText` 등의 상태를 초기화
    */
    async handleImageUpload(event) {
      const file = event.target.files[0];
      this.uploadedImage = file ? URL.createObjectURL(file) : null;
      this.droppedImageUrl = '';
      this.data_list = [];
      this.resultImage = null;
      this.resultText = null;
    },

    /**
    * 모델타입 엔드포인트에 POST 요청을 보내고, 서버로부터 받은 응답을 처리하는 메서드
    *
    * @method
    * 이 메서드는 현재 페이지의 모델 카테고리 및 서브 카테고리 정보를 사용하여
    * http://192.168.0.32:8402/modelType 엔드포인트에 POST 요청을 전송
    * 서버로부터 받은 응답에서 포트 정보를 추출하여 컴포넌트의 상태로 설정
    * if 응답이 성공적으로 수신되지 않으면 콘솔에 오류 메시지를 출력
    */
    async modelType_post() {
      try {
        const response = await axios.post("http://192.168.0.32:8402/modelType", {
          category: this.category,
          sub_category: this.sub_category,
        });

        // 서버 응답에서 포트 정보 추출
        this.port = response?.data?.data_from_first_app?.result?.port || null;
      } catch (error) {
        console.error("POST 요청 전송 중 오류:", error);
      }
    },

    /**
    * 이미지를 전송하고 서버 응답 데이터를 처리하는 메서드
    *
    * @method
    *   이 메서드는 업로드된 이미지가 있는 경우에만 실행
    *   이미지 전송 처리를 시작할 때 isLoading을 true로 설정
    *   업로드된 이미지를 Base64로 변환하여 데이터 리스트에 추가
    *   그 후 http://192.168.0.32:8402/inference 엔드포인트에 POST 요청을 전송
    *   서버로부터 받은 응답을 처리. 마지막으로 이미지 전송 처리가 완료되면
    *   isLoading을 false로 설정
    *
    * @throws {Error} - 이미지 전송 또는 서버 응답 처리 중 오류가 발생한 경우 에러를 던집니다.
    */
    async submitImage() {
      if (this.uploadedImage) {
        try {
          this.isLoading = true;
          const imageToSend = this.uploadedImage;
          const imageBase64 = await this.convertImageToBase64(imageToSend);
          const newDataList = [imageBase64];  
          const response = await axios.post("http://192.168.0.32:8402/inference", {
            category: this.category,
            sub_category: this.sub_category,
            port: this.port,
            data_list: newDataList,
          });
          this.handleResponseData(response.data.data_from_first_app);
        } catch (error) {
          console.error(error);
        } finally {
          this.isLoading = false;
        }
      }
    },

    /**
    * 이미지 URL을 받아와 해당 이미지를 Base64로 변환하는 메서드
    *
    * @method
    * @param {String} url - 이미지 URL
    * @returns {Promise<String>} - 변환된 이미지의 Base64 데이터를 담은 Promise 객체
    * @throws {Error} - 이미지 로드나 변환 중 오류가 발생하면 에러를 던집니다.
    */
    convertImageToBase64(url) {
      return new Promise((resolve) => {
        const img = new Image();
        img.crossOrigin = "Anonymous";
        img.onload = function () {
          const canvas = document.createElement("canvas");
          canvas.width = img.width;
          canvas.height = img.height;
          const ctx = canvas.getContext("2d");
          ctx.drawImage(img, 0, 0, img.width, img.height);
          const dataURL = canvas.toDataURL("image/jpeg").split(",")[1];
          resolve(dataURL);
        };
        img.src = url;
      });
    },
    
    /**
     * 결과 이미지를 표시
     *
     * @method
     * @param {String} base64Data - 결과 이미지의 Base64 데이터
     */
    displayImage(base64Data) {
      this.resultImage = "data:image/jpeg;base64," + base64Data;
    },
    
    /**
    * 사용자 정의 솔루션 페이지를 새 창으로 엽니다.
    *
    * @method
    * @returns {void}
    */
    openCustomSolutionPage() {
      window.open("https://www.m47rix.com/21", "_blank");
    },
    
    /**
     * 드롭 이벤트를 처리
     *
     * @method
     * @param {Event} event - 드롭 이벤트
     */
    handleDrop(event) {
      // 드롭 이벤트 기본 동작 방지
      event.preventDefault();
      // 드롭된 이미지 URL 가져오기
      this.droppedImageUrl = event.dataTransfer.getData('text/plain');
      // 업로드된 이미지 및 결과 초기화
      this.uploadedImage = this.droppedImageUrl;
      this.droppedImageUrl = null;
      this.resultImage = null;
      this.resultText = null;
    },
    
    /**
     * 서버 응답 데이터를 처리
     *
     * @method
     * @param {Object} data - 서버 응답 데이터
     */
    handleResponseData(data) {
      if (data.result_img && data.result_text) {
        this.displayImage(data.result_img);
        this.resultText = data.result_text;
      } else if (data.result_img) {
        this.displayImage(data.result_img);
        this.resultText = null;
      } else if (data.result_text) {
        this.resultImage = null;
        this.resultText = data.result_text;
      }
    },
  },
};
</script>

<style scoped>
.text-font {
  font-weight: 600;
  font-size: 15px;
  color: #3d4554; /* gray-700에 해당하는 색상 코드 */
}
.result-text {
  font-size: 20px;
  color: #606060;
  font-weight: bold;
  margin-top: 10px;
  padding-left: 20px;
}
/* 전송 버튼 스타일 */
.box-button {
  display: block;
  margin: 0 auto;
  padding: 6px 30px;
  background-color: white;
  color: #606060;
  border: none;
  border-radius: 15px;
  cursor: pointer;
  font-size: 13px;
  transition: background-color 0.3s ease-in-out, color 0.3s ease-in-out;
  font-weight: bold;
  border: 4px solid #808182;
  box-sizing: border-box;
  width: auto;
}
.box-button:hover {
  background-color: #808182;
  color: white;
}
.center-image img,
.wrapper-button img {
  display: block;
  margin: 0 auto;
  object-fit: contain;
  width: 100%;
  height: 100%;
  max-width: 100%;
  max-height: 100%;
  border-radius: 20px;
}
/* 그리드 레이아웃 및 미디어 쿼리 */
.grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  max-width: 800px;
  height: 340px;
}
@media (max-width: 600px) {
  .grid {
    grid-template-columns: repeat(1, 1fr);
    max-width: 600px;
    gap: 20px;
    margin-bottom: 480px;
  }
}
.spinner-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%; /* 부모 컨테이너의 높이에 따라 조절 */
}
.spinner {
  border: 4px solid rgba(0, 0, 0, 0.1);
  border-top: 4px solid #3498db;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  animation: spin 1s linear infinite;
}
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
