<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps({
  squarePath: {
    default: "../figures/blue-square.svg",
  },
  coords:{
    default:[],
  }
})

const square = ref(props.squarePath)

function getFileName(){
  return new URL("../figures/" + props.squarePath, import.meta.url);
}

const output = getFileName();
</script>

<template>
    
</template>
