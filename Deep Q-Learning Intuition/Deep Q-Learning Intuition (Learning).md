
## 1. Intro to Deep Q-Learning
- Transition from basic Q-learning to deep Q-learning, adding depth and complexity to enhance learning capabilities.
- Deep Q-learning incorporates neural networks to improve decision making processes in more complex environments.

## 2. Basics of Q-Learning
- Fundamentals
	- An agent interacts with the environment, takes actions based on current states, receives rewards, and transitions into new states.
- Learning Mechanisms:
	- Basic Q-learning utilizes a Q-table (matrix) to store and update state-action values (Q-values).
	- The agent learns to optimize actions by updating Q values through experience, aiming to maximize cumulative rewards.
- Policy in Stochastic Environments:
	- Non-stochastic environments allow for direct action planning, while stochastic environments require policies to handle randomness and uncertainty.

---

## 3. Deep Q-learning Setup
- Enhanced State Representation:
	- Introduce two axes (X1 and X2) to describe states in a more detailed manner.
	- Each state in the environment is represented by a pair of values (X1, X2), creating a more comprehensive state space.
- Neural Network Integration:
	- States are fed into a neural network, which processes this information and outputs Q values for all possible actions.
![[deepqlearning.png]]

---

## 4. Neural Network in Deep Q-learning
- Network Structure:
	- The neural network consists of input layers (state values), hidden layers (complex feature extraction), and output layers (Q values for actions).
- Action Prediction:
	- For each state, the network predicts Q values for all possible actions (e.g., up, right, left, down).
- Learning from Experience:
	- Instead of "before" and "after" states, the network uses previously stored Q values to predict current Q values, continually refining its predictions. Cross propagation.

---

## 5. Why use deep learning:
- Limitations of basic q-learning:
	- Basic q-learning is effective in simple environments but failed to scale in complexity.
- Power of deep learning:
	- Deep learning provides the computational power and flexibility needed for complex task such as self-driving cars, advanced gaming, and robotic movements.
- Neural Networks strengths:
	- Neural networks learn by adjusting weights through backpropagation, making them adept at approximating functions, including q values in varied states.

--- 

## 6. Temporal Difference Learning:
- Core Concept:
	- Temporal difference (TD) learning updates Q values based on the difference between expected rewards and actual outcomes.
- Q value adjustment:
	- The agent compares predicted q values with actual rewards plus the discounted values of the next state's q values, iteratively improving its policy.

---

## 7. Adapting Temporal Difference to neural Networks
- State input and q value output:
	- States are input into the neural network, which outputs predicted q values for possible actions.
- Target Q values:
	- Target Q values are derived from previous experiences, providing a benchmark for the network's predictions.
- Loss Calculation:
	- Loss is calculated as the squared difference between predicted Q values and target Q values, providing a measure of prediction accuracy.

---

## 8. Loss Calculation and Backpropagation:
- Minimizing Loss:
	- The networks aims to minimize loss through backpropagation and stochastic gradient descent, adjusting weight to reduce prediction errors.
- Iterative Improvement:
	- The network iteratively updates its weights, continually refining its Q values predictions to better approximate true values.
- Backpropagation process:
	- Loss is propagated backward through the network, updating weights to align predictions with actual rewards, enhancing the agent's learning over time.
![[backpropagation.png| ]]

---

## 9. Learning through trail and error:
- Empirical learning:
	- The agent learns the environment by performing actions, observing rewards, and updating the neural network based on these experiences.
- Continuous Refinement:
	- over time, the neural network becomes more accurate in predicting Q values, enabling the agent to make more informed and effective divisions.
- Policy Optimization:
	- As the network's predictions improve, the agent's policy becomes more optimal, allowing it to navigate and interact with the environment more efficiently.