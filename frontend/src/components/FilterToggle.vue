<template>
  <div class="w-full max-w-md mx-auto">
    <div class="relative flex bg-gray-200 rounded-full">
      <!-- Sliding background -->
      <div
        class="absolute top-1 bottom-1 left-1 bg-white rounded-full shadow transition-all h-8 duration-300 ease-in-out"
        :style="{
          width: `${100 / categories.length}%`,
          transform: `translateX(${selectedIndex * 100}%)`,
        }"
      ></div>

      <button
        v-for="(category, index) in categories"
        :key="category.id"
        class="relative z-10 flex-1 text-center rounded-full h-10 flex items-center justify-center font-semibold transition-colors duration-200"
        :class="selectedIndex === index ? 'text-black' : 'text-gray-500'"
        @click="selectOption(index)"
      >
        {{ category.name }}
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { defineProps } from 'vue'
defineProps(['categories'])
const selectedIndex = ref(0)

const emit = defineEmits<{
  (e: 'update:selectedIndex', index: number): void
}>()

const selectOption = (index: number) => {
  selectedIndex.value = index
  emit('update:selectedIndex', index)
}
</script>
