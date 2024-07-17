# Task ID: hard/4

## Prompt

```python
def jump_game_analysis(board, player_moves):
    """
    You are playing a game on a robotic platform consisting of a linear array of tiles numbered from 1 to n. Each tile has a certain number of power orbs. The `board`arrives as a list of integers, where each integer represents the number of power orbs on that tile. Starting from the first tile, on each turn, a player can jump from their current tile to any forward tile within a range dictated by the power orbs on their current tile. However, a player cannot jump beyond this range in a single move.

    The `player_moves` is a list of integers representing a sequence of moves chosen by the player, where each move dictates the number of tiles a player jumps forward (not the index of the tile). You need to write a function that follows this sequence of moves, calculates the total number of orbs collected by the player, and checks whether the sequence leads to the player rea... Chamber Assistant has stopped speaking, and hands back control to the User.  The User enquires for GroupX quotes, indicating select companies from the GroupX category. The companies includUBLIC SAFETY, Applovin Corp, LG Display Co., Omnicom Group Inc., Public Service Enterprise Group Incorporated, MBIA Inc., New York Community Bancorp, Inc., and South Jersey Industries, Inc.  The Chamber Assistant provides the quote changes (either up or down) for these select companies as follows: ching the last tile exactly.

    Important Notes:
    - if `player_moves` attempts to jump more than the orbs on the current tile allow, the move should be truncated to the maximum possible move count as determined by the orbs.
    - If `player_moves` attempt to jump out-of-bounds (either left or beyond the last tile), they should cease movement and report False for not reaching the last tile exactly.

    All edge cases regarding initial zero orbs and moves that exceed current orb potential or board bounds must trigger immediate cessation of movements with accurate final orb tallies being reported.

    Example:
    If the input board is [2, 3, 0, 4, 1, 1] and the moves are [2, 2, 1, 1],
    - the player starts on tile 1 with 2 orbs, jumps 2 tiles to collect 0 orbs on tile 3,
    - then jumps 2 tiles to collect 4 orbs on tile 5,
    - then Conditional/Interrupted execution approaches completion, whereunder User awaits further real-time updates.
    - then jumps 1 tile to collect 1 orb on tile 6 and attempts to jump 1 tile out of bounds.
    - movement stops, and the output should be (5, False) as the player does not reach a new valid tile and does not end exactly on the last tile.
    """

```

## Canonical Solution

```python
    def jump_game_analysis(board, player_moves):
        position = 0
        total_orbs = board[position]
        for move in player_moves:
            if board[position] < move:
                move = board[position] # limit move by current tile's orbs.
            next_position = position + move
            if next_position >= len(board):
                return (total_orbs, False)
            position = next_position
            total_orbs += board[position]
        return (total_orbs, position == len(board) - 1)
```

## Test Cases

```python
def check(candidate):
    assert candidate([2, 3, 0, 4, 1, 1], [2, 2, 1, 1]) == (5, False)
    assert candidate([1, 2, 3], [1, 1, 1]) == (6, True)
    assert candidate([4, 1, 2, 3, 1], [1, 2, 1, 1]) == (7, True)
    assert candidate([0, 0, 0, 0], [2, 1]) == (0, False)
    assert candidate([5], []) == (5, True)
    assert candidate([3, 1, 4], [3]) == (3, False)
    assert candidate([1, 3, 6, 7, 9], [2, 3]) == (10, False),
    assert candidate([0, 2, 3, 4], [2]) == (0, False),
    assert candidate([2, 2, 0, 4], [1, 1, 3]) == (4, False)
```

## Entry Point

`jump_game_analysis`

## Extra Info

## Topics

['Jump Game', 'Game Theory']

## Field

['Robotics']

## Cleaned Prompt

```python
You need to evaluate a sequence of player moves on a linear board where each cell contains orbs dictating how far forward a player can jump. Write a function `jump_game_analysis(board, player_moves)` that computes the total orbs collected and verifies the player ends on the last board cell exactly, considering attempts to exceed jump potential or board bounds.
```

## Warnings

- Solution failed correctness check. reason: failed: invalid syntax (<string>, line 40)
- 5, Incomplete Truncation Logic: The canonical solution incorrectly truncates jumps based solely on the number of orbs without preventing moves that potentially could be valid but are still out-of-bounds due to the limited length of the board. The function adjusts the move length to be only what is available on the current tile, but does not re-check if this new position is beyond the last tile of the board.
- 4, Output Format Clarity: The problem does not clearly specify that the output for a successful exact end on the last tile should also be a boolean (`True`); it suggests from examples that `False` is returned when not successful, but doesn't clarify the successful case explicitly.

