# Sliding Squares in Parallel

<font color="lightgrey">
Hugo Akitaya, Sándor Fekete, Peter Kramer, Saba Molaei, Christian Rieck, Frederick Stock, Tobias Wallner

European Symposium on Algorithms 2025
</font>


---

# Parallel Sliding Squares

<v-clicks class="darklist">

- Same moves (slides and convex transitions)
- Same constraints (free space and backbone)
- Multiple robots may move in one time step
- We compare algorithms by <font color="yellow">**makespan**</font> instead of number of moves
    - Number of time steps to complete the reconfiguration

</v-clicks>
<!--
ESA Paper
-->

---
transition: none
---

# Related Work

<v-clicks>
    
- Parallel reconfiguration in <font color="yellow"> less restricted models </font>
    - [ACDDFLORSW, 2009] *Linear Reconfiguration of Cube Style Modular Robots*
    - Fekete, Keldenich, Kosfield, Rieck, Scheffer, 2023: *Coordinated Connected Motion Planning with Bounded Stretch*

- An algorithm with $O(n)$ makespan

    - Michail, Skretas, Spirakis, 2019: *On the Transformation Capability of Feasible Mechanisms for Programmable Matter*

    - <font color="yellow"> Does not work in general </font>

</v-clicks>
<!-- some related work from ESA paper -->

---
transition: none

dragPos:
  image: Left,Top,Width,Height,Rotate
---

# Our Contribution
- *Sliding Squares in Parallel* (Akitaya, Fekete, Kramer, Molaei, Rieck, <strong>S</strong>, Wallner, 2025)
- First Parallel Algorithm for reconfiguration of sliding square robots

<img v-drag="[225,164,570,342]" pos="image" src="/general/esa-paper-title.png">

---
transition: none
---

# Our Model of Parallel Squares

<font color="lightgrey"> One move takes one timestep </font> 

<div class="flex flex-col items-center">
    <img src="/ModularRobots/collision-types.png" style="width:500px">
</div>

---
transition: none

layout: iframe-zoom
url: https://modular-robotics-group.github.io/modular-robotics/WebVis/index.html?presenting=true&file=parallel-dissallowed 
cropTop: 0
width: 125
---

# Our Model of Parallel Squares

<!-- -->


---
transition: none
dragPos:
  planarSat: Left,Top,Width,Height
  construction: Left,Top,Width,Height
---

# Complexity of Parallel Squares

- Finding an optimal schedule of makespan 1 is NP-hard 
    - We reduce from Planar Monotone 3Sat

<!-- <SlidevVideo controls width=560 height=315>
        <source src="/ModularRobots/np-hardness.mp4"/>
</SlidevVideo> -->

<div v-click.hide class="flex flex-col items-center" style="padding:4.5em;scale:1.5;">
    <img  src="/ModularRobots/planar-monotone-3sat.svg" style="background:white;padding:1em;">
</div>


<img v-click="1" v-drag="[631,55,314,186]" src="/ModularRobots/planar-monotone-3sat.svg" style="background:white;padding:1em;">

<img v-click="2" v-drag="[24,236,606,281]" src="/ModularRobots/np-hardness-construction.svg" style="background:white;padding:1em;">

---
transition: none
layout: iframe-zoom
url: https://modular-robotics-group.github.io/modular-robotics/WebVis/index.html?presenting=true&file=parallel-squares-nphard&speed=1
cropTop: 0
width: 150
---

# Complexity of Parallel Squares

---
transition: none

layout: iframe-zoom
url: https://modular-robotics-group.github.io/modular-robotics/WebVis/index.html?presenting=true&file=parallel-squares-aproxfactor&speed=1
cropTop: 0
width: 150
---

# Complexity of Parallel Squares

<font color="white">

$\Rightarrow$ This problem is not FPT in the makespan
</font>

$\Rightarrow$ This problem cannot be approximated within a factor of 2 


---

# Positive Result

##### <em> <font color="yellow"> We can compute a weakly in-place schedule of $O(P_1 + P_2)$ transformations in polynomial time </font> </em>

---
transition: none
dragPos:
  scaleSq: Left,Top,Height,Width
  strips: Left,Top,Height,Width
---

# Our Algorithm: An Observation

- When a configuration is <em><strong><font color="yellow">3-scaled</font></strong></em> this is an easy problem

<img v-drag="[341,156,244,244]" src="/ModularRobots/scaled-strips.svg" style="background:white;">

<!-- Second because it needs to be ontop of the previous -->
<img v-click v-drag="[130,313,300,131]" src="/ModularRobots/scaled-to-square.svg">


---
transition: none

layout: iframe-zoom
url: https://modular-robotics-group.github.io/modular-robotics/WebVis/index.html?presenting=true&file=scaled-strip-south&speed=1
cropTop: 0
width: 150
---

# Our Algorithm: An Observation

- When a configuration is <em><strong><font color="yellow">3-scaled</font></strong></em> this is an easy problem



