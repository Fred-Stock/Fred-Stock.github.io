# Modular Robots

<div class="flex flex-col items-center">

<iframe width="560" height="315" src="https://www.youtube.com/embed/fsVJuN75vzE?si=6GaZ4fG6fEWuGmJE&amp;start=152" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</div>

---
transition: none
---

# Modular Robots

- Moves are subject to two constraints

<div class="flex flex-col items-center">
    <img v-click.hide=0 src="/ModularRobots/backbone-full.svg" style="width:800px;">
    <img v-click src="/ModularRobots/free-space.svg" style="width:800px;">
</div>

<!--
List off different models of modular robot
-->

---
transition: none

layout: iframe-zoom
url: https://modular-robotics-group.github.io/modular-robotics/WebVis/index.html?presenting=true&file=Slide-Model 
cropTop: -100
width: 125
---

# Sliding Cubes

- $U$ is any polycube (configuration) composed of $n$ unit (hyper-)cubes
- Transform between configurations via <font color="yellow">**slide rules**</font>

<!-- -->

---
transition: none
---

# Previous Work in 2D

- *Pushing Squares Around* (Dumitrescu and Pach, 2004)
    
- *Compacting Squares: Input-Sensitive In-Place Reconfiguration of Sliding Squares* (ADKKPSSUW, 2022) 

- *Characterizing Universal Reconfigurability of Modular Pivoting Robots* (ADGHHKKLPS, 2020)
 


<!--
SoCG paper + CCCG
-->

--- 
transition: none

clicks: 1

fonts:
    italic: true
--- 

# Standard Technique

<v-click at="1"> 
    <em><font color="yellow"> In-Place Reconfiguration </font></em>
</v-click>

<div class="flex flex-col items-center">
    <img v-click.hide=0 src="/ModularRobots/gen-reconf.svg" style="width:700px;margin-top:5em;padding:.5em">
    <img v-click=[1,2] src="/ModularRobots/in-place.svg" style="width:700px;padding:.5em">
</div>


---
transition: none
dragPos:
  lemmaPos: Left,Top,Width,Height

clicks: 1
---

# Three Dimensions

- There is a simple algorithm (Fitch, Butler, Rus, 2003)


<div class="flex flex-col items-center">
<div class="grid grid-cols-2">

<img src="/general/rus-2003-alg-title.png" style="width:400px">

</div>
</div>

<img v-drag="[586,233,371,143]" v-click src="/general/rus-wrong-lem.png">


---
transition: none
dragPos:
  lemmaPos: Left,Top,Width,Height
---

# Three Dimensions

- There is a simple algorithm (Fitch, Butler, Rus, 2003)


<img v-drag="[588,69,371,143]" src="/general/rus-wrong-lem.png">


<v-clicks class="darklist">

1) <span v-mark="{at:[1,2], type:'box', iterations:'1', color:'yellow'}"> Set $\textbf{z}$ to be some module with maximal $z$-coordinate </span>

2) <span v-mark="{at:[2,3], type:'box', iterations:'1', color:'yellow'}"> Use $\texttt{Lemma 1}$ to find a module $\textbf{m}$ on the outer boundary </span>

3) <span v-mark="{at:[3,4], type:'box', iterations:'1', color:'yellow'}"> Move $\textbf{m}$ to the $z$-most face of $\textbf{z}$ </span>

4) <span v-mark="{at:'4', type:'box', iterations:'1', color:'yellow'}"> Set $\textbf{z} = \textbf{m}$ and repeat 2-4 </span>

</v-clicks>

<div v-drag="[385,239,265,272]">

<img v-click=[1,2] src="/ModularRobots/rus1.svg">

<img v-click=[2,3] src="/ModularRobots/rus-2.svg">

<img v-click=[3,4] src="/ModularRobots/rus-3.svg">

<img v-click=[4,5] src="/ModularRobots/rus-4.svg">

<img v-click=[5,6] src="/ModularRobots/rus-5.svg" style="scale:.7">

<img v-click="6" src="/ModularRobots/rus-6.svg" style="scale:.7">

</div>

---
layout: iframe-zoom
url: https://modular-robotics-group.github.io/modular-robotics/WebVis/index.html?presenting=true&file=locate-and-free
cropTop: 0
width: 150
---

# Three Dimensions


---

# Three Dimensions

- <b> ... This is broken (Miltzow, Parada, Sonke, Speckman, and Wulms, 2020) </b>

<div class="flex flex-col items-center">
<div class="grid grid-cols-2 gap-.5em">

<img src="/general/rus-wrong-lem-2.png" style="width:300px">

