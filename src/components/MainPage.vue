<template>
  <div class="card-page lg:h-screen h-auto p-10 flex flex-col items-center">
    <!-- 로고 Section -->
    <div class="logo-container">
      <img src="@/assets/logo/Matrix_Most.png" alt="Your Logo" style="max-width: 1000px; width: 100%; height: auto; margin-bottom: 5%;" />
    </div>
    <!-- 모델 텍스트 Section -->
    <div class="model-text-container flex items-center">
      <div class="gray-line flex-grow"></div> 
      <h1 class="text-3xl text-gray-700 font-bold" style="white-space: nowrap; padding-left: 1%;">All Models</h1>
      <div class="gray-line flex-grow"></div>
    </div>
    <!-- 모델 그리드 Section -->
    <div class="grid-container w-1/2 justify-center">
      <div class="square-box" v-for="(item, index) in imageData" :key="index">
        <div class="thumbnail_img" v-if="item.thumnail_url" @click="navigateToCategory(item.category_type, item.subcategory_type)">
          <img :src="item.thumnail_url" :alt="'Thumbnail Image - ' + item.subcategory_type" style="object-fit: cover; width: 100%; height: 180px">
          <h2 class="text_font">{{ item.subcategory_type }}</h2>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  /**
  * 컴포넌트 데이터 초기 상태를 정의하는 객체
  *
  * @function
  * @returns {Object} - 초기 데이터 객체
  * @property {Array} imageData - 이미지 데이터를 담는 배열
  * @property {number} gridColumns - 초기 그리드 컬럼 수
  */
  data() {
    return {
      imageData: [],
      gridColumns: 6,
    };
  },

  /**
  * 컴포넌트가 생성될 때 초기 설정을 수행하는 메서드
  *
  * @method
  * @returns {void}
  * @fires sendGetRequest - 서버에 GET 요청을 보내는 함수를 호출
  * @fires adjustGridColumns - 페이지 로드 시 그리드 컬럼 수를 설정하는 함수를 호출
  */
  created() {
    this.sendGetRequest();
    this.adjustGridColumns();
  },

  /**
  * 그리드 클래스를 반환하는 계산된 속성
  *
  * @computed
  * @type {String} - 그리드 클래스를 나타내는 문자열
  */
  computed: {
    gridClass() {
      return `grid grid-cols-${this.gridColumns} mt-10 gap-20`;
    },
  },
  
  /**
  * 컴포넌트가 마운트된 후 창 크기 변경 이벤트에 대한 리스너를 추가
  *
  * @method
  * @returns {void} - 창 크기 변경 이벤트 리스너를 추가
  */
  mounted() {
    window.addEventListener('resize', this.adjustGridColumns);
  },

  /**
  * 컴포넌트가 파괴되기 전에 창 크기 변경 이벤트에 대한 리스너를 제거
  *
  * @method
  * @returns {void} - 창 크기 변경 이벤트 리스너를 제거
  */
  beforeDestroy() {
    window.removeEventListener('resize', this.adjustGridColumns);
  },

  methods: {
    /**
    * 서버에 GET 요청을 보내고 응답 데이터를 처리하는 비동기 함수
    *
    * @async
    * @method
    * @throws {Error} GET 요청이 실패한 경우 에러를 던집니다.
    * @returns {Promise<void>} - Promise 반환하며, 성공적으로 데이터를 받아온 경우 imageData 상태를 업데이트
    */
    async sendGetRequest() {
      try {
        const response = await fetch('http://192.168.0.32:8402/modelCategory', {
          method: 'GET',
        });
        if (!response.ok) {
          throw new Error('GET 요청이 실패했습니다');
        }
        const data = await response.json();
        this.imageData = data.data_from_first_app.result;
      } catch (error) {
          console.error('에러:', error);
      }
    },

    /**
    * 주어진 카테고리와 서브카테고리 정보를 이용하여 모델 데모 페이지로 이동하는 함수
    *
    * @method
    * @param {String} category - 이동할 페이지의 모델 카테고리 정보
    * @param {String} subcategory - 이동할 페이지의 모델 서브 카테고리 정보
    * @returns {void} - 현재 창의 URL을 갱신하여 모델 데모 페이지로 이동
    */
    navigateToCategory(category, subcategory) {
      const pageParameter = `category=${category}&item=${subcategory}`;
      const fixedLink = 'http://192.168.0.32:8406/components/ModelDemo';
      const finalLink = `${fixedLink}?${pageParameter}`;
      window.location.href = finalLink;
    },

    /**
    * 창의 너비에 따라 그리드 컬럼 수를 동적으로 조정하는 함수
    *
    * @method
    * @returns {void} - 현재 창의 너비에 따라 그리드 컬럼 수를 조정
    */
    adjustGridColumns() {
      if (window.innerWidth < 768) {
        this.gridColumns = 1;
      } else if (window.innerWidth < 1200) {
        this.gridColumns = 2;
      } 
      else if (window.innerWidth < 1400) {
        this.gridColumns = 3;
      }else {
        this.gridColumns = 6;
      }
    },
  },
};
</script>

<style scoped>
.square-box {
  border-radius: 20px;
  margin-left: 40px;
  margin-bottom: 80px;
  overflow: hidden;
  height: 230px;
  cursor: pointer;
  border: 2px solid #ececec;
  box-sizing: border-box;
}
.thumbnail_img {
  position: relative;
}
.thumbnail_img img {
  object-fit: cover;
  width: 100%;
  height: 180px;
  transition: filter 0.3s ease;
  transition: transform 0.8s ease;
  border-bottom: 2px solid #e7e6e6;
}
.thumbnail_img:hover img {
  transform: scale(1.6);
}
.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 20px;
    padding-right: 2%;
  }
  @media (min-width: 768px) {
    .grid-container {
      grid-template-columns: repeat(2, minmax(300px, 1fr));
    }
  }
  @media (min-width: 1300px) {
    .grid-container {
      grid-template-columns: repeat(3, minmax(300px, 1fr));
    }
  }
  @media (min-width: 1700px) {
    .grid-container {
      grid-template-columns: repeat(4, minmax(300px, 1fr));
    }
  }
  @media (min-width: 2000px) {
    .grid-container {
      grid-template-columns: repeat(5, minmax(300px, 1fr));
    }
  }
  @media (min-width: 2300px) {
    .grid-container {
      grid-template-columns: repeat(6, minmax(300px, 1fr));
    }
  }
  .logo-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 20px;
  }
  .text_font {
    text-align: center;
    margin-top: 10px;
    font-size: 16px;
    font-weight: 500;
    color: #404041;
  }
  .model-text-container {
    text-align: center;
    margin-bottom: 25px;
    font-weight: bold;
    font-style: italic;
    font-size: 18px;
  }
  .gray-line {
    width: 550px;
    height: 3px;
    background-color: #e7e6e6;
    margin-left: 15px;
  }
</style>