<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps({
  square: {
    default: "../figures/blue-square.svg",
  },
  // transitions: {
  //   default: [],
  // },
})

let square = (props.square);

function getFileName(){
  return new URL("../figures/" + square, import.meta.url);
}

function changeSquare(newPath){
  square = newPath;
}

const output = getFileName();

// const transitions = ref(props.transitions);
</script> 

<template>
  <!-- {{getFileName()}} -->
  <img style="position:absolute,top:0,left:0" width="30px" :src="getFileName()">

</template>
