import numpy as np


# Setting up states, actions, and rewards

gamma = 0.75
alpha = 0.9

states = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11
}

actions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

rewards = np.array([
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0 ,0, 0 ,0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1000, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
])


# ---------------------------------- BUILDING MODEL WITH Q-LEARN -----------------------------------------------
q_values = np.array(np.zeros([12, 12]))


for i in range(2000):
    current_state = np.random.randint(0, 12)
    playable_actions = []
    for j in range(12):
        if rewards[current_state, j] > 0:
            playable_actions.append(j)
    next_state = np.random.choice(playable_actions)
    temp_diff = rewards[current_state, next_state] + gamma*q_values[next_state, np.argmax(q_values[next_state,])] - q_values[current_state, next_state]
    q_values[current_state, next_state] = q_values[current_state, next_state] + alpha*temp_diff

# Q values
print("Q-values:")
print(q_values.astype(int))


state_to_location = {state: location for location, state in states.items()}

def route(starting_location, ending_location):
    route = [starting_location]
    next_location = starting_location
    
    while next_location != ending_location:
        starting_state = states[starting_location]
        next_state = np.argmax(q_values[starting_state])
        next_location = state_to_location[next_state]
        route.append(next_location)
        starting_location = next_location 
    return route

print('Routes:\n', route('E','G'))
