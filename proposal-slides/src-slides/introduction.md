# Reconfiguration Problems

- Reconfiguration problems are defined by

  <v-clicks class="darklist">

  - A universe of objects <font color="yellow"><strong> $U$ </strong></font>

  - A set of <font color="yellow">rules</font> that relate pairs of elements <strong> $a,b \in U$ </strong>
  </v-clicks>
<!--
Notes for slide 2
-->

---
transition: none
dragPos:
  fifteen: Left,Top,Width,Height,Rotate
  vsphere: Left,Top,Width,Height,Rotate
  sokoban: Left,Top,Width,Height,Rotate
---

# Puzzles

<v-clicks>
<img v-drag="[37,175,347,347]" pos="fifteen" src="/general/15-puzzle.jpg">

<img v-drag="[278,21,546,243]" pos="vshpere" src="/general/rubkis-cube.png" style="background:white">

<img v-drag="[544,202,288,320]" pos="sokoban" src="/general/sokoban.gif">
</v-clicks>

---
transition: none
dragPos:
  object: Left,Top,Width,Height,Rotate
  rule: Left,Top,Width,Height

clicks: 1
---

# Example: Rubiks Cube

- $U$ = An arrangement of colored faces

<v-clicks class="darklist">

- Rules = Rotating a $3 \times 3$ section of the cube

</v-clicks>

<img v-click.hide v-drag="[433,255,162,191]" pos="object" src="/general/rubik-single.svg">

<img v-click="1" v-drag="[159,250,700,206]" pos="rule" src="/general/rubik-rule.svg">

---
transition: none

clicks: 5
---

# Flip Graphs 

<span v-click="1">

- $U$ = a triangulation of a point set

</span>
<span v-click="2">

- Rule = Flipping an edge

</span>

<div class="flex flex-col items-center">

<img v-click.hide=0 src="/general/tri-flips-0.svg" style="width:400px;">

<img v-click=[1,2] src="/general/tri-flips-1.svg" style="width:400px">

<img v-click=[2,3] src="/general/tri-flips-2.svg" style="width:400px">

<img v-click=[3,4] src="/general/tri-flips-3.svg" style="width:400px">

<img v-click=[4,5] src="/general/tri-flips-4.svg" style="width:400px">

<img v-click="5" src="/general/tri-flips-5.svg" style="width:400px">

</div>

---
transition: none
dragPos:
  graphPos: Left,Top,Width,Height
---

# Configuration Space


<font color="white"> 

A graph representing related objects of $U$ 

</font>

<v-clicks class="darklist">

  - Objects of $U$ are nodes

  - $a,b \in U$ share an edge if related by a reconfiguration rule

</v-clicks>

<div v-click>

<strong>We usually ask:</strong>

<div text-primary font-bold> 
  
 Is the configuration space of < Insert Problem Here > connected? 

</div>
</div>

<div v-drag="[544,243,319,336,-46]" >
  <img v-click=[1,2] src="/figures/configuration-graph-nodes.svg" style="scale=.5">
  <img v-click="2" src="/figures/configuration-graph.svg" style="scale=.5">
</div>
<!-- -->

<!--
transition: none

clicks: 8

# Non-deterministic Constraint Logic 

- Hearn & Demaine 2009

<div class="flex flex-col items-center">
<img v-click.hide=0 src="/general/ncl-paper-title.png" style="width:600px">

<img v-click=[1,2] src="/general/ncl-1.svg">

<img v-click=[2,3] src="/general/ncl-2.svg">

<img v-click=[3,4] src="/general/ncl-3.svg">

<img v-click=[4,5] src="/general/ncl-4.svg">

<img v-click=[5,6] src="/general/ncl-5.svg">

<img v-click=[6,7] src="/general/ncl-6.svg">

<img v-click=[7,8] src="/general/ncl-7.svg">

<img v-click=[8,9] src="/general/ncl-8.svg">

</div>
-->

---

# What This is About

1) Redistricting
2) Modular Robots (Sliding Cubes)


