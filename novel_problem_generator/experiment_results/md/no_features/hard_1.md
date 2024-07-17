# Task ID: hard/1

## Prompt

```python
def treasure_hunt(matrix):
    """
    You are given a 2D matrix where each cell contains an integer. The goal is to find the shortest path from the top-left corner (0, 0) to the bottom-right corner (len(matrix)-1, len(matrix[0])-1), where the difference in value between two consecutive cells is minimal.

    The path can only move either right or down at each step. The score of a path is determined by the maximum difference in values between any two consecutive cells along the path.

    Write a function that returns the minimum score of all possible paths from the top-left corner to the bottom-right corner.

    Example Input:
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
    
The function should return 1, because the path 1 -> 2 -> 3 -> 6 -> 9 has the minimal maximum difference in values between consecutive cells.

    Example:
    Input: [[3, 10, 6], [9, 7, 3], [0, 5, 8]]
    Output: 5 (One minimal path is: 3 -> 9 -> 7 -> 5 -> 8 with maximum consecutive difference of 5 between 9 and 7)
    """

```

## Canonical Solution

```python
    from heapq import heappop, heappush
    def treasure_hunt(matrix):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0] = 0
        heap = [(0, 0, 0)]
        while heap:
            score, x, y = heappop(heap)
            for dx, dy in ((1, 0), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    next_score = max(score, abs(matrix[nx][ny] - matrix[x][y]))
                    if next_score < dp[nx][ny]:
                        dp[nx][ny] = next_score
                        heappush(heap, (next_score, nx, ny))
        return dp[m-1][n-1]
```

## Test Cases

```python
def check(candidate):
    assert candidate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 1
    assert candidate([[3, 10, 6], [9, 7, 3], [0, 5, 8]]) == 5
    assert candidate([[0]]) == 0
    assert candidate([[1, 100], [1000, 1001]]) == 1
    assert candidate([[100, 300, 200], [600, 400, 500], [300, 200, 100]]) == 200
    assert candidate([[5, 4], [3, 2]]) == 1
```

## Entry Point

`treasure_hunt`

## Extra Info

## Cleaned Prompt

```python
You are given a 2D matrix of integers. Find the shortest path from the top-left to the bottom-right corner that minimizes the maximum difference in value between two consecutive cells, only moving right or down. Return this minimum possible maximum difference. Example: For matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]], the function should return 1, as the best path is 1 -> 2 -> 3 -> 6 -> 9 with a maximal consecutive difference of 1.
```

## Warnings

- Solution failed correctness check. reason: failed: 
- 5, Undefined Behavior for Empty Matrices: The function description and prompt do not specify the expected behavior when the input matrix is empty either by being an empty list or having empty sublists. This can lead to undefined or erroneous behavior if not handled properly in the implementation.
- 5, Inadequate Handling of Non-Rectangular Matrices: The problem statement does not specify whether the input matrix will always be rectangular. Non-rectangular (jagged) matrices could lead to runtime errors or incorrect behavior since the expectation for movement between cells would be ambiguous or undefined.
- 4, Performance Expectations Undefined: There are no specifications or constraints provided about the expected matrix size or time/space complexity requirements. This omission can lead to solutions that are inefficient for large datasets, potentially causing performance issues in real-world applications or competitive scenarios.

