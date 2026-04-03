<script setup>
import { computed } from 'vue'
import { useNav, useSlideContext } from '@slidev/client'

const props = defineProps({
  url: {
    default: "google.com"
  },
  cropTop: {
    default: 0,
  },
  frameWidth: {
    default: 1000
  },
  frameHeight: {
    default: 800
  },
  width: {
    default: 125
  },
  height: {
    default: 600
  }
})

const frameUrl    = computed(() => props.url)
const frameWidth  = computed(() => props.frameWidth)
const frameHeight = computed(() => props.frameHeight)

const styleString = computed(() =>
  `transform: scale(0.8); transform-origin: top left; width: ${props.width}%; height: ${props.height}px; overflow: hidden;`
)
const frameStyle = computed(() =>
  `border: none; transform: translateY(${props.cropTop}px);`
)

// useNav() provides global navigation state (currentPage).
// useSlideContext() provides this slide's own page number ($page).
// Combining them lets us gate the iframe on whether this slide is active.
const { currentPage } = useNav()
const { $page } = useSlideContext()
const isActive = computed(() => currentPage.value === $page.value)
</script>

<template>
  <div class="slidev-layout default">
    <slot />
    <div :style="styleString">
      <iframe
        v-if="isActive"
        :src="frameUrl"
        :width="frameWidth"
        :height="frameHeight"
        :style="frameStyle"
      />
    </div>
  </div>
</template>
