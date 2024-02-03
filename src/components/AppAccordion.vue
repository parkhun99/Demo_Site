<template>
  <!-- 아코디언 버튼과 콘텐츠를 나타내는 Vue 컴포넌트 -->
  <button
    @click="toggleAccordion()"
    class="text-gray-800 transition-all bg-transparent border hover:bg-gray-200 w-full flex text-left rounded-md box-border p-3"
    :aria-expanded="isOpen"
    :aria-controls="`collapse${uid}`"
    :class="{
      'bg-gray-200': isOpen,
      'bg-transparent': !isOpen,
    }"
  >
    <span
      class="box-border mt-1 text-gray-500"
      :class="{
        'rotate-180': isOpen,
        'rotate-0': !isOpen,
      }"
    >
      <span class="float-right">
        <!-- Font Awesome의 angle-down 아이콘 -->
        <Icon icon="fa6-solid:angle-down" />
      </span>
    </span>
  </button>

  <div
    v-show="isOpen"
    :id="uid"
    class="p-3 mt-2 bg-gray-100"
  >
  </div>
</template>

<script>
  let _uid = 0;
  /**
   * 아코디언 버튼과 콘텐츠를 나타내는 Vue 컴포넌트
   * @component
   * 
   */
  export default {
    data() {
      _uid += 1;
      return {
        isOpen: false,
        uid: `collapse${_uid}`,
      };
    },
    
    methods: {
      /**
       * 아코디언의 열림/닫힘 상태를 토글
       * @method
       */
      toggleAccordion() {
        this.isOpen = !this.isOpen;
      },

      /**
       * 메뉴 항목 클릭 이벤트를 처리합니다.
       * @method
       * @param {string} category - category.
       * @param {string} item - sub_category.
       * @emits data-clicked - sidebar.vue 전송
       */
      handleMenuItemClicked(category, item) {
        this.$emit('data-clicked', { category, item });
      },
    },
  };
</script>