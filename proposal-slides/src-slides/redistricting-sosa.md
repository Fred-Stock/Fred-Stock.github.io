# Redistricting in Square and Triangular Grids

<font color="lightgrey">

Hugo Akitaya, Kyle Dituro, Andrei Gonczi, Matias Korman, Diane Souvaine, <strong>Frederick Stock</strong>, and Csaba D. Toth

Symposium on Simplicity in Algorithms 2026
</font>

---

## Redistricting

<div class="flex justify-center">
  <img src="../general/sosa-figures/legal-challenges.png" class="h-80" alt="Brennan Center For Justice" />
</div>

<p class="text-center text-sm italic">Source: Brennan Center For Justice</p>

---
dragPos:
  map42: 215,290,34,34
  map32: 334,198,34,34
  map22: 674,306,34,34
  map12: 517,202,34,34
  d05: Left,Top,Width,Height
  d23: Left,Top,Width,Height
  d23r: Left,Top,Width,Height
  d32: Left,Top,Width,Height
  bell: Left,Top,Width,Height
---

## Mathematics in Redistricting

<p class="text-primary font-bold">Question: How do you prove gerrymandering?</p>


<v-click>

* Statistical Analysis
* Sample possible district maps and compare to real world 

</v-click>

<img v-click="1" v-drag="[242,337,412,186]" src="/figures/gerry-bell.svg">

<img v-click="5" v-drag="[185,293,104,208]" src="/figures/bell0-5.svg">

<img v-click="2" v-drag="[305,202,183,299]" src="/figures/bell2-3.svg">

<img v-click="3" v-drag="[488,205,104,298]" src="/figures/bell2-3-r.svg">

<img v-click="4" v-drag="[576,309,172,192]" src="/figures/bell3-2.svg">


<v-drag v-click="3" pos="map12">

<font color="lightpink">2</font> <font color="purple">3</font>

</v-drag>

<v-drag v-click="4" pos="map22">

<font color="lightpink">3</font> <font color="purple">2</font>

</v-drag>

<v-drag v-click="2" pos="map32">

<font color="lightpink">2</font> <font color="purple">3</font>

</v-drag>

<v-drag v-click="5" pos="map42">

<font color="lightpink">0</font> <font color="purple">5</font>

</v-drag>

---

## Mathematics in Redistricting

<p class="text-primary font-bold">Question: How do you prove gerrymandering?</p>

* Statistical Analysis
* Sample possible district maps and compare to real world 


<p class="text-primary font-bold">Question: How should we sample these district maps?</p>

<div class="relative">
<v-clicks class="absolute top-0 left-0">

* <strong>Our answer:</strong> Markovian Models

</v-clicks>
</div>



---

## Setting

* <font color="yellow"><strong>Map:</strong></font> A graph $M = (V,E)$ that is either:

<div class="relative">
<div class="absolute top-0 left-0">

  <v-click at="1">

  1.  An equilateral subsection of the triangular grid 

  </v-click>
  <v-click at="2"> 

  2. A $m \times n$ subset of the integer lattice $\mathbb{Z}^2$ 
  
  </v-click>

</div>


<div class="grid grid-cols-2 gap-20 mt-12 absolute top-7 left-10%">
  <v-click>
    <!-- <img src="../general/sosa-figures/triangule-graph.png" class="h-40 mx-auto" /> -->
      <div class="flex flex-col items-center justify-center h-full">
      <div style="display:flex; flex-direction:column; align-items:center;">
        <div style="display:flex;">
          <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"}'/>
        </div>
        <div style="display:flex; margin-top:-15px;">
          <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"}'/>
          <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"}'/>
        </div>
        <div style="display:flex; margin-top:-15px;">
          <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"}'/>
          <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"}'/>
          <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"}'/>
        </div>
        <div style="display:flex; margin-top:-15px;">
          <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"}'/>
          <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"}'/>
          <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"}'/>
          <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"}'/>
        </div>
        <div style="display:flex; margin-top:-15px;">
          <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"}'/>
          <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"}'/>
          <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"}'/>
          <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"}'/>
          <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"}'/>
        </div>
        <div style="display:flex; margin-top:-15px;">
          <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"}'/>
          <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"}'/>
          <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"}'/>
          <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"}'/>
          <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"}'/>
          <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"}'/>
        </div>
      </div>
    </div>
  </v-click>
  <v-click>
    <!-- <img src="../general/sosa-figures/square-graph.png" class="h-40 mx-auto" /> -->
      <div class="flex flex-col items-center justify-center h-full">
        <div class="grid grid-cols-6 gap-1" style="zoom: 1.5;">
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
          <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
        </div>
      </div>

  
  </v-click>
</div>

</div>

---

## Setting

<span class="darklist">

* <font color="yellow"><strong>Part:</strong></font> A subdivision of $M$ 
  <v-click>

  * We consider maps with <strong> <span v-mark="{at:'1', color:'yellow'}">three parts</span> </strong> 
  * *Not necessarily of equal size 

  </v-click>

<div class="relative">
<v-click class="absolute top-0 left-0">
  
  * Each part must be <strong><font color="yellow">connected</font></strong> 

</v-click>


<div class="grid grid-cols-2 gap-15 mt-5 absolute top-5 left-10%">
  <!-- <img src="../general/sosa-figures/colored-triangle.png" class="h-40 mx-auto" /> -->
  <div class="flex flex-col items-center justify-center h-full">
  <div style="display:flex; flex-direction:column; align-items:center;">
    <div style="display:flex;">
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
    </div>
  </div>
</div>
<div class="flex flex-col items-center justify-center h-full">
  <div class="grid grid-cols-6 gap-1" style="zoom: 1.5;">
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
  </div>
</div>

  <!-- <img src="../general/sosa-figures/colored-square.png" class="h-40 mx-auto" /> -->
