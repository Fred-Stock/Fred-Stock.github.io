<script setup>
import { ref, computed } from 'vue'

import AniSquare from './AniSquare.vue' 

// Paste your full grid here, example (rows x cols)
// This is just a snippet - replace with your actual grid data as an array of arrays of strings
const grid = [
  [
    "{\"sq\":\"yellow-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"blue-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}"
  ],
  [
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"blue-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"yellow-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"blue-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}"
  ],
  [
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"blue-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"blue-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"yellow-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"blue-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}"
  ],
  [
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"blue-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"blue-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"yellow-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"blue-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"yellow-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"blue-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}"
  ],
  [
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"blue-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"blue-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"yellow-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"blue-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"yellow-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"blue-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"yellow-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"blue-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}"
  ],
  [
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"blue-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"blue-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"blue-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"yellow-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"blue-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"yellow-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"blue-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"yellow-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"yellow-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}"
  ],
  [
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"yellow-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"yellow-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"yellow-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"yellow-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"yellow-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"yellow-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"yellow-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"yellow-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"yellow-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"yellow-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"yellow-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}"
  ],
  [
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"yellow-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"yellow-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"yellow-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"yellow-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"yellow-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"yellow-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"yellow-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"yellow-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"yellow-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"red-square.svg\", \"ind\":\"0\"}"
  ],
  [
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"yellow-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"yellow-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"yellow-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"yellow-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"yellow-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"yellow-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"yellow-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"blue-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"yellow-square.svg\", \"ind\":\"2\"}",
    "{\"sq\":\"yellow-square.svg\", \"ind\":\"0\"};{\"sq\":\"grey-square.svg\", \"ind\":\"1\"};{\"sq\":\"yellow-square.svg\", \"ind\":\"2\"}"
  ]
]

// Cell size
const cellSize = 30
const rows = grid.length
const cols = grid[0].length

// Helper to parse the ind values from the squares string
function parseSquares(squaresStr) {
  const parts = squaresStr.split(';')
  return parts.map(p => {
    try {
      return Number(JSON.parse(p).ind)
    } catch {
      return null
    }
  }).filter(i => i !== null)
}

// Build map from ind → Set of cell coords "r,c"
function getCellsByInd(grid) {
  const cellsByInd = {}
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      const squaresStr = grid[r][c]
      if (!squaresStr) continue
      const inds = parseSquares(squaresStr)
      inds.forEach(ind => {
        if (!cellsByInd[ind]) cellsByInd[ind] = new Set()
        cellsByInd[ind].add(`${r},${c}`)
      })
    }
  }
  return cellsByInd
}

// Get neighbors of a cell (up, right, down, left)
function neighbors(r, c) {
  return [
    [r - 1, c],
    [r, c + 1],
    [r + 1, c],
    [r, c - 1]
  ].filter(([nr, nc]) => nr >= 0 && nr < rows && nc >= 0 && nc < cols)
}

// Find connected components of a set of cells
function findConnectedComponents(cellsSet) {
  const components = []
  const visited = new Set()

  function dfs(start) {
    const stack = [start]
    const comp = new Set()
    while (stack.length) {
      const curr = stack.pop()
      if (visited.has(curr)) continue
      visited.add(curr)
      comp.add(curr)
      const [r, c] = curr.split(',').map(Number)
      neighbors(r, c).forEach(([nr, nc]) => {
        const neighborCoord = `${nr},${nc}`
        if (cellsSet.has(neighborCoord) && !visited.has(neighborCoord)) {
          stack.push(neighborCoord)
        }
      })
    }
    return comp
  }

  for (const cell of cellsSet) {
    if (!visited.has(cell)) {
      components.push(dfs(cell))
    }
  }
  return components
}

// Check if cell is in the region set
function isInRegion(r, c, region) {
  return region.has(`${r},${c}`)
}

