### $$ V(s) = max(R(s,a) + γV(s')) $$
<u>Richard Ernest Bellman</u>: an applied mathematician, and came up with he concept of dynamic programming, which we now call reinforcement learning in 1953, which was when Bellman equation came to be.

---
### Concepts:
- s - State
	- the state in which our agent is in or any other possible state in which it can be.
- a - Action
	- represents an action that an agent can take
	- an agent can have access to a certain list of actions
- R - Reward
	- the reward the agent gets for entering into a certain state
- γ (Gamma) - Discount
	- the discount factor
- V - value
	- value of being in a certain state
- s' - state prime
	- the state the agent will end up in after taking a certain action

---
### How the Bellman Equation works

![[Bellman_Equation_Example.png.png| 400]]

- White Block: Areas where our agent can go
- Grey Block: Walled off area
- Green Block: Area where we want our agent to finish at
	- r = +1
- Red Block: Area where our agent will lose if stepped into
	- r = -1
- actions
	1. up
	2. right
	3. down
	4. left
- rewards
	1. Green Block = +1
	2. Red Block = -1

Our starting value of 'v' will be (v=0). As our agent goes through the maze our value for 'v' will change. Our agent will be programmed to pick the highest value that 'v' will equal if our agent takes a certain action. If our agent goes into a green block 'v' will increase (v+1), if our agent goes into the red block 'v' will decrease (v-1).

![[Bellman_Equation_Example.png_2.png| 450]]
$$ V(s) = max(R(s,a) + γV(s')) $$

---

### Extra Reading
- [[The Theory of Dynamic Programming]]

