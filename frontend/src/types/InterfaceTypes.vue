<script lang="ts">
export interface Note {
  id: number
  description: string
  category: number
  tags: string[]
}

export interface Category {
  id: number
  name: string
}
</script>
