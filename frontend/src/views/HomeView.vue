<template>
  <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 p-4">
    <BoardCard
      v-if="loading"
      v-for="n in 10"
      class="blur-sm grayscale brightness-150"
      title="Boards are loading..."
    />
    <BoardCard v-else v-for="board in boards" :title="board.name" />
  </div>
</template>

<script setup lang="ts">
import BoardCard from '@/components/BoardCard.vue'
import { onMounted, ref } from 'vue'

interface Board {
  id: number
  name: string
}

const boards = ref<Board[]>([])
const loading = ref(false)

onMounted(async () => {
  console.log('Mounted')
  try {
    console.log('Fetching boards...')
    loading.value = true
    const response = await fetch('/api/boards')
    console.log('Status:', response.status)

    if (!response.ok) {
      const resp = await response.text()
      console.error('Error response:', resp)
      throw new Error('Network response was not ok: ' + response.statusText)
    }

    const returnData = (await response.json()) as Board[]
    boards.value = returnData
  } catch (err) {
    console.error('Error fetching boards:', err)
  } finally {
    loading.value = false
  }
})
</script>