</div>
</div>
</span>

---

## Setting

<font color="yellow"><strong>Recombination:</strong></font> "Merge two adjacent parts and redraw their shared boundary"

<div class="flex justify-around mt-10">
  <v-click>
  <!-- <img src="../general/sosa-figures/inf-slack-1.png" class="w-1/4" /></v-click> -->
  <div class="flex flex-col items-center justify-center h-full">
  <div class="grid grid-cols-6 gap-.5" style="zoom: 1.25;">
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
  </div>
</div>
  </v-click>
  <v-click>
  <!-- <img src="../general/sosa-figures/inf-slack-2.png" class="w-1/4" /> -->
  <div class="flex flex-col items-center justify-center h-full">
  <div class="grid grid-cols-6 gap-.5" style="zoom: 1.25;">
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
  </div>
</div>
  </v-click>
  <v-click>
  <!-- <img src="../general/sosa-figures/recomb-final.png" class="w-1/4" /> -->
  <div class="flex flex-col items-center justify-center h-full">
  <div class="grid grid-cols-6 gap-.5" style="zoom: 1.25;">
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
  </div>
</div>
  </v-click>
</div>


---

## Recombination Markov Chains

* Samples uniformly from distribution of spanning trees over <strong>M</strong>

<div class="relative">
<v-clicks class="absolute top-0 left-0">

* Favors "compact" parts of <strong>M</strong>
  * Preferable for voting maps
* If recombination is <font color="yellow"><strong>universal</strong></font>, then the Markov chain is <strong>irreducible</strong> 
  * <strong>Universality</strong> $\Rightarrow$ any map can be turned into another 

</v-clicks>
</div>

---
clicks: 5
---

## Recombination

<strong> Is recombination universal? </strong>

<div class="relative">
<v-click class="absolute top-0 left-0">

<strong><font color="yellow">Slack:</font></strong> How much a part's size may vary from initialization.

* $\infty$-Slack $\Rightarrow$ Too simple

</v-click>

