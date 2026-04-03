<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps({
  squares: {
    default: "{sq:../figures/blue-square.svg, ind:0}",
  },
  // transitions: {
  //   default: [],
  // },
})

let squares = (props.squares.split(";"));
// console.log(squares)
squares = squares.map((s) => JSON.parse(s));

let clickRanges = [];
for( let i = 0; i < squares.length-1; i++){
  clickRanges.push([String(squares[i]["ind"]) , String(squares[i+1]["ind"])]);
}
clickRanges.push([String(squares[squares.length - 1]["ind"]), String(-1)])

let finalList = squares.map(function(s, i){
  let entry = '{"sq":"' + s["sq"] + '", "ind1":"' +
   clickRanges[i][0] + '", "ind2":"' + clickRanges[i][1] + '", "combInd":"' + [clickRanges[i]] + '", "comb":"['+ clickRanges[i][0] + ',' + clickRanges[i][1] + ']"}'
  return JSON.parse(entry);
})


// let finalSquares = JSON.stringify(finalList);


function getFileName(sq){
  return new URL("../figures/" + sq, import.meta.url);
}

function changeSquare(newPath){
  squares = newPath;
}

const output = getFileName(squares[0]);

// const transitions = ref(props.transitions);
</script> 

<template>
  <!-- {{squares}} -->
  <!-- {{finalList}} -->
    <div v-for="item in finalList" :key="item.sq" >
          <div v-if="item.ind2 == -1">
            <div v-if="item.ind1 == 0">
              <Square :square=item.sq></Square>
            </div>
            <div v-else>  
              <Square v-click=item.ind1 :square=item.sq></Square>
            </div>
          </div>
          <div v-else-if="item.ind1 == 0">
            <Square v-click.hide=item.ind2 :square=item.sq></Square>
          </div>
          <div v-else>
           <Square v-click=item.ind1 v-click.hide=item.ind2   :square=item.sq></Square>
          </div>          
    </div>
</template>
