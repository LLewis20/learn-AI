
## Overview
- We are transitioning from theoretical intuition to practical implementation
- The focus of the current session is on integrating an important feature in deep Q-learning called Experience Replay.
- Experience Replay will be coded in the practical segment, but it's crucial to understand its theory first.

---

## Learning and Acting in Deep Q-Learning
- Reinforcement learning consists of two main activities: learning and acting.
- Learning:
	- The neural network updates its weights with each new state to improve its performance in the environment.
	- Loss is calculated and backpropagated through the network to adjust the weights.
- Acting
	- After calculating Q-Values for each state, the network selected the action with the highest Q-Value to perform.

---

## Experience Replay:
- This feature is crucial for addressing the problem of biased learning from sequential states.
- Sequential State Problem:
	- In sequential environments, consecutive state are often similar, leading the network to learn patterns that may not generalize well.
	- For example, a self-driving car navigating a monotonous path learns to drive along walls but fails at corners due to lack of diverse experiences.
- Experience Replay Solution:
	- Instead of updating the network immediately with every state, experiences are saved into memory.
	- A batch of these experiences is used for learning, breaking the sequential bias and providing a more varied dataset.
	- The network learns from a uniformly distributed sample of these experiences, improving generalization and robustness.

---

## Implementation Example
- The self-driving car example illustrates how Experience Replay can prevent overfitting to specifics paths or states.
- Monotonous Path Issue:
	- When the car drives along a wall, the inputs to the neural network remain largely unchanged, leading to biased learning.
	- Experience Replay ensures the network learns from a broader range of states, not just the monotonous ones.

## Advantages of Experience Replay
- Breaks Sequential Bias:
	- Prevents the network from learning biased patterns due to the sequential nature of experiences.
- Utilizes Rare Experiences:
	- Ensures that rare but valuable experiences, like navigating sharp corners, are learned and reinforced.
- Efficient Learning:
	- Allows the network to learn from a batch of experiences multiple times, improving learning efficiency without needing constant new data.

---

## Technical Details:
- Batch Learning:
	- Experiences are stored in batches, which are periodically sampled for training the network.
	- The batch size and sampling frequency can be adjusted based on the environment and task.
- Rolling Window:
	- A rolling window mechanism ensures old experiences are gradually replaced with new ones, maintaining a diverse dataset.
- Uniform Distribution:
	- Experiences are sampled uniformly from the batch to avoid introducing new biases.
	- Prioritized Experience Replay, an advanced technique, can be explored to improve upon uniform sampling.

---

## Extra Reading
[Prioritized Experience Replay](https://arxiv.org/pdf/1511.05952)
