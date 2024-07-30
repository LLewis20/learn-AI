## Action Selection Policies
- Importance of selecting actions based on Q values.
- Basic strategy: choose the action with the highest Q value.

## Exploration vs. Exploitation
- Key challenge in reinforcement learning.
- Need to balance taking known good actions (exploitation) and trying new actions (exploration).

## Common Action Selection Policies
- Epsilon Greedy:
	- Select the action with the highest Q value most of the time.
	- With probability epsilon, select a random action.
- Epsilon Soft:
	- Select a random action most of the time, with probability epsilon, select the action with the highest Q value.
- Softmax:
	- Convert Q values to probabilities using the softmax function.
	- Select actions based on these probabilities, promoting both exploration and exploitation.

## SoftMax in Detail
- Explanation of the SoftMax function and its benefits.
- Converts Q values to a probability distribution.
- Ensures exploration by probabilistically selecting actions.

## Practical Application
- Course will use the SoftMax action selection policy.
- SoftMax combines logic with randomness, providing a ore structured exploration approach.

## Additional Resources
- Reference to an article on adaptive epsilon greedy exploration.
- Encouragement to explore further reading to understand the evolution and comparison of action selection policies.

