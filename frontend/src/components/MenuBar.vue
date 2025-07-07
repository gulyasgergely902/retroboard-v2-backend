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
      <div class="block w-auto" id="navbar-default">
        <ul
          class="font-medium flex flex-row p-0 mt-0 rounded-lg space-x-4 bg-white dark:bg-slate-800"
        >
          <li>
            <RouterLink
              to="/"
              class="block py-2 text-slate-950 hover:text-sky-500 rounded-sm bg-transparent dark:text-slate-50 transition-colors"
              >Home</RouterLink
            >
          </li>
          <li>
            <RouterLink
              to="/board"
              class="block py-2 text-slate-950 hover:text-sky-500 rounded-sm bg-transparent dark:text-slate-50 transition-colors"
              >About</RouterLink
            >
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>
