# Task ID: medium/2

## Prompt

```python
def escape_dungeon(dungeon_map):
    """
    Given a grid where each cell can either be passable ('.') or blocked by an obstacle ('#'), find a probable escape path from the top-left corner (start) to the bottom-right corner (exit). Use a probabilistic approach, specifically a randomized version of Depth-First Search (DFS), to find one of the possible paths.

    The function should return a list of tuples representing the path from start to exit, each tuple containing the coordinates (row, column) of a cell in the path.

    Parameters:
    `dungeon_map`: List of strings where each string represents a row of the dungeon grid.

    Example:
    For dungeon_map=['.#.', '..#', '#..'], a valid output could be [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)].

    Note:
    - The selected path should not revisit cells.
    - The solution should effectively utilize randomness to simulate decision making under uncertainty.
    """

```

## Canonical Solution

```python
	import random

	def is_valid(x, y, n, m):
	    return 0 <= x < n and 0 <= y < m

	def escape_dungeon(dungeon_map):
	    n, m = len(dungeon_map), len(dungeon_map[0])
	    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	    stack = [(0, 0)]
	    visited = set(stack)
	    path = []

	    while stack:
	        current = stack.pop()
	        path.append(current)
	        if current == (n-1, m-1):
	            return path

	        possible_moves = []
	        for dx, dy in directions:
	            nx, ny = current[0] + dx, current[1] + dy
	            if is_valid(nx, ny, n, m) and (nx, ny) not in visited and dungeon_map[nx][ny] == '.':
	                possible_moves.append((nx, ny))

	        if possible_moves:
	            chosen = random.choice(possible_moves)
	            stack.append(chosen)
	            visited.add(chosen)

	    return path

```

## Test Cases

```python
def check(candidate):

	assert len(candidate(['.#.', '..#', '#..'])) >= 3
	assert len(candidate(['...', '...', '...'])) >= 3
	assert candidate(['###', '#.#', '###']) == [(0, 0)]
	assert len(candidate(['.#.', '...', '.#.'])) >= 3
	assert len(candidate(['...', '.#.', '...'])) >= 3
```

## Entry Point

`escape_dungeon`

## Extra Info

## Topics

['Depth-First Search', 'Randomized Algorithms']

## Field

['Pathfinding']

## Cover Story

['dungeon', 'grid']

## Cleaned Prompt

```python
Create a function to find an escape path from a grid-based dungeon using a randomized Depth-First Search (DFS). Each cell in the grid is either passable ('.') or blocked ('#'). The path should not revisit cells and should effectively utilize randomness.
```

## Warnings

- Solution failed correctness check. reason: failed: inconsistent use of tabs and spaces in indentation (<string>, line 17)
- 4, Misleading Problem Constraints: The prompt suggests that the function should be a 'probabilistic' or randomized approach, but the use of randomness isn't well-explicit in either the problem statement or in the example provided, aside from a simple random choice among possible moves. The function should have more complexity or explanation on how randomness significantly affects the path computation beyond trivial decision-making among equivalently valid options.
- 5, Test Cases Not Covering Key Edge Cases: The test cases provided do not account for several edges cases such as very large grids, all cells blocked except start and end, or shapes of the grid differing (e.g., non-rectangle shapes or having several disconnected sections). Such limitations in the test might lead to solutions passing without properly handling all feasible real-world scenarios that the function should account for.

