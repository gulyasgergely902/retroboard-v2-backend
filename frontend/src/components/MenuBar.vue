<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>
<template>
  <nav class="bg-white border-gray-200 dark:bg-slate-900">
    <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
      <RouterLink to="/" class="flex items-center space-x-3 rtl:space-x-reverse">
        <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-slate-50"
          >RetroBoard</span
        >
      </RouterLink>
    </div>
  </nav>
</template>