---
dragPos:
  map1: 514,181,41,40
  map2: 649,180,44,40
  map3: 514,335,40,40
  map4: 648,335,40,40
  map5: Left,Top,Width,Height
---

# Redistricting


<div v-click.hide class="flex flex-col items-center" style="margin-top:10em">

  <img src="/general/gerrymandering-example.svg" style="scale:3">

</div>

<div v-click=[1,2] class="flex flex-col items-center" style="margin-top:.5em">

  <img src="/figures/2-3.svg" style="scale:3.6">

</div>

<div v-click=[2,3] class="flex flex-col items-center" style="margin-top:0em">

  <img src="/figures/0-5.svg" style="scale:3.6">

</div>

<div v-click="3" class="flex flex-col items-center" style="margin-top:-5em">

  <img src="/general/gerrymandering-2a.svg" style="scale:1.2">

</div>

<v-drag v-click="3" pos="map1">

<font color="lightpink">2</font> <font color="purple">3</font>

</v-drag>

<v-drag v-click="3" pos="map2">

<font color="lightpink">3</font> <font color="purple">2</font>

</v-drag>

<v-drag v-click="3" pos="map3">

<font color="lightpink">2</font> <font color="purple">3</font>

</v-drag>

<v-drag v-click="3" pos="map4">

<font color="lightpink">0</font> <font color="purple">5</font>

</v-drag>

---
transition: none

dragPos:
  case: Left,Top,Width,Height,Rotate
  caseT: Left,Top,Width,Height,Rotate
  caseH: Left,Top,Width,Height,Rotate
  caseE: Left,Top,Width,Height,Rotate
  case1: Left,Top,Width,Height,Rotate
  case2: Left,Top,Width,Height,Rotate
  case3: Left,Top,Width,Height,Rotate
  case4: Left,Top,Width,Height,Rotate
  case5: Left,Top,Width,Height,Rotate

#   square: Left,Top,Width,Height,Rotate
---

# Redistricting 


<!-- <v-clicks> -->


<div class="flex flex-col items-center">
  <img src="/Redistricting/legal-challenges.png" style="height:400px">
</div>

<!-- <img v-drag="[43,80,462,368]" src="/Redistricting/case1.png" style='border:2px solid #555555'>

<img v-drag="[101,140,436,342]" pos="caseT" src="/Redistricting/case4.png" style='border:2px solid #555555'>

<img v-drag="[204,203,409,357]" pos="caseH" src="/Redistricting/case3.png" style='border:2px solid #555555'>

<img v-drag="[364,70,375,302]" pos="caseE" src="/Redistricting/case2.png" style='border:2px solid #555555'>

<img v-drag="[397,123,322,330]" pos="case1" src="/Redistricting/case5.png" style='border:2px solid #555555'>

<img v-drag="[453,171,301,314]" pos="case2" src="/Redistricting/case6.png" style='border:2px solid #555555'>

<img v-drag="[537,76,393,377,-27]" pos="case3" src="/Redistricting/case7.png" style='border:2px solid #555555'>

<img v-drag="[165,42,387,369,24]" pos="case4" src="/Redistricting/case8.png" style='border:2px solid #555555'>

<img v-drag="[363,75,393,405,-13]" pos="case5" src="/Redistricting/case9.png" style='border:2px solid #555555'>

</v-clicks> -->

---
transition: none

clicks: 2
---  

# Modular Robots 


<div class="flex flex-col items-center">

<iframe v-click.hide=0 width="560" height="315" src="https://www.youtube.com/embed/fsVJuN75vzE?si=6GaZ4fG6fEWuGmJE&amp;start=152" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe v-click=[1,2] width="560" height="315" src="https://www.youtube.com/embed/4oSavAHf0dg?si=5ohGWJJYvLaacVf0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe v-click=[2,3] width="560" height="315" src="https://www.youtube.com/embed/3R3o74Afx5Y?si=41Bdr-efce3CZYXE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</div>
<!-- -->


---

# Order of Topics

1) Redistricting in Triangular and Square Grids
2) Sequential Sliding (Hyper-)Cubes
3) Parallel Siding Squares
