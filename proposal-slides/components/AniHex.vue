<script setup lang="ts">
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

// Same prop interface as AniSquare — "sq" values are hex SVG filenames
// e.g. squares='{"sq":"red-hex.svg","ind":"0"};{"sq":"yellow-hex.svg","ind":"2"}'
const props = defineProps({
  squares: {
    default: '{"sq":"red-hex.svg","ind":"0"}',
  },
})

const { $clicks } = useSlideContext()

const parsedSquares = computed(() =>
  props.squares.split(';').map(s => JSON.parse(s))
)

const currentHex = computed(() => {
  const current = $clicks.value
  let result = parsedSquares.value[0]
  for (const sq of parsedSquares.value) {
    if (Number(sq.ind) <= current) result = sq
  }
  return result
})
</script>

<template>
  <!--
    52x60 matches the pointy-top hex tile dimensions.
    position:relative gives the absolutely-positioned Hex image an anchor.
    The parent layout is responsible for the -15px row overlap that makes
    pointy-top hexes tile tightly (see the slide snippet below).
  -->
  <div style="position:relative; width:52px; height:60px; flex-shrink:0;">
    <Transition name="hex-swap">
      <Hex :key="currentHex.sq" :hex="currentHex.sq" />
    </Transition>
  </div>
</template>

<style scoped>
/* Old hex shrinks to a point; new hex is already visible behind it */
.hex-swap-enter-active {
  transition: none;
  position: absolute;
  top: 0; left: 0;
}
.hex-swap-leave-active {
  transition: transform 0.5s ease-in, opacity 0.5s ease-in;
  position: absolute;
  top: 0; left: 0;
  z-index: 1;
}
.hex-swap-leave-to {
  transform: scale(0);
  opacity: 0;
}
</style>
