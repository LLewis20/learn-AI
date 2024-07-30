
## Plan

![[plan_example.png| 400]]

- Each route with arrows leading to the green area is a plan.
- Our agent would take wherever you start on the blue line and follow that line until it got to the green area and that's exactly that way the agent would go because we are using a deterministic plan.
- With our agent we don't have a plan unless the agent knows all the steps to get to the location they need to get too, with this we will have randomness as our agent goes through the maze. 
- We will use the new [[The Bellman Equation]] that we went over in the notes for [[Markov Decision Process (MDP)]] so that we now have the weights/values (v) for our tiles.

| Bellman Equation                             | Bellman Equation with MDP                                                    |
| :------------------------------------------- | ---------------------------------------------------------------------------- |
| ![[Bellman_Equation_Example.png_2.png\|350]] | ![[mdp_map.png\| 350]]                                                       |
| $$ V(s) = max(R(s,a) + γV(s')) $$            | $$ V(s) = \max_a \left\{ R(s,a) + \gamma \sum_{s'} P(s,a,s')V(s') \right\}$$ |


### Policy

![[plan_after_MDP.png|400]]

- After running the agent through the maze these are the directions the agent would take when running throughout the maze.
- The agent is able to think of ideas that humans could not easy or quickly look at while running through this maze.
- The box the the right of the grey box is deciding to go back into the grey box, this is because it has a 10% chance of going into the red area if it went up, but if it goes towards the grey box it will bounce back to the same area it was in with a 80%.
- The same effect is happening in the bottom right corner, the agent has decided to go down to minimize the possibility of it landing in the red area.

![[plan_after_mdp_2.png| 400]]