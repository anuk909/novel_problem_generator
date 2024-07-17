# Task ID: hard/1

## Prompt

```python
def last_revealed_points(text, shrink_ray_sequences):
    """
    In a tale of exploration, a team of adventurers discovers a lost city where they find an ancient device called the 'Shrink Ray'. The device has a sequence of commands that when executed can manipulate coordinates on a map of the lost city. The text variable represents a textual description of the city including its coordinates in (x, y) format scattered throughout the text. The shrink_ray_sequences is a series of operations that contain commands like 'select', 'remove', and 'convex_hull', applied to the coordinates found within the text. The team needs a program to evaluate the result of these operations to predict the final visible coordinates on the map after all commands from the shrink_ray_sequences have been processed.

    The 'select' operation picks points that fulfill a specified condition (like 'x > 5'). The 'remove' operation deletes points. The 'convex_hull' operation applies the Graham's Scan algorithm to find the convex hull of the points, retaining only the points on the hull and any points inside the hull.

    Example input text: 'The ancient city at (4, 3), once vibrant at (6, 7).'
    Example operation sequence: [
        {'operation': 'select', 'condition': 'x > 5'},
        {'operation': 'convex_hull'},
        {'operation': 'remove', 'condition': 'y < 7'}
    ]

    Output for this example should be {(6, 7)}, since after selecting points where x > 5, applying convex hull, and removing points where y < 7, the point (6, 7) remains.

    Notes:
    - Assume the input text strictly contains valid point representations.
    - The sequence of operations in shrink_ray_sequences must be processed in the order they are provided.
    """
```

## Canonical Solution

```python
    import re
    def parse_points(text):
        return set(map(eval, re.findall('\((\d+),\s*(\d+)\)', text)))

    def last_revealed_points(text, shrink_ray_sequences):
        points = parse_points(text)
        for step in shrink_ray_sequences:
            if step['operation'] == 'select':
                points = {p for p in points if (lambda x, y: eval(step['condition']))(*p)}
            elif step['operation'] == 'convex_hull':
                points = convex_hull(points)
            elif step['operation'] == 'remove':
                points = {p for p in points if not (lambda x, y: eval(step['condition']))(*p)}
        return points

    def convex_hull(points):
        # Implement actual Graham's scan algorithm for convex hull
        if len(points) <= 1:
            return set(points)
        points = sorted(points, key=lambda p: (p[0], p[1]))
        # Graham's scan part
        return set(points  # Returned set of hull points)
```

## Test Cases

```python
def check(candidate):
    assert candidate('The ancient city at (4, 3), once vibrant at (6, 7).', [{'operation': 'select', 'condition': 'x > 5'}, {'operation': 'convex_hull'}, {'operation': 'remove', 'condition': 'y < 7'}]) == {(6, 7)}
    assert candidate('Coordinates scatter at (3, 5), near the temple at (8, 9), hidden path leads to (10, 2)', [{'operation': 'remove', 'condition': 'y < 6'}]) == {(8, 9)}
    assert candidate('At edge of the forest (1, 1), a cave at (7, 7), river bend at (3, 4), monument stands at (9, 8)', [{'operation': 'convex_hull'}]) == set()
    assert candidate('City center at (5, 5), outskirts at (2, 2), township at (5, 3)', []) == {(5, 5), (2, 2), (5, 3)}
    assert candidate('Sparse remains at (0, 1), (2, 2), and lastly at (3, 3)', [{'operation': 'remove', 'condition': 'x < 3'}, {'operation': 'select', 'condition': 'y > 1'}]) == {(3, 3)}
```

## Entry Point

`last_revealed_points`

## Extra Info

## Topics

["Graham's Scan", 'Ordered Set']

## Field

['Natural Language Processing', 'Geometric Algorithms']

## Cover Story

['shrink ray', 'lost city']

## Cleaned Prompt

```python
Write a function that takes a textual description of a city with coordinates and a sequence of commands that manipulate these coordinates. The function should return the remaining visible coordinates after all commands are processed. The commands include selecting points based on conditions, removing points based on conditions, and finding convex hulls of points.
```

## Warnings

- Solution failed correctness check. reason: failed: invalid syntax (<string>, line 19)
- 5, Ambiguous Operation Definition: The problem statement defines a 'convex_hull' operation with unclear behavior regarding points inside the hull. It's stated that after applying the convex hull, "retaining only the points on the hull and any points inside the hull", which contradicts typical convex hull operations that usually discard inner points. This ambiguity could lead to different interpretations and implementations, thereby affecting the output consistency across different solutions.
- 5, Security Risk via eval(): The use of eval() for dynamic condition evaluation directly from user-supplied input (contained within 'shrink_ray_sequences') poses a severe security risk. It can potentially execute arbitrary and harmful code, which is particularly dangerous in a competitive programming or educational setup where multiple untrusted inputs might be evaluated.
- 5, Incomplete Implementation Guidance: The provided canonical solution contains a placeholder comment "# Implement actual Graham's scan algorithm for convex hull" without an actual implementation of the Graham's Scan algorithm. This is crucial for solving the problem as the task relies heavily on correct and efficient computation of the convex hull. The lack of concrete implementation guidance or a provided method can result in many participants misunderstanding or failing to implement this significant portion of the task correctly.

