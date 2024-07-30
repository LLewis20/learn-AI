# Reinforcement Learning with Deep Q-Learning: LunarLandar-v2

- This repository contains an implementation of Deep Q-Learning (DQN) for solving the LunarLander-v2 environment from OpenAI Gym. This project demonstrates the application of deep reinforcement learning to a classic control problem, where an agent must learn to land a lunar lander safely on a designated landing pad. The implementation includes detailed explanations of how the model works and its connection to fundamental concepts in reinforcement learning such as Bellman’s Equation and Markov Decision Processes (MDPs).


## Integration with MDPs and Bellman's Equation
Using MDPs and Bellman's equation we are able to write an algorithm for our Neural Network to train on. with both ideas we are able to create the mathmatical equation of:

$$ Q_{t}(s,a) = Q_{t-1}(s,a) + \alpha(R(s,a) + \gamma max_{a'}Q(s',a') - Q_{t-1}(s,a))$$

### Where:

- $Q_{t}(s,a)$ is the Q-value for state $s$ and action $a$ at time $t$.
- $Q_{t-1}(s,a)$ is the Q-value for state $s$ and action $a$ at the previous time step $t-1$.
- $\alpha$ is the learning rate, which controls how much new information overrides the old information.
- $R(s,a)$ is the reward received for taking action $a$ in state $s$.
- $\gamma$ is the discount factor, which models the importance of future rewards compared to immediate rewards.
- $\max_{a'} Q(s',a')$ represents the maximum Q-value for the next state $s'$ over all possible actions $a'$.



## Training Progress Videos

| Epochs         | Description                                                                 | Visualize                                                                                  |
|----------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| **Epochs 1-50**   | During these initial epochs, the model is primarily exploring and learning how to navigate the environment. It is still in the early stages of training and not yet optimized. | [![YouTube](http://i.ytimg.com/vi/rEgXE_1e6D4/hqdefault.jpg)](https://www.youtube.com/watch?v=rEgXE_1e6D4) |
| **Epochs 300-350** | At this stage, the model has successfully learned to land without crashing. This period marks its first instances of achieving positive reward scores, indicating significant progress. | [![YouTube](http://i.ytimg.com/vi/r_lz09KOVF0/hqdefault.jpg)](https://www.youtube.com/watch?v=r_lz09KOVF0) |
| **Epochs 451-500** | The model has mastered landing the spacecraft but takes a considerable amount of time to complete the landing. This shows that while the core functionality is in place, there is room for further optimization. | [![YouTube](http://i.ytimg.com/vi/5RrroqLHvkQ/hqdefault.jpg)](https://www.youtube.com/watch?v=5RrroqLHvkQ) |
| **Epochs 751-800** | **COMING SOON**: Details and video for this epoch range will be available shortly.  | **COMING SOON**: Video link to be added.                                                   |

To see all epoch video here is a link to the playlist: [Q-Learn LunarLandar](https://www.youtube.com/playlist?list=PLNMwBbQZg4Ytbwrr4OtA_wC9v2ryv6b_4)



# Project Structure

### `main.py`

The `main.py` script is the central component of this project and handles the following tasks:

1. **Hyperparameter Initialization:**
   - Sets up various hyperparameters used during the training of the agent. This includes:
     - Number of episodes for training.
     - Maximum number of timesteps per episode.
     - Exploration parameters such as epsilon for the epsilon-greedy policy.

2. **Agent and Environment Setup:**
   - Initializes the LunarLander-v2 environment from OpenAI Gym.
   - Creates an instance of the `Agent` class with the appropriate state and action dimensions.

3. **Training Loop:**
   - Executes the training process for the specified number of episodes.
   - For each episode, the agent interacts with the environment, taking actions based on its policy and learning from the rewards received.
   - Updates the agent’s policy using experience replay and target network updates.

4. **Video Recording:**
   - Records and saves videos of the agent’s performance every 50 episodes. This is useful for visualizing and analyzing the agent's learning progress.
   - Uses the `imageio` library to save these videos, which are named according to the episode number.

5. **Video Display:**
   - Includes functionality to display saved videos in a Jupyter notebook or IPython environment for easy viewing.

This structure ensures that the training process is well-organized and that the agent’s learning progress can be monitored through periodic video recordings.

## `nnetwork.py`

This module defines the neural network architecture used in the DQN algorithm.

### `Network`

The `Network` class implements a feedforward neural network with three fully connected layers. It is used to approximate the Q-value function in the DQN algorithm.

- **Constructor (`__init__`):**
  - Initializes the network with three linear layers.
  - The first two layers have 64 units each and use ReLU activation.
  - The final layer outputs Q-values for each action.

- **Method:**
  - **`forward(state)`**: Defines the forward pass through the network, producing Q-values for the given state.

This network is responsible for estimating the Q-values, which guide the agent’s decision-making process.



## `agent.py`

This module defines the core components of the Deep Q-Learning (DQN) algorithm used in the project, including the replay memory and the agent. It consists of the following main classes:

### `ReplayMemory`

`ReplayMemory` is a class responsible for storing and managing the agent's experiences during training. It supports experience replay, which helps to break the temporal correlation between consecutive experiences and improves training stability.

- **Constructor (`__init__`):**
  - Initializes the memory with a specified capacity and selects the appropriate device (CPU or GPU).
  
- **Methods:**
  - `push(event)`: Adds a new experience to the memory. If the memory exceeds its capacity, the oldest experiences are removed.
  - `sample(batch_size)`: Randomly samples a batch of experiences from the memory. The experiences are converted to PyTorch tensors and moved to the appropriate device.

### `Agent`

The `Agent` class encapsulates the behavior of the DQN agent, including interaction with the environment, action selection, and learning from experiences.

- **Constructor (`__init__`):**
  - Initializes the agent with the state size, action size, and other parameters.
  - Creates two Q-networks: `local_qnetwork` and `target_qnetwork`. The local Q-network is used for selecting actions and learning, while the target Q-network is used to compute target Q-values.
  - Sets up an optimizer (`Adam`) and an instance of `ReplayMemory`.

- **Methods:**
  - `step(state, action, reward, next_state, done)`: Processes a single experience by storing it in memory and performing a learning step every 4 actions if the memory is sufficiently large.
  - `act(state, epsilon=0.)`: Chooses an action based on the current policy. It uses an epsilon-greedy strategy where the agent either selects the action with the highest Q-value or a random action with probability epsilon.
  - `learn(experiences, discount_factor)`: Updates the Q-network weights by minimizing the mean squared error between the expected Q-values and the target Q-values. This method also performs a soft update of the target network.
  - `soft_update(local_model, target_model, interpolation_parameter)`: Performs a soft update of the target network’s weights by blending them with the weights of the local network.


  