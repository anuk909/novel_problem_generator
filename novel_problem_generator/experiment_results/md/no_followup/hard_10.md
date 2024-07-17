# Task ID: hard/10

## Prompt

```python
def treasure_combinations(capacity, items):
    """
    During an archaeological dig, a team of robots has discovered several ancient artifacts, each with a certain historical significance score, and each occupies a certain space. The team has a storage container with a limited capacity. Your goal is to determine which combination of artifacts the robots should select to maximize the total historical significance score without exceeding the capacity of the storage container.

    Write a function that takes an integer representing the maximum space (capacity) the container can hold and a list of tuples, where each tuple contains two integers representing the historical significance score and the space occupied by an artifact, respectively. The function should return the maximum total historical significance score that can be achieved without exceeding the capacity.

    This is a variant of the 'Knapsack problem' and is often solved using dynamic programming.

    For example:
    - If capacity = 10 and items = [(5, 3), (4, 2), (7, 4), (8, 5)], the output should be 12, because the best combination is the items with scores 5 and 7 which occupy spaces 3 and 4 respectively (total space 7), maximizing the score without exceeding the capacity.

    - If capacity = 5 and items = [(3, 4), (2, 3)], the output should be 0, since no single artifact or combination of artifacts fits without exceeding the capacity.
    """

```

## Canonical Solution

```python
    def knapsack(dp, items, i, capacity):
        if i >= len(items):
            return 0
        if dp[i][capacity] != -1:
            return dp[i][capacity]
        not_taken = knapsack(dp, items, i + 1, capacity)
        taken = 0
        if items[i][1] <= capacity:
            taken = items[i][0] + knapsack(dp, items, i + 1, capacity - items[i][1])
        dp[i][capacity] = max(not_taken, taken)
        return dp[i][capacity]
    
    dp = [[-1 for _ in range(capacity + 1)] for _ in range(len(items))]
    return knapsack(dp, items, 0, capacity)
```

## Test Cases

```python
def check(candidate):
    assert candidate(10, [(5, 3), (4, 2), (7, 4), (8, 5)]) == 12
    assert candidate(5, [(3, 4), (2, 3)]) == 0
    assert candidate(20, [(3, 4), (5, 6), (10, 7), (8, 9)]) == 18
    assert candidate(7, [(2, 3), (4, 2), (5, 4)]) == 6
    assert candidate(50, [(4, 5), (5, 10), (10, 13), (15, 20), (20, 25)]) == 35
```

## Entry Point

`treasure_combinations`

## Extra Info

## Topics

['House Robber', 'Combination Sum']

## Field

['Internet of Things (IoT)']

## Cover Story

['archaeological dig', 'robots']

## Cleaned Prompt

```python
Write a function to determine the maximum historical significance score a robot team can achieve by selecting artifacts given storage capacity constraints. The function 'treasure_combinations(capacity, items)' receives an integer 'capacity' which is the maximum space the storage can hold and a list 'items' where each item is a tuple (historical significance score, space occupied). Return the maximum score obtainable without exceeding the capacity using dynamic programming.
```

## Warnings

- Solution failed correctness check. reason: failed: 
- 4, Misleading Problem Tags: The tags "House Robber" and "Combination Sum" do not directly relate to the actual problem, which essentially is a "Knapsack problem". This might mislead participants regarding the expected problem-solving approach, causing confusion and potentially leading them to incorrect solutions.

