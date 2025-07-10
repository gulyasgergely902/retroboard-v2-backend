<template>
  <filter-toggle @update:selectedIndex="handleSelection" class="mb-4" :categories="categories" />
  <masonry-wall :items="filteredNotes" :ssr-columns="1" :column-width="300" :gap="16" class="p-4">
    <template #default="{ item, index }">
      <div class="bg-sky-500 rounded-xl p-4">
        <span>{{ item.description }}</span>
      </div>
    </template>
  </masonry-wall>
</template>

<script setup lang="ts">
import MasonryWall from '@yeger/vue-masonry-wall'
import { onMounted, ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import FilterToggle from '@/components/FilterToggle.vue'

import type { Note, Category } from '@/types/InterfaceTypes.vue'

const notes = ref<Note[]>([])
const categories = ref<Category[]>([])

const loading = ref(false)

const route = useRoute()
const boardId = route.params.id as string

const selectedCategory = ref<number | null>(null)

onMounted(async () => {
  try {
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

    const categoriesData = (await cateries_response.json()) as Category[]
    categories.value = categoriesData

    notes.value = (await notes_response.json()) as Note[]
  } catch (err) {
    console.error('Error fetching notes:', err)
  } finally {
    loading.value = false
  }
})

const filteredNotes = computed(() => {
  if (selectedCategory.value === null)
    return notes.value.filter((n) => n.category === categories.value[0].id)

  return notes.value.filter((n) => n.category === selectedCategory.value)
})

function handleSelection(index: number) {
  selectedCategory.value = index
}
</script>
