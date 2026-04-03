<script setup>
import {ref} from 'vue'

const props = defineProps({
  url:{
    default:"google.com"
  },
  cropTop:{
    default:0,
  },
  frameWidth:{
    default:1000
  },
  frameHeight:{
    default:800
  },
  width:{
    default:125
  },
  height:{
    default:600
  }
})

const frameUrl    = ref(props.url);
const cropTop     = String(props.cropTop) + "px";
const frameWidth  = ref(props.frameWidth);
const frameHeight = ref(props.frameHeight);
const width       = String(props.width) + "%";
const height      = String(props.height) + "px";
const speed       = String(props.speed);

const styleString = "transform: scale(0.8); transform-origin: top left; width:" + width + "; height: " + height + "; overflow: hidden;"

const frameStyle = "border: none; transform: translateY(" + cropTop + ");"




</script>


<template>
  <div class="slidev-layout default">
  <slot />
  <div :style=styleString>
    <iframe 
      :src=frameUrl
      :width=frameWidth 
      :height=frameHeight
      :style=frameStyle>
    </iframe>
  </div>
  </div>
</template>