# Task ID: hard/10

## Prompt

```python
def pirate_treasure(combination_weights, capacity):
    """
    A pirate discovers a cave filled with treasure chests, each filled with gold coins of different weights. The cave has an ancient security system where exceeding a total weight limit triggers deadly traps. The challenge is to determine the maximum weight of gold coins that can be extracted without activating these traps.

    Given an array of integers representing the weight of gold coins in each chest and an integer 'capacity' representing the maximum allowable weight, return the maximum weight of coins that can be carried without surpassing the capacity. You must achieve this by using each chest only once.

    Example:
    - If `combination_weights` = [2, 3, 5, 7] and `capacity` = 10, the correct output should be 10 because the combinations `2 + 3 + 5` maximize the total weight.
    - If `combination_weights` = [1, 2, 3, 4] and `capacity` = 5, the optimal load is 5 because you can use `1 + 4`.
    - If `combination_weights` = [1, 5, 10, 11] and `capacity` = 20, the best choice results in 16 by using `5 + 11`.

    Note:
    - Each weight represents a distinct chest. Chests can be used in combination as long as the total weight does not exceed the capacity.
    """

```

## Canonical Solution

```python
    def optimal_coin_load(weights, limit):
        if not weights:
            return 0
        dp = [0] * (limit + 1)
        for w in weights:
            for j in range(limit, w - 1, -1):
                dp[j] = max(dp[j], dp[j - w] + w)
        return dp[limit]
    return optimal_coin_load(combination_weights, capacity)
```

## Test Cases

```python
def check(candidate):
    assert candidate([2, 3, 5, 7], 10) == 10
    assert candidate([1, 2, 3, 4], 5) == 5
    assert candidate([1, 5, 10, 11], 20) == 16
    assert candidate([1, 3, 4, 5], 7) == 7
    assert candidate([10, 10, 10, 10], 5) == 0
    assert candidate([], 50) == 0
    assert candidate([1, 2, 3, 4, 5], 0) == 0
```

## Entry Point

`pirate_treasure`

## Extra Info

## Topics

['Dynamic Programming', 'Subset Sum']

## Cover Story

['pirate ship', 'ancient security system', 'traps']

## Cleaned Prompt

```python
{'function_definition': 'def pirate_treasure(combination_weights, capacity):\n', 'explanation': 'Given weights of gold coins in treasure chests and a maximum carrying capacity, calculate the maximum total weight of coins that can be taken without exceeding the capacity, each chest can be used not more than once.\n', 'examples': {'example_1': {'combination_weights': [2, 3, 5, 7], 'capacity': 10, 'output': 10}, 'example_2': {'combination_weights': [1, 2, 3, 4], 'capacity': 5, 'output': 5}, 'example_3': {'combination_weights': [1, 5, 10, 11], 'capacity': 20, 'output': 16}}}
```

## Warnings

- Solution failed correctness check. reason: failed: 
- 5, Mismatch Between Entry Point and Solution Method: The entry point is defined as 'pirate_treasure', but the 'canonical_solution' is using a different function name 'optimal_coin_load'. This will cause the function to not be invoked properly and the problem will be unsolvable without externally defining 'pirate_treasure' in the correct form.
- 5, Incorrect Solution Implementation in Problem Statement: The solution provided in 'canonical_solution' is defined with an inline 'optimal_coin_load' function but returns 'optimal_coin_load' as if it was declared outside. This results in incorrect function return scope which could lead to a runtime error of referencing an undefined function. The correct implementation needs to correct the return scope.

