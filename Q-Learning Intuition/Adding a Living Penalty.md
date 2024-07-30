
### Reinforcement Learning Basics
- As talked about in [[Reinforcement Learning]] the role of the agent it to perform actions in an environment to change its state. 
- To get our agent to move we would use just a single location that would give our agent a reward.
	- Rewards were only at the ends of the maze
	- +1 for reaching the green area
	- -1 for reaching the red area
- We need to give an reward to our agent when they are find their way through the maze.

---

### Continuous Rewards
- Typically we would give our agent rewards at they journey through whatever the agent is doing, not just at the end.
- Examples
	- AI in a game receives points for actions like killing an enemy
	- Points for overtaking another car in a racing game
- For the maze we have been working on, we will add a small reward that our agent receives
![[maze_of_rewards.png| ]]
- When our agent enters a tile, the agent will be given the reward that is listed on the tile.
- Having a negative reward incentivizes the agent to complete the maze as quickly as it can.

---

### Continuous Rewards with different values

- With a lower reward value, it creates a policy were our agent will try to find a more optimal route as it goes through our maze

![[living_reward_different_values.png]]

- Reward(s) = 0
	- This is how our first iteration of our maze was, our agent chooses to move into walls to avoid taking risk of landing in the red area.
	- This approach prolongs the game since our agent is not being penalized for taking longer.
- Reward(s) = -0.04
	- In this approach our agent no longer decides to move into walls, but the agent still decides to take a long way around the maze so that it avoid the possibility of running into the red area.
- Reward(s) = -0.5
	- Here the longer the path the less attractive that solution would be, now our agent is taking shorter routes, but also taking riskier routers, even if there is a change of hitting the red area.
- Reward(s) = -2.0
	- Since the agent is receiving an extremely high penalty, it incentivizes the agent to end the game as quickly as possible.
	- This leads the agent preferring to jump into the red area because it has a reward value of -1 instead of -2.
- Having a higher living penalty does not mean that the agent will always find the most correct/optimal solution, you have to find a balance between the rewards and the living penalty.


---

