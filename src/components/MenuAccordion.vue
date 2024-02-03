<template>
  <!-- category 속성 -->
  <button
    @click="toggleAccordion"
    class="text-gray-800 bg-transparent hover:bg-gray-200 w-full flex text-left rounded-md box-border p-3"
    :aria-expanded="isOpen"
    :aria-controls="`collapse${_uid}`"
    :class="{
      'bg-gray-200': isOpen,
      'bg-transparent': !isOpen,
    }"
  >
    <!-- 아코디언 제목 슬롯 -->
    <span class="mr-30 text-xl"></span>
    <span class="w-full">
      <slot name="title" />
    </span>
    <!-- 아코디언 아이콘 -->
    <span
      class="box-border mt-1 text-gray-500"
      :class="{
        'rotate-180': isOpen,
        'rotate-0': !isOpen,
      }"
    >
      <span class="float-right">
        <Icon icon="fa6-solid:angle-down" />
      </span>
    </span>
  </button>

<!-- sub_category 속성 -->
<div
  @click="toggleAccordion"
  class="text-gray-800 rounded-md p-2"
  v-show="isOpen"
  :id="`collapse${_uid}`"
  :style="{ width: isOpen ? '105%' : 'auto' }"
>
  <slot name="content" />
</div>

</template>

<script>
import { Icon } from "@iconify/vue";

/**
 * Accordion 컴포넌트
 *
 * @component
 * @prop {Boolean} open - 초기에 아코디언이 열려있는지 여부를 나타내는 prop
 * @data {Boolean} isOpen - 아코디언의 현재 열림/닫힘 상태를 관리하는 데이터
 * @method toggleAccordion - 아코디언을 토글하는 메서드
 * @component Icon - 아이콘 컴포넌트
 */
export default {
  props: {
    open: Boolean,
  },
  data() {
    return {
      isOpen: this.open,
    };
  },

  methods: {
    toggleAccordion() {
      this.isOpen = !this.isOpen;
    },
  },
  components: {
    Icon,
  },
};
</script>