// Get boundary edges of a region (connected component)
function getBoundaryEdges(region) {
  const edges = new Set()
  function edgeKey(x1, y1, x2, y2) {
    // Sort coordinates so edge direction doesn’t matter for uniqueness
    // But here direction is needed for path building, so keep order
    return `${x1},${y1}-${x2},${y2}`
  }

  for (const coord of region) {
    const [r, c] = coord.split(',').map(Number)
    const x = c * cellSize
    const y = r * cellSize

    // Top edge
    if (!isInRegion(r - 1, c, region)) edges.add(edgeKey(x, y, x + cellSize, y))
    // Right edge
    if (!isInRegion(r, c + 1, region)) edges.add(edgeKey(x + cellSize, y, x + cellSize, y + cellSize))
    // Bottom edge
    if (!isInRegion(r + 1, c, region)) edges.add(edgeKey(x + cellSize, y + cellSize, x, y + cellSize))
    // Left edge
    if (!isInRegion(r, c - 1, region)) edges.add(edgeKey(x, y + cellSize, x, y))
  }
  return Array.from(edges)
}

// Build polygon path from unordered edges by walking the edges in order
function buildPolygonPath(edges) {
  if (edges.length === 0) return ""

  // Map from start point to end point for each edge
  const pointMap = new Map()
  for (const edge of edges) {
    const [start, end] = edge.split('-')
    pointMap.set(start, end)
  }

  const startPoint = edges[0].split('-')[0]
  const pathPoints = [startPoint]

  let currentPoint = startPoint
  while (true) {
    const nextPoint = pointMap.get(currentPoint)
    if (!nextPoint || nextPoint === startPoint) break
    pathPoints.push(nextPoint)
    currentPoint = nextPoint
  }

  let path = `M${pathPoints[0]}`
  for (let i = 1; i < pathPoints.length; i++) {
    path += ` L${pathPoints[i]}`
  }
  path += ' Z'

  return path
}

// Compute all outlines for all connected components for a given ind
function computeOutlinesForInd(ind) {
  if (!cellsByInd[ind]) return []
  const components = findConnectedComponents(cellsByInd[ind])
  return components.map(region => {
    const edges = getBoundaryEdges(region)
    return buildPolygonPath(edges)
  })
}

const cellsByInd = getCellsByInd(grid)
const inds = Object.keys(cellsByInd).map(Number).sort((a, b) => a - b)

const currentInd = ref(inds[0] || 0)

function nextInd() {
  const currentIndex = inds.indexOf(currentInd.value)
  currentInd.value = inds[(currentIndex + 1) % inds.length]
}

const outlines = computed(() => computeOutlinesForInd(currentInd.value))

const svgWidth = cols * cellSize
const svgHeight = rows * cellSize
</script>

<template>
  <div style="position: relative; width: max-content;">

    <!-- Grid -->
    <div
      class="grid"
      :style="{
        display: 'grid',
        gridTemplateColumns: `repeat(${cols}, ${cellSize}px)`,
        gridAutoRows: `${cellSize}px`,
        gap: '1px',
        position: 'relative',
      }"
    >
      <div
  v-for="(row, r) in grid"
  :key="r"
>
        <div
          v-for="(cellSquares, c) in row"
          :key="`${r}-${c}`"
          v-click="nextInd"
          style="width: 30px; height: 30px;"
        >
          <!-- Pass the squares string directly -->
          <AniSquare :squares="cellSquares" :ind="currentInd" />
        </div>
      </div>
    </div>

    <!-- SVG Outline for currentInd -->
    <svg
      :width="svgWidth"
      :height="svgHeight"
      style="position: absolute; top: 0; left: 0; pointer-events: none;"
    >
      <path
        v-for="(path, index) in outlines"
        :key="index"
        :d="path"
        stroke="red"
        stroke-width="2"
        fill="none"
        stroke-linejoin="round"
      />
    </svg>
  </div>

  <p style="margin-top: 10px;">
    Click any cell to cycle through indices: currently highlighting index
    <strong>{{ currentInd }}</strong>.
  </p>
</template>