<iframe width="400" height="225" src="https://www.youtube.com/embed/7PtRdF5cYJY?si=FpMm9X6U112Dlm0W&amp;start=195&mute=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</div>
</div>



<!-- 
- Incorrect! there might be no movable modules on the boundary 
    - <i> Hiding Sliding Cubes: Why Reconfiguration of Modular Robots is Hard </i> Miltzow, Parada, Sonke, Speckman, and Wulms
<div class="flex flex-col items-center">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/7PtRdF5cYJY?si=FpMm9X6U112Dlm0W&amp;start=195&mute=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div> -->

<!--
Russ paper and media expo
-->

---
transition: none

dragPos:
  image: Left,Top,Width,Height,Rotate
---

# Pushing (hyper-)cubes Around (Abel & Kominers)

<v-clicks class="darklist">

- Introduced $\texttt{LocateAndFree}$ 

    - If there is no movable module on the outer boundary, then it makes one movable.

- Only proves a bound of $O(n^3)$ moves

    - Best known lower bound is $O(n^2)$

</v-clicks>

<img v-drag="[423,200,498,242]" pos="image" src="/ModularRobots/pushing-hyper-cubes.png">

---
transition: none

clicks: 2

dragPos:
  image: Left,Top,Width,Height,Rotate
  image2: Left,Top,Width,Height,Rotate
  image3: Left,Top,Width,Height,Rotate
---

# Our Contribution

<div v-click=2>

- <i>A Universal In-Place Reconfiguration Algorithm for Sliding Cube-Shaped Robots in a Quadratic Number of Moves</i> (Abel, Akitaya, Kominers, Korman, S., 2024)
- resolved issues in original preprint 
- Improved analysis giving a tight $\Theta(n^2)$ moves
- Input-sensitive in-place algorithm

</div>

<img v-click.hide=0 v-drag="[172,114,735,357]" pos="image" src="/ModularRobots/pushing-hyper-cubes.png">

<img v-click=[1,2] v-drag="[172,110,740,360]" pos="image2" src="/ModularRobots/pushing-hyper-cubes-annotated.png">

<img v-click=[2,3] v-drag="[366,228,545,242]" pos="image3" src="/ModularRobots/new-arxiv-post.png">

---
transition: none

dragPos: 
    naLem:Left,Top,Width,Height
    naFig:Left,Top,Width,Height
---

# $\texttt{LocateAndFree}$

<img v-drag="[426,188,513,66]" src="/ModularRobots/na-lemma-socg.png">


- There may not be a mobile module on the boundary but there will be something "almost mobile" 
    - "Almost mobile" $\Rightarrow$ splits $C$ into exactly two pieces, boundary and interior

<div style="padding-top:1.5em;">
<img v-click=[1,2] src="/ModularRobots/nna1.svg" style="width:200px;">
<img v-click=[2,3] src="/ModularRobots/nna2.svg" style="width:200px;">
<img v-click=[3,4] src="/ModularRobots/nna3.svg" style="width:200px;">
<img v-click=[4,5] src="/ModularRobots/landf1.svg" style="width:200px;">
<img v-click=[5,6] src="/ModularRobots/landf3.svg" style="width:200px;">
<img v-click=[6,7] src="/ModularRobots/lemma2-case2-3.svg" style="width:300px;">
<img v-click=[7,8] src="/ModularRobots/lemma2-case2-4.svg" style="width:300px;">
<img v-click=[8,9] src="/ModularRobots/lemma2-case2-5.svg"style="width:300px;">
<img v-click=[9,10] src="/ModularRobots/lemma2-case2-6.svg" style="width:300px;">
<img v-click="10" src="/ModularRobots/lemma2-case2-7.svg" style="width:300px;">
</div>



---

# Locate and Free Algorithm

<v-clicks class="darklist">

1) <span v-mark="{at:[1,2], type:'box', iterations:'1', color:'yellow'}"> Set $\textbf{z}$ to be some module with maximal $z$-coordinate </span>

2) <span v-mark="{at:[2,3], type:'box', iterations:'1', color:'yellow'}"> Use <font color="red"> <del> lemma 1 </del> $\Rightarrow$ </font>  $\texttt{LocateAndFree}$ to free a module $\textbf{m}$ on the outer boundary </span>

3) <span v-mark="{at:[3,4], type:'box', iterations:'1', color:'yellow'}"> Move $\textbf{m}$ to the $z$-most face of $\textbf{z}$ </span>

4) <span v-mark="{at:4, type:'box', iterations:'1', color:'yellow'}"> Set $\textbf{z} = \textbf{m}$ and repeat steps 2-4 </span>

</v-clicks>


<div v-drag="[476,222,265,272]">

