<script setup lang="ts">
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

const props = defineProps({
  squares: {
    default: '{"sq":"blue-square.svg", "ind":"0"}',
  },
})

const { $clicks } = useSlideContext()

const parsedSquares = computed(() =>
  props.squares.split(';').map(s => JSON.parse(s))
)

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
  <div style="position:relative; width:30px; height:30px;">
    <Transition name="square-swap">
      <Square :key="currentSquare.sq" :square="currentSquare.sq" />
    </Transition>
  </div>
</template>

<style scoped>
/* The entering square appears instantly with no animation — it sits
   statically behind while the leaving square shrinks over it. */
.square-swap-enter-active {
  transition: none;
  position: absolute;
  top: 0;
  left: 0;
}
.square-swap-leave-active {
  transition: transform 0.5s ease-in, opacity 0.5s ease-in;
  position: absolute;
  top: 0;
  left: 0;
  /* Ensure the shrinking old square renders on top of the new one */
  z-index: 1;
}
.square-swap-leave-to {
  transform: scale(0);
  opacity: 0;
}
</style>