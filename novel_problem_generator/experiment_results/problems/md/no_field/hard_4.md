# Task ID: hard/4

## Prompt

```python
def cave_exploration(grid):
    """
    In a museum display, there is a representation of a mysterious cave system arranged as a 2D grid. Each section of the grid can either be a wall ('W'), an empty space ('E'), or a treasure ('T'). The task is to find all the treasure which is in one 'strongly connected' space without moving diagonally.

    A 'strongly connected' space is defined as regions connected orthogonally (up, down, left, or right) without any interruptions by walls. Each unique space can be considered a separate cave. Within each cave, if there is at least one treasure ('T'), then all empty spaces ('E') and the treasures in that cave are considered part of the treasure area.

    Your function should return a list of integers where each integer represents the size of a treasure area in any cave found in the grid, sorted in descending order.

    For example, given the grid:
        [
         ['E', 'W', 'T'],
         ['T', 'W', 'E'],
         ['E', 'E', 'T']
        ]
    The grid has two distinct caves. One cave comprises elements {'E'} on the most left column and the other contains the elements {'T', 'E', 'T', 'E', 'E'} where we count the two top items connected despite being separated by 'W' in the original definition.

    Note:
    - There can be multiple caves and even nested caves. Nested caves are treated as multiple unique caves.
    - Only consider horizontal and vertical connections, no diagonal.
    - Treat each 'T' as part of the returned size if it belongs to the cave with treasures.
    """

```

## Canonical Solution

```python
    def dfs(grid, x, y, visited):
        n, m = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        stack = [(x, y)]
        size = 0
        has_treasure = False
        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in visited:
                continue
            visited.add((cx, cy))
            if grid[cx][cy] == 'W':
                continue
            if grid[cx][cy] == 'T':
                has_treasure = True
            size += 1
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and grid[nx][ny] != 'W':
                    stack.append((nx, ny))
        return size if has_treasure else 0

    def cave_exploration(grid):
        visited = set()
        treasure_sizes = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] != 'W':
                    size = dfs(grid, i, j, visited)
                    if size > 0:
                        treasure_sizes.append(size)
        treasure_sizes.sort(reverse=True)
        return treasure_sizes
```

## Test Cases

```python
def check(candidate):
    assert candidate([
        ['E', 'W', 'T'],
        ['T', 'W', 'E'],
        ['E', 'E', 'T']
    ]) == [5]
    assert candidate([
        ['W', 'W', 'W'],
        ['W', 'W', 'W'],
        ['W', 'W', 'W']
    ]) == []
    assert candidate([
        ['E', 'E'],
        ['T', 'T']
    ]) == [4]
    assert candidate([
        ['T', 'W'],
        ['E', 'E']
    ]) == [1]
    assert candidate([
        ['E', 'T', 'E', 'W', 'T'],
        ['W', 'E', 'W', 'W', 'E'],
        ['E', 'T', 'E', 'E', 'T']
    ]) == [7, 1]
```

## Entry Point

`cave_exploration`

## Extra Info

## Topics

['Divide and Conquer', 'Strongly Connected Component']

## Cover Story

['museum', 'mysterious cave']

## Cleaned Prompt

```python
def cave_exploration(grid):
    """
    Given a grid representing a cave system, where each cell can be a wall ('W'), an empty space ('E'), or a treasure ('T'), return a list of the size of each 'strongly connected' treasure area sorted in descending order.

    - Use Depth-First Search to explore caves.
    - Count size of treasure area in caves.
    - Only explore orthogonal connections, no diagonals are considered.
    """
```

## Warnings

- Solution failed correctness check. reason: failed: 
- 5, Incorrect Example Explanation: The problem statement contains an example explanation that contradicts the defined problem behavior. Specifically, it states that elements separated by a 'W' are counted together, which defies the intended logic of treating 'W' as an interruption in the connection of cave regions.
- 5, Misleading Problem Description: The prompt's definition of 'strongly connected' and the handling of orthogonal connections appear to be incorrectly applied in the example provided. This can lead to confusion and incorrect implementations as the example suggests connectivity that should not exist per the initial rules.
- 4, Test Case Validity: The test cases provided in the problem statement may lead to incorrect solutions being considered correct, or vice versa, especially with how connectivity through walls ('W') is handled. This could result in erroneous assumptions and a failure in accurately testing the core functionality of the solution.