<img v-click=[1,2] src="/ModularRobots/rus1.svg">

<img v-click=[2,3] src="/ModularRobots/rus-2.svg">

<img v-click=[3,4] src="/ModularRobots/rus-3.svg">

<img v-click=[4,5] src="/ModularRobots/rus-4.svg">

<img v-click=[5,6] src="/ModularRobots/rus-5.svg" style="scale:.7">

<img v-click="6" src="/ModularRobots/rus-6.svg" style="scale:.7">

</div>

---

# An Input-Sensitive In-Place Algorithm

<v-clicks class="darklist">

1) <span v-mark="{at:[1,3], type:'box', iterations:'1', color:'yellow'}"> Use $\texttt{LocateAndFree}$ to produce a <strong><em><font color="yellow">scaffolding</font></em></strong> </span>

2) <span  v-mark="{at:[3,5], type:'box', iterations:'1', color:'yellow'}"> Sweep this scaffoling to <strong><em><font color="yellow">meld</font></em></strong> layers of the configuration together </span>

3) <span  v-mark="{at:5, type:'box', iterations:'1', color:'yellow'}"> Turn the configuration into a <strong><em><font color="yellow">compact</font></em></strong> form </span>

</v-clicks>

<div v-drag="[476,222,265,272]">

<img v-click=[1,2] src="/ModularRobots/inplace-1.svg">

<img v-click=[2,3] src="/ModularRobots/inplace-2.svg" style="scale:.8">

<img v-click=[3,4] src="/ModularRobots/inplace-3.svg" style="scale:.8;padding-top:-1em;">

<img v-click=[4,5] src="/ModularRobots/clumps.svg" style="scale:1.2;">

<img v-click="5" src="/ModularRobots/Compact.svg" style="scale:1.5; padding-top:6em;">


</div>

---

# Scaffolding

1) Use $\texttt{LocateAndFree}$ to produce a <strong><em><font color="yellow">scaffolding</font></em></strong>

<!-- 
<div class="flex flex-col items-center">
    <img src="/ModularRobots/scaffolding.svg" style="width:700px">
</div>

layout: iframe-zoom
url: https://modular-robotics-group.github.io/modular-robotics/WebVis/index.html?presenting=true&file=scaffolding
cropTop: -100
width: 125

# Scaffolding -->


---

# Melding

2) Sweep this scaffoling to <strong><em><font color="yellow">meld</font></em></strong> layers of the configuration together

<div class="flex flex-col items-center">
    <img src="/ModularRobots/Melding.svg" style="width:700px">
</div>

---
layout: iframe-zoom
url: https://modular-robotics-group.github.io/modular-robotics/WebVis/index.html?presenting=true&file=melding
cropTop: 0
width: 150
---

# Melding


---
transition: none
---

# Compact Reconfiguration

3) Turn the configuration into a <strong><em><font color="yellow">compact</font></em></strong> form

<div class="flex flex-col items-center">
    <img v-click.hide=0 src="/ModularRobots/clumps.svg" style="padding:.25em;">
    <img v-click src="/ModularRobots/Compact.svg" style="padding-top:8em;padding-left:.25em;padding-right:.25em;padding:.25;scale:1.5;">
</div>


---
layout: iframe-zoom
url: https://modular-robotics-group.github.io/modular-robotics/WebVis/index.html?presenting=true&file=compactform
cropTop: 0
width: 150
---

# Compact Reconfiguration


---
transition: none
dragPos:
  image: Left,Top,Width,Height,Rotate
---

# Simultaneous Result

- <i>Optimal In-Place Compaction of Sliding Cubes</i> (Kostitsyna, Ophelders, Parada, Peters, Sonke, Speckman)
- Different algorithmic idea, also in-place and input-sensitive
    - Better best-case bounds than ours

<img v-drag="[395,168,528,313]" pos="image" src="/ModularRobots/dutch-team.png"/>

---
transition: none
---

# Simultaneous Result

<iframe width="700" height="394" src="https://www.youtube.com/embed/cRn-ZRuOZ18?si=RBd8GKevswkDozO2&mute=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<!-- Dutch paper -->

---
transition: none
dragPos:
  image: Left,Top,Width,Height,Rotate
  overview: Left,Top,Width,Height,Rotate
---

# Matching Their Algorithm

- Only $O(1)$ musketeers
- Roughly, modules only move to new positions with lesser sum of coordinates
    - Decrease proportional to the required moves

<img v-drag="[441,202,394,327]" pos=image src="/ModularRobots/improved-alg.png">

<img v-drag="[46,225,356,269]" pos=overview src="/ModularRobots/musketeers.png">

<!--
Our CCCG Paper
-->
