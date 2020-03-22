
## Epidemic spreading simulation

We develop a simple epidemic spreading model inspired by Boltzmann kinetic equation. 
The model has two main parameters which determine how the epidemic spreading 
will propagate in a system of N agents. By providing a short analytical description, 
we attempt to explain the intrinsic meaning of these parameters
and investigate their connection with the spreading evolution.

#### Problem formulation

Unlike chaotic molecules, people exploit their ability to cooperate 
for global energy minimization. In our daily life, we spend time in groups of people 
in a bus, elevator, at work in the office or in a lecture hall. 
A significant amount of time we spend alone. These groups of people we call clusters. 

We have a system of N agents, which can be in one of the 5 states:
    
    - INFECTED
    - SUSCEPTIBLE
    - RECOVERED
    - DEAD
    - IMMUNE
    
Let the probability that an agent gets infected at the i-th step 
of evolution be denoted as 
<a href="https://www.codecogs.com/eqnedit.php?latex=p_i(c,&space;cl,&space;inf)" target="_blank"><img src="https://latex.codecogs.com/png.latex?p_i(c,&space;cl,&space;inf)" title="p_i(c, cl, inf)" /></a>
. It depends on the probabilities of 
```c``` - the collision event,
```inf``` - infected agents in a cluster,
```cl``` - a cluster in which. 
Assuming the infection spreads when infected agent is in contact with a susceptible one:

<a href="https://www.codecogs.com/eqnedit.php?latex=p_i(c,&space;cl,&space;inf)&space;=&space;p(c&space;|&space;cl,&space;inf)&space;*&space;p(inf|cl)&space;*&space;p(cl)" target="_blank"><img src="https://latex.codecogs.com/png.latex?p_i(c,&space;cl,&space;inf)&space;=&space;p(c&space;|&space;cl,&space;inf)&space;*&space;p(inf|cl)&space;*&space;p(cl)" title="p_i(c, cl, inf) = p(c | cl, inf) * p(inf|cl) * p(cl)" /></a>

We consider the first term a constant, the second term uniquely distributed,
the last term, exponentially distributed. 

At each step, according to the policy, 
susceptible agents can get infected according to the provided mechanism.
An infected agent can either recover after several iteration steps or die.
Immune agents neither can get infected nor propagate the infection.
Simulation starts with one infected agent and ends when there're no infected left.


#### Simulation results:

![Smoothed simulation run](data/area_plot/area_stack_mean_100_03-22-2020__23-20-47.png?raw=true) 
     
#### Possible research vectors:

   - Can the micro-parameters be "fitted" to real data (obtained from macro-parameters)?
   
   - What determines when the exponential distribution will stop?
   
   - What determines the total lifespan of infection.
    
   - How the maximum number of infected depends on the parameters alpha and beta
   
   - Is there a relation between the number of infected and the number of recovered