<div class="flex flex-col items-center justify-center h-full">
  <div class="grid grid-cols-6 gap-0  absolute top-20" style="zoom: 1.5;">
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"2"};{"sq":"red-square.svg","ind":"3"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"grey-square.svg","ind":"4"};{"sq":"blue-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"1"};{"sq":"grey-square.svg","ind":"4"};{"sq":"yellow-square.svg","ind":"5"}'/></div>
  </div>
</div>

</div>


---
clicks: 6
---

## Recombination

<div class="relative">

<div class="absolute top-0 left-0">
<strong> Is recombination universal? </strong>


<strong><font color="yellow">Slack:</font></strong> How much a part's size may vary from initialization.

* $\infty$-Slack $\Rightarrow$ Too simple

* 0-Slack $\Rightarrow$ leads to "rigid" configurations <span v-click="5"> <font color="yellow"> $\Rightarrow$ not universal </font> </span>

<v-click at="6">

* <font color="yellow"><strong> We use 1-slack </strong></font>

</v-click>

</div>
<!-- <div class="flex justify-around mt-10">
  <v-click><img src="../general/sosa-figures/0-slack-1.png" class="w-1/6" /></v-click>
  <v-click><img src="../general/sosa-figures/0-slack-2.png" class="w-1/6" /></v-click>
  <v-click><img src="../general/sosa-figures/0-slack-5.png" class="w-1/6" /></v-click>
</div> -->


<div class="flex flex-col items-center justify-center h-full">
  <div class="grid grid-cols-6 gap-.5 absolute top-30" style="zoom: 1.5;">
    <div><AniSquare squares='{"sq":"blue.svg","ind":"0"};{"sq":"lightgray_dot.svg","ind":"1"};{"sq":"lightgray.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"blue.svg","ind":"0"};{"sq":"lightgray_dot.svg","ind":"1"};{"sq":"lightgray.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"red.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue.svg","ind":"0"};{"sq":"lightgray_dot.svg","ind":"1"};{"sq":"lightgray.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"lightgray.svg","ind":"0"};{"sq":"lightgray_dot.svg","ind":"1"};{"sq":"blue.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"lightgray.svg","ind":"0"};{"sq":"lightgray_dot.svg","ind":"1"};{"sq":"blue.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"red.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"white.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"magenta.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"magenta.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"lightgray.svg","ind":"0"};{"sq":"lightgray_dot.svg","ind":"1"};{"sq":"blue.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"white.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"white.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"darkred.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"magenta.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"darkblue.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"darkblue.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"black.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"darkred.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"darkred.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"cyan.svg","ind":"0"};{"sq":"lightgray_dot.svg","ind":"3"};{"sq":"green.svg","ind":"4"}'/></div>
    <div><AniSquare squares='{"sq":"darkblue.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"green.svg","ind":"0"};{"sq":"lightgray_dot.svg","ind":"3"};{"sq":"cyan.svg","ind":"4"}'/></div>
    <div><AniSquare squares='{"sq":"black.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"black.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"purple.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"cyan.svg","ind":"0"};{"sq":"lightgray_dot.svg","ind":"3"};{"sq":"green.svg","ind":"4"}'/></div>
    <div><AniSquare squares='{"sq":"cyan.svg","ind":"0"};{"sq":"lightgray_dot.svg","ind":"3"};{"sq":"green.svg","ind":"4"}'/></div>
    <div><AniSquare squares='{"sq":"green.svg","ind":"0"};{"sq":"lightgray_dot.svg","ind":"3"};{"sq":"cyan.svg","ind":"4"}'/></div>
    <div><AniSquare squares='{"sq":"green.svg","ind":"0"};{"sq":"lightgray_dot.svg","ind":"3"};{"sq":"cyan.svg","ind":"4"}'/></div>
    <div><AniSquare squares='{"sq":"purple.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"purple.svg","ind":"0"}'/></div>
  </div>
</div>

</div>

---

## Previous Work

<strong>(Cannon 2024)</strong> *Irreducibility of Recombination Markov Chains in the Triangular Lattice* 
<v-clicks class="darklist">

  * Universality of recombination 
  * 3 parts with $\pm 1$ Slack 
  * <strong>Only</strong> triangular lattice 
  * <strong>Only</strong> simply connected parts 
  * $O(n^3)$ recombinations 

</v-clicks>

<div class="grid grid-cols-2 gap-25% mt-4 absolute top-75 left-25%">
<div class="flex flex-col items-center justify-center h-full">
  <v-click at="3">
  <div style="display:flex; flex-direction:column; align-items:center; zoom:.75;">
    <div style="display:flex;">
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
    </div>
  </div>
  </v-click>
</div>
<div class="flex flex-col items-center justify-center h-full">
  
  <v-click at="4" class="relative">
  <div style="display:flex; flex-direction:column; align-items:center; zoom:.75;">
    <div style="display:flex;">
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
    </div>
  </div>
    <img src="../figures/big-x.svg" class="absolute top-25% left-82" style="scale:2.5"></img>
  </v-click>
</div>
</div>

---

## <font color="red"> <del>Previous Work</del> </font> Our Results

<strong>(Akitaya et al. 2026)</strong> *Redistricting in Square and Triangular Grids*


- Universality of recombination 
- 3 parts with $\pm 1$ Slack 

<v-clicks class="darklist">

- <font color="red"> <del>Only</del> </font> Triangular <font color="blue">and Square grid </font> 
- <font color="red"> <del>Only simply connected parts</del></font> <font color="blue">Connected parts </font> 
- $O(n^3)$ recombinations 

</v-clicks>

<div class="grid grid-cols-2 gap-25% mt-4 absolute top-75 left-25%">
<div class="flex flex-col items-center justify-center h-full">
  <v-click at="1" hide>
  <div style="display:flex; flex-direction:column; align-items:center; zoom:.75;" class="absolute top-0 left--9.75">
    <div style="display:flex;">
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
    </div>
  </div>
  </v-click>
  <v-click at="1">
  <!-- <img src="../general/sosa-figures/inf-slack-1.png" class="w-1/4" /></v-click> -->
    <div class="flex flex-col items-center justify-center h-full absolute top--3 left--9.75">
      <div class="grid grid-cols-6 gap-.5" style="zoom: 1.25;">
        <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
        <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
      </div>
    </div>
  </v-click>
</div>
<div class="flex flex-col items-center justify-center h-full">
  <div style="display:flex; flex-direction:column; align-items:center; zoom:.75;">
    <div style="display:flex;">
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
    </div>
  </div>
    <v-click hide at="2">
    <img src="../figures/big-x.svg" class="absolute top-25% left-82" style="scale:2.5"></img>
    </v-click>
    <v-click at="2">
    <img src="../figures/big-check.svg" class="absolute top-20% left-78" style="scale:1.5"></img>
    </v-click>
</div>
</div>


---


## Our Strategy

- If every map can reach the same configuration $\Rightarrow$ recombination is universal. 



<div class="absolute left-30% top-35%">

<img v-click.hide src="../figures/reversible-recomb.svg" style="scale:1.5;"></img>

<img v-click=[1,2] src="../figures/recomb-strategy.svg" style="scale:1.5;"></img>

<img v-click="2" src="../figures/recomb-strategy-2.svg" style="scale:1.5;"></img>

</div>

---
clicks: 6

dragPos:
  tri: Left,Top,Width,Height
  sqPath: Left,Top,Width,Height
---

## Our Strategy
<img v-click at="1" v-drag="[199,268,326,245]" src="../figures/tri-canon-path.svg"></img>

<img v-after v-drag="[565,254,262,273]" src="../figures/sq-canon-path.svg"></img>

<div class="relative">

<div class="absolute top-0 left-0">

- If every map can reach the same configuration $\Rightarrow$ recombination is universal. 

<div class="darklist">
<span v-after>


1. <span v-mark="{at:[1,3], type:'box', iterations:'1', color:'yellow'}"> Define a <font color="yellow"><strong>canonical ordering</strong></font> on <strong>M</strong> </span>

</span>

<v-click at="+2">

2. <span v-mark="{at:[3,5], type:'box', iterations:'1', color:'yellow'}"> Use recombination to assign part 1 ($\mathcal{P}_1$) to the first $|\mathcal{P}_1|$ cells </span>

</v-click>

<v-click at="+2">

3. <span v-mark="{at:'5', type:'box', iterations:'1', color:'yellow'}"> Assign part 2 to the next $|\mathcal{P}_2|$ cells </span>

</v-click>
</div>


</div>
<!-- 
<div class="grid grid-cols-2 gap-4 mt-4 absolute top-40 left-25%">
  <img src="../general/sosa-figures/tri-strategy-1.png" class="h-32 mx-auto" />
  <img src="../general/sosa-figures/sq-strategy-1.png" class="h-32 mx-auto" />
</div> -->

<div class="grid grid-cols-2 gap-10 mt-4 absolute top-35 left-15%">
<div class="flex flex-col items-center justify-center h-full">
  <div style="display:flex; flex-direction:column; align-items:center;">
    <div style="display:flex;">
      <AniHex squares='{"sq":"grey-hexagon.svg","ind":"1"};{"sq":"red-hexagon.svg","ind":"2"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"};{"sq":"red-hexagon.svg","ind":"2"}'/>
      <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"};{"sq":"red-hexagon.svg","ind":"2"};{"sq":"yellow-hexagon.svg","ind":"3"};{"sq":"red-hexagon.svg","ind":"4"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"};{"sq":"red-hexagon.svg","ind":"2"}'/>
      <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"};{"sq":"red-hexagon.svg","ind":"2"}'/>
      <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"};{"sq":"red-hexagon.svg","ind":"2"};{"sq":"yellow-hexagon.svg","ind":"3"};{"sq":"red-hexagon.svg","ind":"4"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"};{"sq":"yellow-hexagon.svg","ind":"2"};{"sq":"red-hexagon.svg","ind":"3"};{"sq":"yellow-hexagon.svg","ind":"4"}'/>
      <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"};{"sq":"yellow-hexagon.svg","ind":"2"};{"sq":"red-hexagon.svg","ind":"3"};{"sq":"yellow-hexagon.svg","ind":"4"}'/>
      <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"};{"sq":"yellow-hexagon.svg","ind":"2"}'/>
      <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"};{"sq":"yellow-hexagon.svg","ind":"2"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"};{"sq":"yellow-hexagon.svg","ind":"2"};{"sq":"blue-hexagon.svg","ind":"3"};{"sq":"yellow-hexagon.svg","ind":"6"}'/>
      <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"};{"sq":"yellow-hexagon.svg","ind":"2"}'/>
      <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"};{"sq":"yellow-hexagon.svg","ind":"2"}'/>
      <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"};{"sq":"blue-hexagon.svg","ind":"2"}'/>
      <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"};{"sq":"blue-hexagon.svg","ind":"2"};{"sq":"yellow-hexagon.svg","ind":"3"};{"sq":"blue-hexagon.svg","ind":"6"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"};{"sq":"blue-hexagon.svg","ind":"2"}'/>
      <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"};{"sq":"blue-hexagon.svg","ind":"2"}'/>
      <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"};{"sq":"blue-hexagon.svg","ind":"2"}'/>
      <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"};{"sq":"blue-hexagon.svg","ind":"2"}'/>
      <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"};{"sq":"blue-hexagon.svg","ind":"2"}'/>
      <AniHex squares='{"sq":"grey-hexagon.svg","ind":"0"};{"sq":"blue-hexagon.svg","ind":"2"}'/>
    </div>
  </div>