---
transition: none
dragPos:
  scaleSq: Left,Top,Height,Width
  strips: Left,Top,Height,Width
  stripsMv: Left,Top,Height,Width
  stripsFinal: Left,Top,Height,Width
---

# Our Algorithm: An Observation

- When a configuration is <em><strong><font color="yellow">3-scaled</font></strong></em> this is an easy problem

<img v-click.hide v-drag="[341,156,244,244]" src="/ModularRobots/scaled-strips.svg" style="background:white;">

<div v-click="1" class="grid grid-cols-3 gap-50 absolute top-70 left-50">

<img src="/ModularRobots/scaled-strips.svg" style="background:white;scale:3;">

<img src="/ModularRobots/scaled-strips-mv.svg" style="background:white;scale:3;">

<img src="/ModularRobots/scaled-strips-final.svg" style="background:white;scale:3;">

</div>


---
transition: none
dragPos:
  hist1: Left,Top,Width,Height
  hist2: Left,Top,Width,Height
  hist3: Left,Top,Width,Height
---

# Our Algorithm: An Observation

- When a configuration is <em><strong><font color="yellow">3-scaled</font></strong></em> this is an easy problem

<div  class="flex flex-col items-center" style="padding-top:4em;scale:3.5">

<img v-click.hide="1" src="/ModularRobots/histogram.svg" style="background:white;padding:.3em;">

<img v-click=[1,2] src="/ModularRobots/histogram-bisectors.svg" style="background:white;">

<img v-click=[2,3] src="/ModularRobots/histogram-reconfig.svg" style="background:white;padding:.3em;">

<img v-click="3" src="/ModularRobots/histogram-final.svg" style="background:white;padding:.3em;">

</div>


---
transition: none

layout: iframe-zoom
url: https://modular-robotics-group.github.io/modular-robotics/WebVis/index.html?presenting=true&file=scaled-move&speed=1
cropTop: 0
width: 150
---

# Our Algorithm: An Observation

- When a configuration is <em><strong><font color="yellow">3-scaled</font></strong></em> this is an easy problem


---
transition: none

layout: iframe-zoom
url: https://modular-robotics-group.github.io/modular-robotics/WebVis/index.html?presenting=true&file=scaled-histogram&speed=1
cropTop: 0
width: 150
---

# Our Algorithm: An Observation

- When a configuration is <em><strong><font color="yellow">3-scaled</font></strong></em> this is an easy problem

---

# Our Algorithm
- For any instance $I$ of $\textsf{Parallel Sliding Squares}$, we can compute a
feasible, weakly in-place schedule of $O(P_1 + P_2)$ transformations in polynomial time


<div class="grid grid-cols-2 gap-4em">

<div class="darklist">

1) <span v-click="1" v-mark="{at:[1,2], type:'box', iterations:'1', color:'yellow'}"> Compute a Skeleton </span>

2) <span v-click="2" v-mark="{at:[2,4], type:'box', iterations:'1', color:'yellow'}"> Construct a Sweep Line </span>

3) <span v-click="4" v-mark="{at:'4', type:'box', iterations:'1', color:'yellow'}"> Sweep the configuration to be 3-scaled </span>

</div>
<div>

<img v-click=[1,2] src="/ModularRobots/overview-0.svg" style="background:white;width:300px;">

<img v-click=[2,3] src="/ModularRobots/overview-1.svg" style="background:white;width:400px;">

<img v-click=[3,4] src="/ModularRobots/overview-2.svg" style="background:white;width:400px;">

<img v-click=[4,5] src="/ModularRobots/overview-3.svg" style="background:white;width:400px;">

<img v-click=[5,6] src="/ModularRobots/overview-4.svg" style="background:white;width:400px;">

<img v-click=[6,7] src="/ModularRobots/overview-5.svg" style="background:white;width:400px;">

<img v-click="7" src="/ModularRobots/overview-6.svg" style="background:white;width:400px;">

</div>

</div>

<!-- 

clicks: 6


# Our Algorithm

<div class="flex flex-col items-center">

<div v-click.hide=2> Compute a Skeleton </div>
<div v-click=[2,4]> Build a Sweep Line </div>
<div v-click=4> Sweep the line </div>

<img v-click.hide=0 src="/ModularRobots/overview-0.svg" style="background:white;width:400px;">

<img v-click=[1,2] src="/ModularRobots/overview-1.svg" style="background:white;width:400px;">

<img v-click=[2,3] src="/ModularRobots/overview-2.svg" style="background:white;width:400px;">

<img v-click=[3,4] src="/ModularRobots/overview-3.svg" style="background:white;width:400px;">

<img v-click=[4,5] src="/ModularRobots/overview-4.svg" style="background:white;width:400px;">

<img v-click=[5,6] src="/ModularRobots/overview-5.svg" style="background:white;width:400px;">

<img v-click=[6,7] src="/ModularRobots/overview-6.svg" style="background:white;width:400px;">

</div> 
-->

---
layout: iframe-zoom
url: https://modular-robotics-group.github.io/modular-robotics/WebVis/index.html?presenting=true&file=sweepline
cropTop: 0
width: 150
---

# Sweep Line
