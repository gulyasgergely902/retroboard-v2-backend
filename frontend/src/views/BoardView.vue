<template>
  <masonry-wall :items="items" :ssr-columns="1" :column-width="300" :gap="16">
    <template #default="{ item, index }">
      <div class="bg-sky-200 rounded-xl p-4">
        <span>{{ item }}</span>
      </div>
    </template>
  </masonry-wall>
</template>

<script setup lang="ts">
import MasonryWall from '@yeger/vue-masonry-wall'
import { onMounted, ref } from 'vue'
const items = [
  'Cras sagittis, tellus sit amet sagittis rhoncus, metus lectus fringilla enim, a consectetur ante lorem a tortor. Maecenas tincidunt nec augue a aliquet.',
  'Nunc sit amet nunc rhoncus.',
  'Nam nec arcu est. Nullam pulvinar ligula ac massa consequat, a tincidunt est condimentum. Aliquam egestas vehicula risus, a interdum diam lobortis ultrices. Phasellus eget pretium quam.',
  'Etiam dolor lacus, sodales semper porta sit amet, gida nec tortor.',
  'Nulla lobortis, felis eleifend tempor maximus, leo mi sagittis sem, a eleifend leo orci eu ex. Phasellus fringilla quam quis tempor tempor. Sed sit amet enim ut dui interdum semper.',
  'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In gravida eleifend libero, ac dapibus urna posuere eu. Ut id eros facilisis turpis consequat luctus a sed metus. Cras sagittis, tellus sit amet sagittis rhoncus, metus lectus fringilla enim, a consectetur ante lorem a tortor.',
  'Lorem ipsum.',
  'Nulla lobortis, felis eleifend tempor maximus, leo mi sagittis sem, a eleifend leo orci eu ex.',
  'Cras sagittis, tellus sit amet sagitt  is rhoncus, metus lectus fringilla enim, a consectetur ante lorem a tortor.',
]
const loading = ref(false)
const boards = ref(null)

onMounted(async () => {
  console.log('Mounted')
  try {
    console.log('Fetching boards...')
    loading.value = true
    const response = await fetch('/api/boards')
    if (!response.ok) throw new Error('Network response was not ok')
    const returnData = await response.json()
    console.log('Boards fetched:', returnData)
    boards.value = returnData
  } catch (err) {
    console.error('Error fetching boards:', err)
  } finally {
    loading.value = false
  }
})
</script>
