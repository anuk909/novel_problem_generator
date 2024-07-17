# Task ID: hard/6

## Prompt

```python
def max_path_sum(grid):
    """
    Given a matrix of integers representing a grid, start at the top-left corner and find a path to the bottom-right corner which maximizes the sum of integers in the path. You may only move down or right at any step.

    For example, if the grid is:
        [
         [1, 3, 1],
         [1, 5, 1],
         [4, 2, 1]
        ]
The output should be 12 because the maximum sum path is from the top-left corner 1 -> 3 -> 5 -> 2 -> 1, which results in the sum of 1+3+5+2+1 = 12.

    Note:
    - The grid size will be at least 1x1.
    - All numbers in the grid will be integers.
    """

```

## Canonical Solution

```python
    def max_path_sum(grid):
        n = len(grid)
        m = len(grid[0])
        for i in range(1, n):
            grid[i][0] += grid[i-1][0]
        for j in range(1, m):
            grid[0][j] += grid[0][j-1]
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] += max(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
```

## Test Cases

```python
def check(candidate):
    assert candidate([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 12
    assert candidate([[1]]) == 1
    assert candidate([[1, 3, 1], [1, 5, 1]]) == 10
    assert candidate([[2], [3], [5]]) == 10
    assert candidate([[1, 2, 3, 0], [0, 0, 0, 10], [9, 8, 7, 6]]) == 27
```

## Entry Point

`max_path_sum`

## Extra Info

## Cleaned Prompt

```python
Write a function 'max_path_sum(grid)' that computes the maximum sum of a path from the top-left corner to the bottom-right corner in a grid where moves are restricted to right and down. The function input 'grid' is a 2D matrix of integers.
```

## Warnings

- Solution failed correctness check. reason: failed: 
- 5, Problem description contradiction: The prompt example path is incorrect based on the provided logic. The prompt suggests moving from the top-left to the bottom-right using the path 1 -> 3 -> 5 -> 2 -> 1, leading to a sum path of 13 (not 12 as stated). Yet, the problem statement states that paths can only move right or down, hence a correct path according to this rule (assuming no skipping) should be 1 -> 3 -> 1 -> 5 -> 1 -> 1 for a sum of 12. However, the stated path yields a sum of 13 instead. There's a computation error or a misunderstanding of how the path is described or calculated. This could confuse the participants about the rules or methods to find the path.

