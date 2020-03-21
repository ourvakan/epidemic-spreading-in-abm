
## Epidemic spreading simulation

We develop a simple epidemic spreading model inspired by Boltzmann kinetic equation. 
The model has two main parameters which determine how the epidemic spreading 
will propagate in a system of N agents. By providing a short analytical description, 
we explain the intrinsic meaning of these parameters
and investigate how they are interconnected with the spreading.

#### Problem formulation

Unlike chaotic molecules, people exploit their ability to cooperate 
for a global of energy minimization. In our daily life, we spend time in groups of people 
in a bus, elevator, at work in the office or in a lecture hall. 
A significant amount of time we spend alone. These groups of people we call clusters. 

We have a system of N agents, which can be in one of the 5 states:
    
    - INFECTED
    - SUSCEPTIBLE
    - RECOVERED
    - DEAD
    - IMMUNE
    
At each step, according to the policy, 
susceptible agents can get infected with a chosen mechanism
if they are in contact with an infected agent. 
An infected agent can either recover after several iteration steps or die.
Immune agents neither can get infected nor propagate the infection.

The simulation starts with one infected agent and ends when there're no infected left.

#### Probability spreading:

= discrete time model

= derive a probability for infection

= find ```beta``` from microscopic parameters

#### Simulation results:

1. Different alpha

2. Different beta
 
     
#### Open questions:

   - Can the micro-parameters be "fitted" to real data (obtained from macro-parameters)?
   
   - What determines when the exponential distribution will break
   
   - What determines the total time of infection.
    