</div>

<div class="flex flex-col items-center justify-center h-full">
  <div class="grid grid-cols-6 gap-.5" style="zoom: 1.5;">
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"red-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"yellow-square.svg","ind":"2"};{"sq":"red-square.svg","ind":"3"};{"sq":"yellow-square.svg","ind":"4"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"yellow-square.svg","ind":"2"};{"sq":"red-square.svg","ind":"3"};{"sq":"yellow-square.svg","ind":"4"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"blue-square.svg","ind":"2"};{"sq":"red-square.svg","ind":"3"};{"sq":"yellow-square.svg","ind":"4"};{"sq":"blue-square.svg","ind":"6"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"blue-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"blue-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"red-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"red-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"yellow-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"blue-square.svg","ind":"2"};{"sq":"red-square.svg","ind":"3"};{"sq":"yellow-square.svg","ind":"4"};{"sq":"blue-square.svg","ind":"6"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"blue-square.svg","ind":"2"};{"sq":"red-square.svg","ind":"3"};{"sq":"blue-square.svg","ind":"4"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"blue-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"red-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"red-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"red-square.svg","ind":"4"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"yellow-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"blue-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"blue-square.svg","ind":"6"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"blue-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"blue-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"red-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"red-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"red-square.svg","ind":"4"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"yellow-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"yellow-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"blue-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"blue-square.svg","ind":"6"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"blue-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"red-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"red-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"red-square.svg","ind":"4"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"yellow-square.svg","ind":"2"};{"sq":"blue-square.svg","ind":"3"};{"sq":"yellow-square.svg","ind":"6"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"yellow-square.svg","ind":"2"};{"sq":"blue-square.svg","ind":"3"};{"sq":"yellow-square.svg","ind":"6"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"blue-square.svg","ind":"2"};{"sq":"yellow-square.svg","ind":"3"};{"sq":"blue-square.svg","ind":"4"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"blue-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"red-square.svg","ind":"2"};{"sq":"blue-square.svg","ind":"3"};{"sq":"red-square.svg","ind":"4"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"red-square.svg","ind":"2"};{"sq":"blue-square.svg","ind":"3"};{"sq":"red-square.svg","ind":"4"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"yellow-square.svg","ind":"2"};{"sq":"blue-square.svg","ind":"3"};{"sq":"yellow-square.svg","ind":"6"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"yellow-square.svg","ind":"2"};{"sq":"blue-square.svg","ind":"3"};{"sq":"yellow-square.svg","ind":"6"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"blue-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"grey-square.svg","ind":"0"};{"sq":"blue-square.svg","ind":"2"}'/></div>
  </div>
</div>

</div>
</div>

---
clicks: 3
---

## Tower Move

* Can we always grow $\mathcal{P}_1$? 

<!-- <div class="flex justify-around mt-10">
  <img src="../general/sosa-figures/need-tower-1.png" class="w-1/5" />
  <v-click><img src="../general/sosa-figures/need-tower-2.png" class="w-1/5" /></v-click>
  <v-click><img src="../general/sosa-figures/need-tower-3.png" class="w-1/5" /></v-click>
  <v-click><img src="../general/sosa-figures/need-tower-4.png" class="w-1/5" /></v-click>
</div> -->

<div class="flex flex-col items-center justify-center h-full">
  <div class="grid grid-cols-6 gap-1" style="zoom: 1.5;">
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"};{"sq":"grey-square.svg","ind":"1"};{"sq":"red-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"};{"sq":"grey-square.svg","ind":"1"};{"sq":"red-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"};{"sq":"grey-square.svg","ind":"1"};{"sq":"red-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"};{"sq":"grey-square.svg","ind":"1"};{"sq":"red-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"};{"sq":"grey-square.svg","ind":"1"};{"sq":"red-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"};{"sq":"grey-square.svg","ind":"1"};{"sq":"red-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"};{"sq":"grey-square.svg","ind":"1"};{"sq":"yellow-square.svg","ind":"2"};{"sq":"yellow-highlight-solid.svg","ind":"3"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"};{"sq":"grey-square.svg","ind":"1"};{"sq":"red-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"};{"sq":"grey-square.svg","ind":"1"};{"sq":"red-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"};{"sq":"grey-square.svg","ind":"1"};{"sq":"yellow-square.svg","ind":"2"};{"sq":"yellow-highlight-solid.svg","ind":"3"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"};{"sq":"grey-square.svg","ind":"1"};{"sq":"red-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"};{"sq":"grey-square.svg","ind":"1"};{"sq":"red-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"};{"sq":"grey-square.svg","ind":"1"};{"sq":"yellow-square.svg","ind":"2"};{"sq":"yellow-highlight-solid.svg","ind":"3"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"};{"sq":"grey-square.svg","ind":"1"};{"sq":"red-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"};{"sq":"grey-square.svg","ind":"1"};{"sq":"yellow-square.svg","ind":"2"};{"sq":"yellow-highlight-solid.svg","ind":"3"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"};{"sq":"grey-square.svg","ind":"1"};{"sq":"yellow-square.svg","ind":"2"};{"sq":"yellow-highlight-solid.svg","ind":"3"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"};{"sq":"grey-square.svg","ind":"1"};{"sq":"red-square.svg","ind":"2"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"};{"sq":"grey-square.svg","ind":"1"};{"sq":"yellow-square.svg","ind":"2"};{"sq":"yellow-highlight-solid.svg","ind":"3"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"};{"sq":"grey-square.svg","ind":"1"};{"sq":"yellow-square.svg","ind":"2"};{"sq":"yellow-highlight-solid.svg","ind":"3"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"};{"sq":"grey-square.svg","ind":"1"};{"sq":"yellow-square.svg","ind":"2"};{"sq":"yellow-highlight-solid.svg","ind":"3"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"};{"sq":"grey-square.svg","ind":"1"};{"sq":"yellow-square.svg","ind":"2"};{"sq":"yellow-highlight-solid.svg","ind":"3"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
  </div>
</div>

---
clicks: 10
---

## Tower Move

* We use <font color="yellow"><strong>Tower Moves</strong></font> to grow $\mathcal{P}_1$ 
<div class="relative">
<v-click at="10" class="absolute top-0 left-0">

  * Leaves two parts sized $\pm 1$ 

</v-click>
</div>

<!-- <div class="grid grid-cols-2 gap-4 mt-8">
  <img src="../general/sosa-figures/tri-tower-1.png" class="h-40 mx-auto" />
  <img src="../general/sosa-figures/sq-tower-1.png" class="h-40 mx-auto" />
</div> -->

<div class="grid grid-cols-2 gap-4 mt-8 absolute top-40 left-40">

 <div class="flex flex-col items-center justify-center h-full">
  <div class="grid grid-cols-6 gap-0" style="zoom: 1.5;">
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"};{"sq":"red-square-circle-start.svg","ind":"1"};{"sq":"red-square.svg","ind":"10"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"};{"sq":"blue-square-grey-line.svg","ind":"2"};{"sq":"blue-square-line-circle.svg","ind":"8"};{"sq":"red-square.svg","ind":"9"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"};{"sq":"red-square-grey-line.svg","ind":"3"};{"sq":"red-square-line-circle.svg","ind":"6"};{"sq":"blue-square.svg","ind":"7"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"};{"sq":"yellow-square-line-circle.svg","ind":"4"};{"sq":"red-square.svg","ind":"5"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"blue-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"red-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
    <div><AniSquare squares='{"sq":"yellow-square.svg","ind":"0"}'/></div>
  </div>
</div>  

  <div class="flex flex-col items-center justify-center h-full">
    <div style="display:flex; flex-direction:column; align-items:center;">
      <div style="display:flex;">
        <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      </div>
      <div style="display:flex; margin-top:-15px;">
        <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
        <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      </div>
      <div style="display:flex; margin-top:-15px;">
        <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
        <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
        <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"};{"sq":"red-hexagon-circle-start.svg","ind":"1"};{"sq":"red-hexagon.svg","ind":"10"}'/>
      </div>
      <div style="display:flex; margin-top:-15px;">
        <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
        <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
        <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"};{"sq":"yellow-hexagon-line.svg","ind":"2"};{"sq":"yellow-hexagon-line-circle.svg","ind":"8"};{"sq":"red-hexagon.svg","ind":"9"}'/>
        <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      </div>
      <div style="display:flex; margin-top:-15px;">
        <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
        <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
        <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"};{"sq":"blue-hexagon-line.svg","ind":"3"};{"sq":"blue-hexagon-line-circle.svg","ind":"6"};{"sq":"yellow-hexagon.svg","ind":"7"}'/>
        <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
        <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      </div>
      <div style="display:flex; margin-top:-15px;">
        <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
        <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"}'/>
        <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"};{"sq":"yellow-hexagon-line-circle.svg","ind":"4"};{"sq":"blue-hexagon.svg","ind":"5"}'/>
        <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"}'/>
        <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
        <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"}'/>
      </div>
    </div>
  </div>


</div>

---
clicks: 15
---

## Our Algorithm

<div class="relative">

<div class="absolute top-0 left-0">

<span v-mark="{at:[1,2], type:'box', iterations:'1', color:'yellow'}">

1. Use a <strong><font color="yellow">tower move</font></strong> to grow $\mathcal{P}_1$ 

</span>

<!-- <span v-mark="{at:[3,4], type:'box', iterations:'1', color:'yellow'}"> -->

<v-click at="2">

<span v-mark="{at:[3,5], type:'box', iterations:'1', color:'yellow'}">

2. <strong><font color="yellow">Rebalance</font></strong> the districts 

</span>

  <v-click at="3">
      
      * The complicated part 

  </v-click>

</v-click>

<v-click at="5">

<span v-mark="{at:[5,14], type:'box', iterations:'1', color:'yellow'}">

3. <strong><font color="yellow">Repeat</font></strong> until $\mathcal{P}_1$ is fully grown 

</span>
</v-click>

<span v-mark="{at:14, type:'box', iterations:'1', color:'yellow'}">
<v-click at="14">

4. Only one more recombination is needed 

</v-click>
</span>

</div>

<!-- <div class="flex justify-center mt-4 absolute top-20">
  <img src="../general/sosa-figures/algo/algo-_g117.png" class="h-40" />
</div> -->

</div>


<div class="grid grid-cols-2 gap-30 mt-8 absolute top-50 left-30">

<v-click at="1">

<div class="flex flex-col items-center justify-center h-full">
  <div style="display:flex; flex-direction:column; align-items:center;">
    <div style="display:flex;">
      <AniHex squares='{"sq":"red-hexagon-circle-start.svg","ind":"1"};{"sq":"red-hexagon.svg","ind":"3"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"yellow-hexagon-line-circle.svg","ind":"1"};{"sq":"red-hexagon-circle.svg","ind":"3"};{"sq":"red-hexagon.svg","ind":"5"};{"sq":"red-hexagon-circle-start.svg","ind":"7"};{"sq":"red-hexagon.svg","ind":"9"}'/>
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"1"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"1"};{"sq":"yellow-hexagon-line-circle.svg","ind":"7"};{"sq":"red-hexagon-circle.svg","ind":"9"};{"sq":"red-hexagon.svg","ind":"11"}'/>
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"1"}'/>
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"1"};{"sq":"red-hexagon-circle-start.svg","ind":"13"};{"sq":"red-hexagon.svg","ind":"14"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"1"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"1"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"1"};{"sq":"yellow-hexagon-line.svg","ind":"13"};{"sq":"red-hexagon-circle.svg","ind":"14"};{"sq":"red-hexagon.svg","ind":"16"}'/>
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"1"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"1"};{"sq":"yellow-hexagon.svg","ind":"16"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"1"};{"sq":"yellow-hexagon-circle.svg","ind":"13"};{"sq":"yellow-hexagon.svg","ind":"14"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"1"};{"sq":"blue-hexagon-line-circle.svg","ind":"13"};{"sq":"yellow-hexagon-circle.svg","ind":"14"};{"sq":"yellow-hexagon.svg","ind":"16"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"1"};{"sq":"yellow-hexagon-circle.svg","ind":"7"};{"sq":"yellow-hexagon.svg","ind":"9"};{"sq":"blue-hexagon.svg","ind":"16"}'/>
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"1"};{"sq":"blue-hexagon-circle.svg","ind":"14"};{"sq":"blue-hexagon.svg","ind":"16"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"1"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"1"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"1"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"1"}'/>
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"1"};{"sq":"blue-hexagon-circle.svg","ind":"5"};{"sq":"blue-hexagon.svg","ind":"7"}'/>
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"1"};{"sq":"blue-hexagon-circle.svg","ind":"11"};{"sq":"blue-hexagon.svg","ind":"13"}'/>
    </div>
  </div>
