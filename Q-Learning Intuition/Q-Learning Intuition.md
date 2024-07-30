
### State Values (Previous Approach)
- Agent evaluates options of next action based on current state without considering the steps taken to get there.
- Uses [[The Bellman Equation]] to decide the best action based on future states
- Considers the stochastic nature of the process (multiple possible outcomes for each action)

### Action Values (Q-learning Approach)
- Difference:
	- Shift from evaluating state values (V) to action values (Q)
	- Q represents the quality or value of an action taken in a given state.

---

### Formulas

- State Values Approach
$$ V(s) = \max_a \left\{ R(s,a) + \gamma \sum_{s'} P(s,a,s')V(s') \right\}$$
- Action Values (Q-learning) Approach
$$ Q(s,a) = R(s,a) + \gamma \sum_{s'} (P(s,a,s') max_{a'}\ Q(s', a')) $$
*Q(s, a) = Reward + Discount Factor \* Expected value of future Q-values*
*Recursive calculation, reflecting the stochastic nature of the environment*

---

### Mechanics of Q-values
- Action and States:
	- Agent considers the value of each possible action (up, right, left, down) in a given state
	- Q-values quantify the potential reward of these actions.

---

### Derivation of Q-values
1. Immediate Reward:
	- Performing an action yields an immediate reward
2. Future States:
	- Agent transitions to a new state with certain probabilities
	- Expected values of the next state's value is considered
3. Discount Factor:
	- Future reward are discounted to reflect their present value
4. Expected Value Calculation:
	- Sum of discounted expected values across all possible future states, weighted by their probabilities

---

### Linking Q-values to State Values
- Relationship:
	- Value of a state (V) is the maximum of the Q-values of all possible actions in that state
	- Reinforces that the state value depends on the best possible action available

---

### Implications of Q-learning
- Decision-Making:
	- Agents compare Q-values of possible actions to choose the optimal one.
	- Focus on immediate action quality rather than long-term state values
- Environment Consistency:
	- Environment remains the same regardless of the approach (state value or action value)
	- Both approaches should yield the same overall result

---

### Extra Reading
[Markov Decision Processes: Concepts and Algorithms](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=968bab782e52faf0f7957ca0f38b9e9078454afe)