
## Learning and Acting in Reinforcement Learning:
- Learning:
	- This involves the agent interacting with the environment and collecting data about the consequences of its actions.
	- The neural network predict Q-values for each possible action in a given state.
	- The agent receives feedback from the environment, which is used to calculate the loss.
	- Backpropagation is used to update the network weights, minimizing the prediction error over time.
- Acting:
	- Once the Q-values are obtained, they are used to select actions.
	- The agent decides which action to take based on the Q-values, with the goal of maximizing future rewards.
![[learningvacting.png]]

---

## Action Selection:
- The agent uses the Q-values, passing them through a Soft Max Function to select an action.
	- Soft Max Function:
		- This function converts raw Q-values into probabilities.
		- It allows for exploration by giving a non-zero probability to all actions, not just the highest Q-value action.
		- This helps balance exploration (trying new actions) and exploitation (using known rewarding actions).
		- ![[softmax.png]]

	- Exploration vs. Exploitation:
		- An important concept in reinforcement learning.
		- Initially, more exploration is encouraged to learn about the environment.
		- Over time, the agent exploits known good actions to maximize rewards.

---

## Process Repetition:
- The described process of learning and acting repeats for every state that agent encounters.
- Each completion of the game or reaching a terminal state marks the end of an epoch, after which the process restarts.
- Epoch:
	- In machine learning, an epoch is one complete pass through the entire training dataset
	- Here, it refers to the agent completing a full game or task cycle.
- Continuous Improvement:
	- The agent continuously learns from each epoch, improving its policy and performance over time.
	- Each new state and action taken provides more data to refine the neural network.

---

## Encoding the Environment
- The state of the environment is encoded as a vector, simplifying the problem initially.
- Vector Encoding:
	- The state is represented as a vector of features.
	- This could be a simple list of numerical values indicating different aspects of the state.
- One-Hot Encoding:
	- Another method to encode the state, particularly useful in grid-like environments.
	- Each state is represented by a vector with one element set to 1 (indicating the agent's position) and all other set to 0.
- Gradual Complexity:
	- the course starts with simple encoding methods.
	- More complex methods like convolutional neural networks (CNNs) will be introduced later, which are better suited for processing images.

---

## Extra Reading
- [Simple Reinforcement Learning with Tensorflow](https://awjuliani.medium.com/simple-reinforcement-learning-with-tensorflow-part-4-deep-q-networks-and-beyond-8438a3e2b8df)
