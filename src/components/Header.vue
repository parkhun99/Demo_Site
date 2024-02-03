<template>
  <!-- 사이드바 인, 아웃 버튼 -->
  <div>
    <button
      class="text-gray-500 lg:hidden block"
      @click="$emit('sidebarToggle', true)"
      :class="{ 'bg-gray-50': isMainPage, 'bg-white': !isMainPage }"
      :style="{ width: '100%' }"
    >
      <!-- 아이콘 등의 내용은 그대로 유지 -->
      <svg
        xmlns="http://www.w3.org/2000/svg"
        aria-hidden="true"
        role="img"
        width="2em"
        height="2em"
        preserveAspectRatio="xMidYMid meet"
        viewBox="0 0 16 16"
      >
        <path
          fill="none"
          stroke="currentColor"
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="1.5"
          d="M2.75 12.25h10.5m-10.5-4h10.5m-10.5-4h10.5"
        />
      </svg>
    </button>
  </div>
</template>

<script>
export default {
  props: {
    isMainPage: Boolean, // MainPage 여부를 부모 컴포넌트로부터 받아옴
  },
};
</script>