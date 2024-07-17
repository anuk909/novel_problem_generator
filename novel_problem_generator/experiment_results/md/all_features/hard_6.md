# Task ID: hard/6

## Prompt

```python
def count_artifacts(grid):
    """
    Suppose you are in a fairy tale world where there has just been a supernatural storm that has scattered magical artifacts all over a kingdom represented by a 2D grid. Each cell in this grid can either be empty (0) or contain part of a magical artifact (1).

    Magical artifacts can be spread over multiple cells but will always form a linear horizontal or vertical segment. Fortunately, the artifacts remain intact in their segments post-storm.

    Your task is to determine how many distinct artifacts are there in the grid. Each artifact is a continuous line of '1's vertically or horizontally. Connections are not counted diagonally. Furthermore, each '1' in the grid is part of exactly one artifact.

    The grid is guaranteed to have dimensions between 1x1 and 500x500.

    Example:
    For the grid:
        [
            [1, 0, 0, 1, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 1, 0, 0],
            [0, 1, 1, 0, 1]
        ]
    The function should return 6, as there are six distinct artifacts:
        - Two vertical artifacts of length 2 at the first and fourth column.
        - Two horizontal artifacts of length 2 at the fourth row.
        - One vertical artifact of length 1 in the third row, third column.
        - One horizontal artifact of length 1 in the third row.
    """

```

## Canonical Solution

```python
    def count_artifacts(grid):
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        count = 0

        def dfs(r, c, direction):
            if direction == 'horizontal':
                while c < cols and grid[r][c] == 1 and not visited[r][c]:
                    visited[r][c] = True
                    c += 1
            else:  # direction == 'vertical'
                while r < rows and grid[r][c] == 1 and not visited[r][c]:
                    visited[r][c] = True
                    r += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    if c == 0 or grid[r][c-1] == 0:
                        dfs(r, c, 'horizontal')
                        count += 1
                    if r == 0 or grid[r-1][c] == 0:
                        dfs(r, c, 'vertical')
                        count += 1
        return count
```

## Test Cases

```python
def check(candidate):
    assert candidate([[1, 0, 0, 1, 1], [1, 0, 0, 1, 1], [0, 0, 1, 0, 0], [0, 1, 1, 0, 1]]) == 6
    assert candidate([[1, 1, 0, 1], [1, 1, 0, 1], [0, 0, 1, 1]]) == 3
    assert candidate([[1, 0, 1], [0, 1, 0], [1, 0, 1]]) == 5
    assert candidate([[1]]) == 1
    assert candidate([[0,0,0,0],[0,0,0,0]]) == 0
```

## Entry Point

`count_artifacts`

## Extra Info

## Topics

['Counting Sort', 'Line Sweep']

## Field

['Computer Vision']

## Cover Story

['supernatural storm', 'fairy tale']

## Cleaned Prompt

```python
Write a function that receives a 2D grid, each cell in the grid being either empty (0) or contain part of a magical artifact (1). Artifacts form continuous horizontal or vertical segments of '1's. Your function should count and return the number of distinct magical artifacts in the grid. Artifacts do not connect diagonally and each '1' belongs to exactly one artifact. For example, in a grid [[1, 1, 0], [0, 0, 0], [1, 0, 1]], the count of artifacts would be 3.
```

## Warnings

- Solution failed correctness check. reason: failed: 
- 5, Logical flaw in algorithm implementation: The provided canonical solution has a critical logical flaw where it checks cell-by-cell for starting new artifacts both horizontally and vertically without proper conditions to determine the actual start of an artifact. This approach leads to the double-counting of artifacts that can start from intersecting horizontal and vertical lines. This violates the constraint where each '1' in the grid is part of exactly one artifact. The DFS function is incorrectly initialized for every '1' that follows an empty cell or edge cell, regardless of whether it's part of an already counted segment or starting a new unique segment, particularly when such a cell could be reached through horizontal and vertical paths simultaneously.

