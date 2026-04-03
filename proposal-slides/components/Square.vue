<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps({
  square: {
    default: "blue-square.svg",
  },
})

// Use a computed so the URL reactively updates whenever props.square changes.
// The original code did `let square = props.square` (a plain variable copy)
// and closed over that in getFileName() — so it never reflected prop updates.
const src = computed(() => new URL("../figures/" + props.square, import.meta.url).href)
</script>

<template>
  <img style="top:0;left:0" width="30px" :src="src">
</template>
