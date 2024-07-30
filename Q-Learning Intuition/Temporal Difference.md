Temporal difference (TD) is a crucial part for understanding Q-learning algorithm.
It is central to how Q-learning combines the various concepts learned in artificial intelligence.

---

### Deterministic vs. Non-Deterministic Search:
- In deterministic environment, an agent's actions lead to predicable outcomes
- In non-deterministic environments, the agent's actions have probabilistic outcomes (e.g., 10% change to go left, 10% to go right, and 80% chance to go straight).

### Challenges in Non-Deterministic Environments:
- V-Values, or state values, are easier to calculate in deterministic environments using the Bellman equation.
- In non-deterministic environments, the agent's movements are probabilistic, making it more complex to calculate V-values.
- The need for recursion and the presence of randomness complicate these value calculations.

---

### Understanding Temporal Difference (TD)


![[td_example1.png| 400]]

- Before moving our value is:$$Q(s,a)$$
- After moving our value is:
	$$R(s,a) + \gamma\ max_{a'}Q(s',a')$$
- Temporal Difference Equation

$$ TD(a,s) = R(s,a) + \gamma\ max_{a'}\ Q(s',a') - Q_{t-1}(s,a)$$
WHERE
$$ Q_{t}(s,a) = Q_{t-1}(s,a) + \alpha TD_{t}(a,s)$$

Expanded
$$Q_{t}(s,a) = Q_{t-1}(s,a) + \alpha(R(s,a) + \gamma max_{a'}Q(s',a') - Q_{t-1}(s,a))$$


- We will use the before moving value at the end of our temporal difference equation, and use the after moving value for our remaining parts of the equation.


### Extra Reading
- [[Learning to Predict by the Methods of Temporal Differences]]

