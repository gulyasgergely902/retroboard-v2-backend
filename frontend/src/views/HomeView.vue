<template>
  <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 p-4">
    <BoardCard
      v-if="loading"
      v-for="n in 10"
      class="blur-sm grayscale brightness-150"
      title="Boards are loading..."
    />
    <RouterLink
      v-else
      v-for="board in boards"
      :to="{ name: 'board', params: { id: String(board.id) } }"
    >
      <BoardCard v-if="board.id" :title="board.name" />
      <BoardCard v-else class="grayscale" title="Board data is missing" />
    </RouterLink>
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
  try {
    loading.value = true
    const response = await fetch('/api/boards')

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
