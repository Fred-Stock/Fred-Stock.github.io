<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps({
  hex: {
    default: 'red-hex.svg',
  },
})

// Reactive src — same pattern as Square.vue
const src = computed(() => new URL('../figures/' + props.hex, import.meta.url).href)
</script>

<template>
  <!-- 52x60 matches the pointy-top hex SVG dimensions -->
  <img style="position:absolute;top:0;left:0" width="50px" height="58px" :src="src">
</template>
