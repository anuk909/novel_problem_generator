# Task ID: hard/10

## Prompt

```python
def mythic_search(office_map):
    """
    Implement a reinforcement learning agent that navigates through a mythical office, represented as a 2D grid. The grid contains various cells: accessible cells ('O'), treasures ('T'), mythical beasts ('B'), and walls ('W'). The goal is to start from the top-left corner of the grid and find a path to collect all treasures while avoiding beasts. The agent can move up, down, left, or right but cannot move through walls or beasts.

    The office_map is a list of strings where each string represents a row of the grid. The agent must be implemented using reinforcement learning techniques to determine the optimal path to collect all treasures and then exit the maze.

    For example:
    ['OOOO',
     'OWOO',
     'OBOO',
     'OTOO']
    should return a path [(0,0), (1,0), (2,0), (2,1), (3,1), (3,2)] which collects the treasure and exits safely.

    - The agent always starts from (0,0).
    - There are no treasures in cells with beasts or walls.
    - You need to implement the training of the agent within this function.
    """

```

## Canonical Solution

```python
   
    # The canonical solution should include a detailed reinforcement learning approach, which was omitted due to its complexity but primarily involves the following steps:
    # 1. Define the environment and states.
    # 2. Set up the reward system, penalizing the agent for moving onto a beast and rewarding for collecting treasures.
    # 3. Implement an RL algorithm like Q-learning to train the agent to maximize rewards.
    # 4. Track the optimal path found after training to collect all treasures and exit.
    # Implementations would involve libraries like OpenAI Gym for simulating the environment and agents.
```

## Test Cases

```python
def check(candidate):
    assert candidate(['OOOO', 'OWOO', 'OBOO', 'OTOO']) == [(0,0), (1,0), (2,0), (2,1), (3,1), (3,2)]
    assert candidate(['OTO', 'OOO', 'OOB']) == [(0,0), (0,1), (0,2)]
    assert candidate(['OOO', 'OBO', 'OTO']) == [(0,0), (1,0), (2,0), (2,1), (2,2)]
    assert candidate(['OOOO', 'WOBO', 'OOOO', 'TTOT']) in [[(0,0), (0,1), (0,2), (0,3), (1,3), (2,3), (3,3), (3,2), (3,1)]]
    assert candidate(['OOW', 'BOW', 'TOO']) == [(0,0), (0,1), (1,1), (2,1), (2,2)]
```

## Entry Point

`mythic_search`

## Extra Info

## Field

Reinforcement Learning

## Cover Story

['office', 'mythical beast']

## Cleaned Prompt

```python
Define a reinforcement learning function to navigate a grid, avoiding beasts and collecting treasures.

Example:
['OOOO', 'OWOO', 'OBOO', 'OTOO'] -> [(0,0), (1,0), (2,0), (2,1), (3,1), (3,2)]
Explanation: This path collects the treasure and avoids the beast, demonstrating an optimal solution learned by the RL agent.
```

## Warnings

- Solution failed correctness check. reason: failed: 
- 5, Unrealistic Implementation Expectation: The prompt demands implementing a full reinforcement learning agent within a single function, which is highly complex and atypical for such environments. Real-world RL setups involve extensive configuration, external libraries, and training environments that are unreasonable to encapsulate fully in one function.
- 4, Unclear Exit Condition: The problem description does not specify how or where the agent should exit the grid after collecting all treasures. The example implies exiting is part of the task but no explicit exit point or condition is given in the description, leading to potential confusion about the task's end goal.
- 4, Ambiguous Test Outputs: The expected paths in the tests assume a very specific sequence of movements, which may not be the only optimal path, especially given the nondeterministic nature of training in reinforcement learning. This could lead to correct solutions being incorrectly marked as failed due to differing valid paths.

