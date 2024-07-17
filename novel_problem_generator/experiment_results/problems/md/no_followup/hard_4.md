# Task ID: hard/4

## Prompt

```python
def treasure_hunt_on_floating_island(dungeon_map):
    """
    Imagine a floating island containing hidden treasures scattered around in a magical dungeon represented as an 8-level octree (a tree where each parent node has exactly 8 children). Each node represents a room that could either contain gold or might be a portal to other rooms. Every level in the octree increases the depth and complexity of the dungeon.

    However, there is a cunning spell cast on the dungeon whereby certain rooms create invisible cycles that could trap an explorer forever. Your job is to use a reinforcement learning approach to detect any cycles in this dungeon (octree) so the treasure hunters can safely navigate the dungeon without being trapped.

    The dungeon_map is given as a list of tuples where each tuple contains two elements. The first element is an integer representing the numerical identifier of a room, and the second element is a list of integers representing direct connections to other rooms via portals.

    Output should return a boolean indicating whether there's a cycle in the dungeon.

    Example:
    Input: [(1, [2, 3]), (2, [3]), (3, [1])]
    Output: True (represents a cycle present from room 1 to 2 to 3 back to 1)

    Input: [(1, [2]), (2, [3]), (3, [4])]
    Output: False (no cycle present in the given rooms)
    """

```

## Canonical Solution

```python
    import random

    def is_cycle_present(node, adj_list, visited, rec_stack):
        visited[node] = True
        rec_stack[node] = True

        for neighbour in adj_list[node]:
            if not visited[neighbour]:
                if is_cycle_present(neighbour, adj_list, visited, rec_stack):
                    return True
            elif rec_stack[neighbour]:
                return True

        rec_stack[node] = False
        return False

    adj_list = {room[0]: room[1] for room in dungeon_map}
    visited = {room[0]: False for room in dungeon_map}
    rec_stack = {room[0]: False for room in dungeon_map}

    for room in dungeon_map:
        if not visited[room[0]]:
            if is_cycle_present(room[0], adj_list, visited, rec_stack):
                return True

    return False
```

## Test Cases

```python
def check(candidate):
    assert candidate([(1, [2, 3]), (2, [3]), (3, [1])]) == True
    assert candidate([(1, [2]), (2, [3]), (3, [4])]) == False
    assert candidate([(1, [2]), (2, [1]), (3, [4, 5]), (4, [5]), (5, [3])]) == True
    assert candidate([(1, [2]), (2, [1])]) == True
    assert candidate([]) == False
```

## Entry Point

`treasure_hunt_on_floating_island`

## Extra Info

## Topics

['Detect Cycle in Graph', 'Octree']

## Field

['Reinforcement Learning']

## Cover Story

['floating island', 'dungeon']

## Cleaned Prompt

```python
Given a dungeon in the form of an 8-level octree structure, write a function to detect any cycles to ensure the safety of treasure hunters. The input is provided as a list of tuples where each tuple consists of a room's identifier and a list of connected rooms. Output whether a cycle is present.

Example:
- Input: [(1, [2, 3]), (2, [3]), (3, [1])]
  Output: True (This indicates a cycle from room 1 to 2 to 3 and back to 1 is present)
- Input: [(1, [2]), (2, [3]), (3, [4])]
  Output: False (There is no cycle in these rooms)
```

## Warnings

- Solution failed correctness check. reason: failed: 4
- 5, Misleading prompt: The problem statement initially mentions the use of a reinforcement learning approach for detecting cycles in an octree representing a dungeon. However, the provided canonical solution uses a straightforward graph traversal or depth-first search (DFS) technique instead of employing reinforcement learning methods. This disparity between the suggested method (reinforcement learning) and the actual method used (DFS) in the solution makes the prompt misleading.
- 5, Inconsistent graph structure: The problem introduces the dungeon map as an 8-level octree where each parent node has exactly 8 children, but the example input and the solution treat the dungeon as a general graph with arbitrary connections. This inconsistency in describing the graph structure (octree vs general graph with cycles) can confuse participants about the nature and constraints of the problem.
- 4, Incompleteness in explanation of outputs: The problem statement would improve by including the reasoning behind each output in examples, particularly explaining why a specific configuration forms a cycle or not. This can aid in understanding and thus help avoid confusion.

