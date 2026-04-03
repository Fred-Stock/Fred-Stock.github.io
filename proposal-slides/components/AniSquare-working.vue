<script setup lang="ts">
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

const props = defineProps({
  squares: {
    default: '{"sq":"blue-square.svg", "ind":"0"}',
  },
})

// useSlideContext() provides $clicks scoped to the current slide, which is
// reactive — it updates as the user clicks through. useNav() is global and
// does not update per-slide click state, which is why the previous version
// rendered correctly on first load but didn't respond to clicks.
const { $clicks } = useSlideContext()

const parsedSquares = computed(() =>
  props.squares.split(';').map(s => JSON.parse(s))
)

// Show the last square whose `ind` value is <= the current click count.
const currentSquare = computed(() => {
  const current = $clicks.value
  let result = parsedSquares.value[0]
  for (const sq of parsedSquares.value) {
    if (Number(sq.ind) <= current) {
      result = sq
    }  
  }
  return result
})
</script>

<template>
  <Square :square="currentSquare.sq" />
</template>
