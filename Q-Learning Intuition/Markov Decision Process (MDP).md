
## Deterministic Search

![[Deterministic_Search_example.png.png| 200]]

- Deterministic search means that if our agent decides to take any action then what will happen is with 100% probability, it will take that action and change its state.

## Non-Deterministic Search

![[Non_Deterministic_search.png.png| 450]]

- Non-deterministic search is when our agent says it wants to take an action but there is a certain probability that our agent will take a different action. In the example above There are 3 options our agent can take. With an 80% change he goes up. But then with a 10% chance when he wants to go up, he will actually go to the left or right.
- We are modeling that there is something that is out of the control of the agent, something that it cannot predict to cause randomness.

---

### Markov Process
- A stochastic process has the Markov property if the conditional probability distribution of future states of the process (conditional on both past and present states) depends only upon the present state, not on the sequence of events that preceded it. A process with this property is called a Markov process.
- In simple terms the Markov property describes a process where future states depend only on the current state, not on the sequence of events that preceded it. The results of any action taken in the current environment are influenced solely by the present state and not by how the system arrived at this state.
### Markov Decision Processes (MDPs)
- Provides a mathematical framework for modeling decision making in situations where outcomes are partly random and partly under the control of a decision maker.


### Adding MDP to Bellman's Equation
The Markov decision process is just an add-on to the [[The Bellman Equation]] but just a bit more sophisticated by adding randomness to our discount factor (γ).

Current Equation (Deterministic): $$ V(s) = max(R(s,a) + γV(s')) $$

Updated Equation after MDP (Non-Deterministic): $$ V(s) = \max_a \left\{ R(s,a) + \gamma \sum_{s'} P(s,a,s')V(s') \right\}$$

For our discount factor now all we are doing is looking at each action that we could take then multiplying it by out probability of actually getting to that state.

Using our Non-Deterministic search example from above here is how the equation would look: $$V(s) = \max_a \left( R(s, a) + \gamma \left[ 0.8 \cdot V(s_1) + 0.1 \cdot V(s_2) + 0.1 \cdot V(s_3) \right] \right)$$


## Extra Reading 

- [[A Survey of Applications of Markov Decision Processes]]
