<template>
  <div
    class="bg-sky-500 text-sky-950 hover:bg-sky-700 dark:bg-sky-950 dark:text-sky-50 transition-colors p-4 rounded-xl h-32"
  >
    {{ title }}
  </div>
</template>
<script setup lang="ts">
import { defineProps } from 'vue'
defineProps(['title', 'boardId'])
</script>