</div>

</v-click>

<div class="flex flex-col items-center justify-center h-full">
  <div style="display:flex; flex-direction:column; align-items:center;">
    <div style="display:flex;">
      <AniHex squares='{"sq":"red-hexagon-circle-start.svg","ind":"0"};{"sq":"grey-hexagon.svg","ind":"1"};{"sq":"red-hexagon.svg","ind":"2"};{"sq":"grey-hexagon.svg","ind":"3"};{"sq":"red-hexagon.svg","ind":"4"};{"sq":"grey-hexagon.svg","ind":"7"};{"sq":"red-hexagon.svg","ind":"8"};{"sq":"grey-hexagon.svg","ind":"9"};{"sq":"red-hexagon.svg","ind":"10"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"yellow-hexagon-line-circle.svg","ind":"0"};{"sq":"grey-hexagon.svg","ind":"1"};{"sq":"red-hexagon-circle.svg","ind":"2"};{"sq":"grey-hexagon.svg","ind":"3"};{"sq":"red-hexagon.svg","ind":"4"};{"sq":"red-hexagon-circle-start.svg","ind":"6"};{"sq":"grey-hexagon.svg","ind":"7"};{"sq":"red-hexagon.svg","ind":"8"};{"sq":"grey-hexagon.svg","ind":"9"};{"sq":"red-hexagon.svg","ind":"10"}'/>
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"};{"sq":"grey-hexagon.svg","ind":"1"};{"sq":"red-hexagon.svg","ind":"2"};{"sq":"grey-hexagon.svg","ind":"3"};{"sq":"red-hexagon.svg","ind":"4"};{"sq":"grey-hexagon.svg","ind":"7"};{"sq":"red-hexagon.svg","ind":"8"};{"sq":"grey-hexagon.svg","ind":"9"};{"sq":"red-hexagon.svg","ind":"10"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"};{"sq":"grey-hexagon.svg","ind":"1"};{"sq":"yellow-hexagon.svg","ind":"2"};{"sq":"grey-hexagon.svg","ind":"5"};{"sq":"yellow-hexagon-line-circle.svg","ind":"6"};{"sq":"grey-hexagon.svg","ind":"7"};{"sq":"red-hexagon-circle.svg","ind":"8"};{"sq":"grey-hexagon.svg","ind":"9"};{"sq":"red-hexagon.svg","ind":"10"}'/>
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"};{"sq":"grey-hexagon.svg","ind":"1"};{"sq":"red-hexagon.svg","ind":"2"};{"sq":"grey-hexagon.svg","ind":"3"};{"sq":"red-hexagon.svg","ind":"4"};{"sq":"grey-hexagon.svg","ind":"7"};{"sq":"red-hexagon.svg","ind":"8"};{"sq":"grey-hexagon.svg","ind":"9"};{"sq":"red-hexagon.svg","ind":"10"}'/>
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"};{"sq":"grey-hexagon.svg","ind":"1"};{"sq":"red-hexagon.svg","ind":"2"};{"sq":"grey-hexagon.svg","ind":"3"};{"sq":"red-hexagon.svg","ind":"4"};{"sq":"grey-hexagon.svg","ind":"7"};{"sq":"red-hexagon.svg","ind":"8"};{"sq":"grey-hexagon.svg","ind":"9"};{"sq":"red-hexagon.svg","ind":"10"};{"sq":"red-hexagon-circle-start.svg","ind":"12"};{"sq":"red-hexagon.svg","ind":"13"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"};{"sq":"grey-hexagon.svg","ind":"1"};{"sq":"yellow-hexagon.svg","ind":"2"};{"sq":"grey-hexagon.svg","ind":"5"};{"sq":"yellow-hexagon.svg","ind":"6"};{"sq":"grey-hexagon.svg","ind":"7"};{"sq":"yellow-hexagon.svg","ind":"8"};{"sq":"grey-hexagon.svg","ind":"11"};{"sq":"yellow-hexagon.svg","ind":"12"};{"sq":"grey-hexagon.svg","ind":"14"};{"sq":"yellow-hexagon.svg","ind":"15"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"};{"sq":"grey-hexagon.svg","ind":"1"};{"sq":"yellow-hexagon.svg","ind":"2"};{"sq":"grey-hexagon.svg","ind":"5"};{"sq":"yellow-hexagon.svg","ind":"6"};{"sq":"grey-hexagon.svg","ind":"7"};{"sq":"yellow-hexagon.svg","ind":"8"};{"sq":"grey-hexagon.svg","ind":"11"};{"sq":"yellow-hexagon.svg","ind":"12"};{"sq":"grey-hexagon.svg","ind":"14"};{"sq":"yellow-hexagon.svg","ind":"15"}'/>
      <AniHex squares='{"sq":"yellow-hexagon.svg","ind":"0"};{"sq":"grey-hexagon.svg","ind":"1"};{"sq":"yellow-hexagon.svg","ind":"2"};{"sq":"grey-hexagon.svg","ind":"5"};{"sq":"yellow-hexagon.svg","ind":"6"};{"sq":"grey-hexagon.svg","ind":"7"};{"sq":"yellow-hexagon.svg","ind":"8"};{"sq":"grey-hexagon.svg","ind":"11"};{"sq":"yellow-hexagon-line.svg","ind":"12"};{"sq":"red-hexagon-circle.svg","ind":"13"};{"sq":"red-hexagon.svg","ind":"14"}'/>
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"};{"sq":"grey-hexagon.svg","ind":"1"};{"sq":"red-hexagon.svg","ind":"2"};{"sq":"grey-hexagon.svg","ind":"3"};{"sq":"red-hexagon.svg","ind":"4"};{"sq":"grey-hexagon.svg","ind":"7"};{"sq":"red-hexagon.svg","ind":"8"};{"sq":"grey-hexagon.svg","ind":"9"};{"sq":"red-hexagon.svg","ind":"10"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"};{"sq":"grey-hexagon.svg","ind":"3"};{"sq":"blue-hexagon.svg","ind":"4"};{"sq":"grey-hexagon.svg","ind":"5"};{"sq":"blue-hexagon.svg","ind":"6"};{"sq":"grey-hexagon.svg","ind":"9"};{"sq":"blue-hexagon.svg","ind":"10"};{"sq":"grey-hexagon.svg","ind":"11"};{"sq":"blue-hexagon.svg","ind":"12"};{"sq":"grey-hexagon.svg","ind":"14"};{"sq":"yellow-hexagon.svg","ind":"15"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"};{"sq":"grey-hexagon.svg","ind":"3"};{"sq":"blue-hexagon.svg","ind":"4"};{"sq":"grey-hexagon.svg","ind":"5"};{"sq":"blue-hexagon.svg","ind":"6"};{"sq":"grey-hexagon.svg","ind":"9"};{"sq":"blue-hexagon.svg","ind":"10"};{"sq":"grey-hexagon.svg","ind":"11"};{"sq":"yellow-hexagon-circle.svg","ind":"12"};{"sq":"yellow-hexagon.svg","ind":"13"};{"sq":"grey-hexagon.svg","ind":"14"};{"sq":"yellow-hexagon.svg","ind":"15"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"};{"sq":"grey-hexagon.svg","ind":"3"};{"sq":"blue-hexagon.svg","ind":"4"};{"sq":"grey-hexagon.svg","ind":"5"};{"sq":"blue-hexagon.svg","ind":"6"};{"sq":"grey-hexagon.svg","ind":"9"};{"sq":"blue-hexagon.svg","ind":"10"};{"sq":"grey-hexagon.svg","ind":"11"};{"sq":"blue-hexagon-line-circle.svg","ind":"12"};{"sq":"yellow-hexagon-circle.svg","ind":"13"};{"sq":"grey-hexagon.svg","ind":"14"};{"sq":"yellow-hexagon.svg","ind":"15"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"};{"sq":"grey-hexagon.svg","ind":"3"};{"sq":"blue-hexagon.svg","ind":"4"};{"sq":"grey-hexagon.svg","ind":"5"};{"sq":"yellow-hexagon-circle.svg","ind":"6"};{"sq":"grey-hexagon.svg","ind":"7"};{"sq":"yellow-hexagon.svg","ind":"8"};{"sq":"grey-hexagon.svg","ind":"11"};{"sq":"yellow-hexagon.svg","ind":"12"};{"sq":"grey-hexagon.svg","ind":"14"};{"sq":"blue-hexagon.svg","ind":"15"}'/>
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"};{"sq":"grey-hexagon.svg","ind":"1"};{"sq":"red-hexagon.svg","ind":"2"};{"sq":"grey-hexagon.svg","ind":"3"};{"sq":"red-hexagon.svg","ind":"4"};{"sq":"grey-hexagon.svg","ind":"7"};{"sq":"red-hexagon.svg","ind":"8"};{"sq":"grey-hexagon.svg","ind":"9"};{"sq":"red-hexagon.svg","ind":"10"};{"sq":"blue-hexagon-circle.svg","ind":"13"};{"sq":"grey-hexagon.svg","ind":"14"};{"sq":"blue-hexagon.svg","ind":"15"}'/>
    </div>
    <div style="display:flex; margin-top:-15px;">
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"};{"sq":"grey-hexagon.svg","ind":"3"};{"sq":"blue-hexagon.svg","ind":"4"};{"sq":"grey-hexagon.svg","ind":"5"};{"sq":"blue-hexagon.svg","ind":"6"};{"sq":"grey-hexagon.svg","ind":"9"};{"sq":"blue-hexagon.svg","ind":"10"};{"sq":"grey-hexagon.svg","ind":"11"};{"sq":"blue-hexagon.svg","ind":"12"};{"sq":"grey-hexagon.svg","ind":"14"};{"sq":"blue-hexagon.svg","ind":"15"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"};{"sq":"grey-hexagon.svg","ind":"3"};{"sq":"blue-hexagon.svg","ind":"4"};{"sq":"grey-hexagon.svg","ind":"5"};{"sq":"blue-hexagon.svg","ind":"6"};{"sq":"grey-hexagon.svg","ind":"9"};{"sq":"blue-hexagon.svg","ind":"10"};{"sq":"grey-hexagon.svg","ind":"11"};{"sq":"blue-hexagon.svg","ind":"12"};{"sq":"grey-hexagon.svg","ind":"14"};{"sq":"blue-hexagon.svg","ind":"15"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"};{"sq":"grey-hexagon.svg","ind":"3"};{"sq":"blue-hexagon.svg","ind":"4"};{"sq":"grey-hexagon.svg","ind":"5"};{"sq":"blue-hexagon.svg","ind":"6"};{"sq":"grey-hexagon.svg","ind":"9"};{"sq":"blue-hexagon.svg","ind":"10"};{"sq":"grey-hexagon.svg","ind":"11"};{"sq":"blue-hexagon.svg","ind":"12"};{"sq":"grey-hexagon.svg","ind":"14"};{"sq":"blue-hexagon.svg","ind":"15"}'/>
      <AniHex squares='{"sq":"blue-hexagon.svg","ind":"0"};{"sq":"grey-hexagon.svg","ind":"3"};{"sq":"blue-hexagon.svg","ind":"4"};{"sq":"grey-hexagon.svg","ind":"5"};{"sq":"blue-hexagon.svg","ind":"6"};{"sq":"grey-hexagon.svg","ind":"9"};{"sq":"blue-hexagon.svg","ind":"10"};{"sq":"grey-hexagon.svg","ind":"11"};{"sq":"blue-hexagon.svg","ind":"12"};{"sq":"grey-hexagon.svg","ind":"14"};{"sq":"blue-hexagon.svg","ind":"15"}'/>
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"};{"sq":"grey-hexagon.svg","ind":"1"};{"sq":"red-hexagon.svg","ind":"2"};{"sq":"grey-hexagon.svg","ind":"3"};{"sq":"blue-hexagon-circle.svg","ind":"4"};{"sq":"grey-hexagon.svg","ind":"5"};{"sq":"blue-hexagon.svg","ind":"6"};{"sq":"grey-hexagon.svg","ind":"9"};{"sq":"blue-hexagon.svg","ind":"10"};{"sq":"grey-hexagon.svg","ind":"11"};{"sq":"blue-hexagon.svg","ind":"12"};{"sq":"grey-hexagon.svg","ind":"14"};{"sq":"blue-hexagon.svg","ind":"15"}'/>
      <AniHex squares='{"sq":"red-hexagon.svg","ind":"0"};{"sq":"grey-hexagon.svg","ind":"1"};{"sq":"red-hexagon.svg","ind":"2"};{"sq":"grey-hexagon.svg","ind":"3"};{"sq":"red-hexagon.svg","ind":"4"};{"sq":"grey-hexagon.svg","ind":"7"};{"sq":"red-hexagon.svg","ind":"8"};{"sq":"grey-hexagon.svg","ind":"9"};{"sq":"blue-hexagon-circle.svg","ind":"10"};{"sq":"grey-hexagon.svg","ind":"11"};{"sq":"blue-hexagon.svg","ind":"12"};{"sq":"grey-hexagon.svg","ind":"14"};{"sq":"blue-hexagon.svg","ind":"15"}'/>
    </div>
  </div>
</div>

<p v-click="1" class="flex justify-center absolute top-95% left-12%"> Previous State </p>
<p class="absolute top-95% left-72%"> Current State </p>

</div>

---

## Conclusion

* <strong>Our Results:</strong>
  * Universality of recombination in square and triangular grids for maps with <strong>three parts</strong> 

* <strong>Future Work:</strong>
  * More than three districts
  * Improved asymptotics (Mixing Time)
