<script setup lang="ts">
import { computed } from 'vue'
import { useNav } from '@slidev/client'

const props = defineProps({
  squares: {
    default: '{"sq":"blue-square.svg", "ind":"0"}',
  },
})

// Slidev's reactive click counter for the current slide.
// Using this instead of v-click directives avoids the static analysis
// problem: Slidev cannot count dynamic v-click bindings inside v-for loops
// in child components, which causes it to mis-set $clicks.total and render
// every square simultaneously on first load.
const { clicks } = useNav()

const parsedSquares = computed(() =>
  props.squares.split(';').map(s => JSON.parse(s))
)

// Show the last square whose `ind` value is <= the current click count.
// This replaces the v-click / v-click.hide chain that was previously
// generating one <Square> per state with dynamic show/hide directives.
const currentSquare = computed(() => {
  const current = clicks.current
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
