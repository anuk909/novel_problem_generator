# Task ID: hard/3

## Prompt

```python
def find_optimal_wind_route(matrix):
    """
    Imagine navigating a grid where each cell depicts wind resistance at that location with a tuple in the format (incoming_strength, outgoing_strength). Here, 'incoming_strength' is the resistance experienced when entering the cell and 'outgoing_strength' is the resistance when leaving the cell.

    Your task is to move from the top-left corner (starting point) to the bottom-right corner (destination) of the grid, minimizing the total resistance experienced. You can only move right or down, and moving into a new cell incurs the 'incoming_strength' at that cell as a cost.

    Write a function to calculate the minimum total resistance required to traverse the matrix.

    Example:
    Input: [
        [(0, 2), (3, 1)],
        [(1, 4), (2, 0)]
    ]
    Output: 1 (Right from (0,0) costing 3 to (0,1), then Down from (0,1) costing 0 to (1,1))

    Notes:
    - The matrix will always be a non-empty 2D array.
    - Each tuple in the matrix contains non-negative integers.
    """
```

## Canonical Solution

```python
    def find_optimal_wind_route(matrix):
        m, n = len(matrix), len(matrix[0])
        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0] = 0
        for i in range(m):
            for j in range(n):
                if j + 1 < n:
                    dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + matrix[i][j+1][0])
                if i + 1 < m:
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + matrix[i+1][j][0])
        return dp[-1][-1]
```

## Test Cases

```python
def check(candidate):
    assert candidate([[(0, 2), (3, 1)], [(1, 4), (2, 0)]]) == 1
    assert candidate([[(1, 2), (2, 2), (3, 4)], [(4, 0), (5, 1), (1, 3)], [(1, 1), (2, 0), (0, 2)]]) == 3
    assert candidate([[(2, 0)], [(1, 5)]]) == 0
    assert candidate([[(0, 1), (1, 0)], [(3, 2), (1, 4)]]) == 2
    assert candidate([[(1, 3), (1, 3), (1, 3)], [(2, 1), (2, 1), (2, 1)], [(3, 0), (3, 0), (3, 0)]]) == 7
```

## Entry Point

`find_optimal_wind_route`

## Extra Info

## Topics

['Dynamic Programming', 'Grid Traversal']

## Cover Story

['wind resistance', 'grid navigation']

## Cleaned Prompt

```python
Write a function to calculate the minimum total resistance required to traverse a grid from the top-left to the bottom-right. Each cell has a tuple (incoming_strength, outgoing_strength), and moving to a new cell costs the 'incoming_strength' of that cell. The goal is to determine the path with the minimum total resistance.
```

## Warnings

- Solution failed correctness check. reason: failed: invalid syntax (<string>, line 19)
- 5, Misinterpretation in Problem Statement: The problem prompt includes an example that does not take into account the 'outgoing_strength' for each movement, which conflicts with the tuple descriptions provided in the matrix. This leads to ambiguity on whether the 'outgoing_strength' should play a role in the cost calculation, making the problem unsolvable as stated.
- 4, Lack of Edge Case Testing: The test cases do not explicitly check for minimal edge (1x1 grid) or with unusual patterns of wind strength that may cause irregular routes, which are essential to determine the robustness of the solution under diverse conditions.

