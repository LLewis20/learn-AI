*Paper can be found here: [The Theory of Dynamic Programming](https://www.ams.org/journals/bull/1954-60-06/S0002-9904-1954-09848-8/S0002-9904-1954-09848-8.pdf)*


## Summary
### 1. Introduction
- Focus:
	- Dynamic programming addresses problems where decisions need to be made sequentially over multiple stages.
	- Each decision influences the system's state and impacts subsequent decisions.
	- The objective is to find a strategy that maximizes a function of the final state parameters.
- Context:
	- This theory is applicable to a wide range of fields requiring optimization over time.

---
### 2. Applications
- Fields:
	- Industrial Production Planning: Optimizing production schedules, resource allocation, and workflow to enhance productivity and minimize costs.
	- Medical Scheduling: Efficiently scheduling patient appointments, surgeries, and treatments to maximize resource utilization and patient care.
	- Investment Program: Developing strategies for financial investments to maximize returns while managing risks.
	- Machinery Replacement Policies: Determining the optimal time to replace machinery to balance costs with operational efficiency and reliability.
	- Optimal Purchasing and Inventory Strategies: Managing inventory levels and purchasing decisions to minimize costs while ensuring availability.

---
### 3. Concepts and Terminology
- Policy:
	- A sequence of decisions made at different stages of the process.
- Optimal Policy:
	- The policy that results in the highest return according to a predefined criterion.
- Classical Approach:
	- Involves evaluating all feasible policies to identify the one that maximizes returns.
	- Often impractical due to the "curse of dimensionality" where the number of potential policies grows exponentially with the number of stages.

---
### 4. Principle of Optimality
- Definition:
	- A principle stating the an optimal policy has the property that, regardless of the initial state and decisions, the remaining decisions must constitute an optimal policy concerning the state resulting from the first decision.
- Foundation:
	- This principle forms the basis for formulating functional equations in dynamic programming.
	- It simplifies the problem by breaking it down into subproblems, each of which can be solved independently.

---

### 5. Mathematical Formulation
- Deterministic Processes:
	- Described by state vectors and transformations.
	- Each decision deterministically affects that state.
	- The goal is to find a sequence of decisions that maximize a scalar function of the final state.
- Stochastic Processes:
	- Decisions lead to a distribution of outcome states rather than a single deterministic outcome.
	- Policies are evaluated based on expected returns, considering the probabilities of different outcomes.
- Infinite Processes:
	- Useful for theoretical purposes, involving an unbounded number of stages.
	- These processes often lead to the formulation of partial differential equations in continuous systems.

---

### 6. Examples
- Allocation Problem:
	- Scenario: Distributing resources across different stages to maximize total return.
	- Approach: Using dynamic programming to determine the optimal allocation strategy.
	- Impact: Ensures efficient use of resources over time.
- Stochastic Gold Mining:
	- Scenario: Deciding how to use a mining machine between two mines with different probabilities of yielding gold.
	- Approach: Developing a policy that maximizes the expected return from mining activities.
	- Impact: Balances the risk and potential reward in resource extraction.
- Calculus of Variations:
	- Scenario: A continuous decision where the goal is to maximize a function over time.
	- Approach: Using dynamic programming principles to derive the Euler equation, which provides the conditions for an optimal solution.
	- Impact: Applies to various field, including physics, economics, and engineering, where optimal continuous paths need to be determined.