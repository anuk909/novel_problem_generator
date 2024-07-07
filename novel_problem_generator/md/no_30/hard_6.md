# Task ID: hard/6

## Prompt

```python
def spaceship_command_sequence(grid, commands):
    """
    In a universe where space travel is navigated through controlled grids and commands, there exists a grid system where each cell either contains a portal ('P'), a rock ('#'), or is empty ('.'). A spaceship starts at the top-left corner of the grid. Using a series of commands, the spaceship tries to move toward a portal to travel to a new dimension. The command sequence consists of 'U' (up), 'D' (down), 'L' (left), and 'R' (right).

    Given a grid and a sequence of commands, write a function that returns the final position (as a tuple of coordinates) of the spaceship after the completion of the given command sequence. If the spaceship encounters a rock ('#'), it cannot proceed in that direction and thus stays in the current position. If it tries to move outside the grid boundaries or reaches a portal ('P'), the command sequence is halted immediately, and the current position is returned.

    For example, consider the following grid and commands:
    Grid:
    [
        ['.', '.', '.'],
        ['.', '#', 'P'],
        ['.', '.', '.']
    ]
    Commands: "DRR"

    Starting from the top-left corner (0, 0), the spaceship would:
    - Move down to (1, 0)
    - Attempt to move right but encounters a rock at (1, 1), it remains at (1, 0)
    - Moves right to (1, 2), encountering a portal, thus halting the command sequence.
    The function should return (1, 2).

    Note:
    - The grid will have at least one row and one column.
    - The spaceship always starts at the top-left corner (0, 0).
    - The grid will always contain at least one portal.
    - Commands end if the spaceship encounters a portal or an invalid move.
    
"""

```

## Canonical Solution

```python
    def spaceship_command_sequence(grid, commands):
        x, y = 0, 0  # Start position
        max_rows = len(grid)
        max_cols = len(grid[0])
        direction_map = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        for command in commands:
            dx, dy = direction_map[command]
            new_x = x + dx
            new_y = y + dy
            if 0 <= new_x < max_rows and 0 <= new_y < max_cols:
                if grid[new_x][new_y] == '#':
                    continue
                if grid[new_x][new_y] == 'P':
                    return (new_x, new_y)
                x, y = new_x, new_y
            else:
                break
        return (x, y)
```

## Test Cases

```python
def check(candidate):
    grid1 = [['.', '.', '.'], ['.', '#', 'P'], ['.', '.', '.']]
    commands1 = "DRR"
    assert candidate(grid1, commands1) == (1, 2)

    grid2 = [['.', '.', '.', '.'], ['.', '#', 'P', '.'], ['.', '.', '.', 'P']]
    commands2 = "DDRRUUL"
    assert candidate(grid2, commands2) == (1, 0)

    grid3 = [['P', '#', '.'], ['.', '.', '.'], ['.', '.', '.']]
    commands3 = "RRD"
    assert candidate(grid3, commands3) == (0, 0)

    grid4 = [['.', 'P'], ['.', '.']]
    commands4 = "R"
    assert candidate(grid4, commands4) == (0, 1)

    grid5 = [['.', '.', '.', 'P'], ['.', '#', '.', '.'], ['.', '.', '.', '.']]
    commands5 = "RRRDD"
    assert candidate(grid5, commands5) == (0, 3)
    grid6 = [['.', '.', '.', '.'], ['P', '.', '.', '.'], ['.', '.', '.', '.']]
    commands6 = "DL"
    assert candidate(grid6, commands6) == (1, 0)
```

## Entry Point

`spaceship_command_sequence`

## Extra Info

## Topics

['Binary Tree', 'Word Search']

## Field

['Reinforcement Learning']

## Cover Story

['rocket', 'portal']

## Cleaned Prompt

```python
Given a grid representing a space with empty cells ('.'), rocks ('#'), and portals ('P'), and a series of move commands ('U' for up, 'D' for down, 'L' for left, 'R' for right), compute the final position of a spaceship starting at the top-left corner after executing the commands. The sequence stops if the ship encounters a rock, moves outside the grid, or reaches a portal.
```

## Warnings

- Solution failed correctness check. reason: failed: 
- 4, Contradictory Instructions: The problem statement mentions that the command sequence ends whenever the spaceship encounters a rock ('#') or an invalid move, but the example "DDRRUUL" in the test cases suggests the spaceship can continue commands after stopping due to a rock. This contradiction between the description and provided example leads to ambiguity on how to correctly handle encountering a rock.

