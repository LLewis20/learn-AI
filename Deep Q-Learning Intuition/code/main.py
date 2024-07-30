from agent import Agent, ReplayMemory
import gymnasium as gym
import glob
import io
import base64
import imageio
from IPython.display import HTML, display
#from gym.wrappers.monitoring.video_recorder import VideoRecorder
from collections import deque, namedtuple
import numpy as np
import torch
import os

print(torch.cuda.is_available())
env = gym.make('LunarLander-v2')
state_shape = env.observation_space.shape
state_size = env.observation_space.shape[0]
number_actions = env.action_space.n
agent = Agent(state_size, number_actions)

# Training parameters
number_episodes = 2000
maximum_number_timesteps_per_episode = 1000
epsilon_starting_value = 1.2
epsilon_ending_value = 0.01
epsilon_decay_value = 0.995
epsilon = epsilon_starting_value
scores_on_100_episodes = deque(maxlen=100)

# Function to save a video of the agent
def save_video(agent, env_name, episode_number):
    env = gym.make(env_name, render_mode='rgb_array')
    state, _ = env.reset()
    done = False
    frames = []

    while not done:
        frame = env.render()
        # Preprocess frame to ensure dimensions are divisible by 16
        frame = frame[:frame.shape[0] // 16 * 16, :frame.shape[1] // 16 * 16, :]
        frames.append(frame)
        action = agent.act(state)
        state, reward, done, _, _ = env.step(action)

    env.close()

    filename = f'video_{episode_number}.mp4'
    imageio.mimsave(filename, frames, fps=30)

# Training loop
for episode in range(1, number_episodes + 1):
    state, _ = env.reset()
    score = 0
    for t in range(maximum_number_timesteps_per_episode):
        action = agent.act(state, epsilon)
        next_state, reward, done, _, _ = env.step(action)
        agent.step(state, action, reward, next_state, done)
        state = next_state
        score += reward
        if done:
            break
    scores_on_100_episodes.append(score)
    epsilon = max(epsilon_ending_value, epsilon_decay_value * epsilon)
    print('\rEpisode {}\tAverage Score: {:.2f}'.format(episode, np.mean(scores_on_100_episodes)), end="")
    
    if episode % 50 == 0:
        print('\rEpisode {}\tAverage Score: {:.2f}'.format(episode, np.mean(scores_on_100_episodes)))
        save_video(agent, 'LunarLander-v2', episode)
    
    if np.mean(scores_on_100_episodes) >= 200.0:
        print('\nEnvironment solved in {:d} episodes!\tAverage Score: {:.2f}'.format(episode - 100, np.mean(scores_on_100_episodes)))
        torch.save(agent.local_qnetwork.state_dict(), 'checkpoint.pth')
        break

# Function to display videos in the notebook
def show_video(episode_number):
    filename = f'video_{episode_number}.mp4'
    if os.path.exists(filename):
        video = io.open(filename, 'r+b').read()
        encoded = base64.b64encode(video)
        display(HTML(data='''<video alt="test" autoplay
                loop controls style="height: 400px;">
                <source src="data:video/mp4;base64,{0}" type="video/mp4" />
             </video>'''.format(encoded.decode('ascii'))))
    else:
        print(f"Could not find video {filename}")

# Show a specific episode video
show_video(100)  # Change the episode number to view different videos