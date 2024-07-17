# Task ID: hard/5

## Prompt

```python
def haunted_treasure_diary(diary_entries, treasure_coords):
    """
    In a scenario where you're exploring a haunted house, you discover an old diary peppered with hints to hidden treasures expressed in coordinates embedded in DNA-like sequence strings. Each diary entry, composed of the characters 'A', 'C', 'G', 'T', encodes a potential treasure location.

    Given a list of these string entries and real-world treasure coordinates as tuples (x, y), determine which treasure coordinates are most likely represented in the diary using a KD-Tree algorithm for efficient nearest-neighbor searching.

    Entries are decoded to coordinates by counting occurrences of each character:
    - 'A' adds positively to the x-coordinate
    - 'C' subtracts from the x-coordinate
    - 'G' adds positively to the y-coordinate
    - 'T' subtracts from the y-coordinate

    The 'closeness' between the decoded points and actual treasures is determined using Euclidean distance where the nearest point in the KD-Tree represents a likely match.

    Example:
    diary_entries = ['AAGCT', 'CCGTAA', 'TTGG'],
    treasure_coords = [(2, 1), (3, -1), (-1, 1)],
    The output should be [(2, 1)] as the treasure at (2, 1) closely corresponds to the diary entry 'AAGCT'.

    Notes:
    - A diary entry could potentially describe multiple treasures if distances are equivalent.
    - Diary entries and treasure points could have varying scales.
    """

```

## Canonical Solution

```python
    from scipy.spatial import KDTree
    def decode(entry):
        x = entry.count('A') - entry.count('C')
        y = entry.count('G') - entry.count('T')
        return x, y

    decoded_points = [decode(entry) for entry in diary_entries]
    tree = KDTree(treasure_coords)
    closest = set()
    for point in decoded_points:
        _, i = tree.query(point)
        closest.add(tuple(treasure_coords[i]))

    return list(closest)
```

## Test Cases

```python
def check(candidate):
    assert candidate(['AAGCT', 'CCGTAA', 'TTGG'], [(2, 1), (3, -1), (-1, 1)]) == [(2, 1)]
    assert candidate(['AAAA', 'CCCC', 'GGGG', 'TTTT'], [(4, 0), (-4, 0), (0, 4), (0, -4)]) == [(4, 0), (-4, 0), (0, 4), (0, -4)]
    assert candidate(['ACGT', 'TGCA'], [(0, 0)]) == [(0, 0)]
    assert candidate(['AAAACCCCGGGGTTTT', 'AAGCT'], [(10, 10), (2, 1)]) == [(10, 10), (2, 1)]
    assert candidate(['GGG'], [(0, 3)]) == [(0, 3)]
```

## Entry Point

`haunted_treasure_diary`

## Extra Info

## Topics

['String', 'KD-Tree']

## Field

['Bioinformatics']

## Cover Story

['haunted house', 'treasure']

## Cleaned Prompt

```python
Given a list of string diary entries encoded with characters 'A', 'C', 'G', 'T' which map to masked coordinates, and a list of real treasure coordinates as tuples, return the list of treasure coordinates that, using a KD-Tree algorithm and Euclidean distance as the measure of closeness, are most likely to be described by the diary entries.
```

## Warnings

- Solution failed correctness check. reason: failed: 'NoneType' object is not callable
- 4, Ambiguous Problem Specification: The prompt does not clearly specify how to handle multiple entries matching the same treasure coordinate with identical distances or how to manage multiple entries potentially mapping to multiple treasures equally. This ambiguity could lead to different interpretations and implementations, affecting the consistency and comparability of solutions.

