<template>
  <filter-toggle @update:selectedIndex="handleSelection" class="mb-4" :categories="categories" />
  <masonry-wall :items="notes" :ssr-columns="1" :column-width="300" :gap="16" class="p-4">
    <template #default="{ item, index }">
      <div class="bg-sky-500 rounded-xl p-4">
        <span>{{ item.description }}</span>
      </div>
    </template>
  </masonry-wall>
</template>

<script setup lang="ts">
import MasonryWall from '@yeger/vue-masonry-wall'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import FilterToggle from '@/components/FilterToggle.vue'

interface Note {
  id: number
  description: string
  category: string
  tags: string[]
}

interface Category {
  id: number
  name: string
}

const notes = ref<Note[]>([])
const categories = ref<Category[]>([])

const loading = ref(false)

const route = useRoute()
const boardId = route.params.id as string

const selectedFilterIndex = ref(0)

onMounted(async () => {
  try {
    console.log('Fetching notes & categories...')
    loading.value = true
    const notes_response = await fetch('/api/notes?board_id=' + boardId)
    const cateries_response = await fetch('/api/categories?board_id=' + boardId)

    if (!notes_response.ok) {
      const resp = await notes_response.text()
      console.error('Error response:', resp)
      throw new Error('Network response was not ok: ' + notes_response.statusText)
    }

    if (!cateries_response.ok) {
      const resp = await cateries_response.text()
      console.error('Error response:', resp)
      throw new Error('Network response was not ok: ' + cateries_response.statusText)
    }

    const notesData = (await notes_response.json()) as Note[]
    notes.value = notesData
    const categoriesData = (await cateries_response.json()) as Category[]
    categories.value = categoriesData
  } catch (err) {
    console.error('Error fetching notes:', err)
  } finally {
    loading.value = false
  }
})

function handleSelection(index: number) {
  selectedFilterIndex.value = index
  console.log('Selected:', index)
}
</script>
