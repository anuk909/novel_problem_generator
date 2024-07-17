# Task ID: hard/1

## Prompt

```python
def ghostly_sum_events(ghost_events, energy_threshold):
    """
    In an old haunted house, paranormal investigators use sensors to detect ghostly energy disturbances. Each disturbance emits an energy value, and these events come as an uninterrupted data stream. The investigators are particularly interested in discovering pairs of events whose summed energy precisely matches a given energy threshold to confirm a potent 'energy vortex'.

    Implement a function that, given a list of integers (representing energy disturbances as they are detected) and an integer (the energy threshold), determines how many pairs of disturbances sum up exactly to the given threshold. Each disturbance may only be used once, and the function should return the count of unique pairs where the order of events in a pair does not matter.

    For example:
    ghostly_sum_events([5, 3, 6, 2], 8) should return 2, with pairs (5, 3) and (6, 2) summing to 8.
    ghostly_sum_events([1, 1, 3, 5], 4) should return 1, with a qualifying pair being (1, 3).

    """

```

## Canonical Solution

```python
    def ghostly_sum_events(ghost_events, energy_threshold):
        seen = {}
        count = 0
        for e in ghost_events:
            complement = energy_threshold - e
            if complement in seen and seen[complement] > 0:
                count += 1
                seen[complement] -= 1
            else:
                if e in seen:
                    seen[e] += 1
                else:
                    seen[e] = 1
        return count
```

## Test Cases

```python
def check(candidate):
    assert candidate([5, 3, 6, 2], 8) == 2
    assert candidate([1, 1, 3, 5], 4) == 1
    assert candidate([10, 3, 5, 2], 5) == 0
    assert candidate([0, 0, 0, 0], 0) == 6
    assert candidate([100, 1, 42, -42, 100], 58) == 1
    assert candidate([4, -2, 7, -5, 11, 5, -4], 9) == 1
    assert candidate([1, 5, 1, 5], 10) == 0
    assert candidate([-7, -3, 10, 4, 2, 0, -10], 0) == 2
    assert candidate([-5, 12, 6, 3, 9, 2, 1, -8], 4) == 4
    assert candidate([15, 5, -10, -5, -15, 10], 0) == 3
```

## Entry Point

`ghostly_sum_events`

## Extra Info

## Topics

['Data Stream', 'Two-Sum Problem']

## Cover Story

['haunted house', 'energy vortex']

## Cleaned Prompt

```python
Given a list of integers representing energy disturbances in a haunted house and an integer energy threshold, count how many unique pairs of disturbances sum precisely to the energy threshold. Only count pairs where disturbances are used once. For example:
ghostly_sum_events([5, 3, 6, 2], 8) should return 2, since the pairs (5, 3) and (6, 2) both sum to 8.
```

## Warnings

- Solution failed correctness check. reason: failed: 
- 4, insufficient definition of 'unique pairs': The problem statement does not clearly explain what constitutes 'unique pairs' especially with regards to handling multiple identical pairs. This can create ambiguity if the input contains duplicate values leading to multiple identical sum pairs.
- 5, tuple order irrelevance not explicitly managed in canonical solution: The problem statement asserts that the order of pairs does not matter in counting unique pairs. However, the canonical solution does not have a mechanism to ensure that pairs such as (1, 3) and (3, 1) are counted as a single unique pair due to how dictionaries manage keys and values, potentially leading to incorrect counts when identical values are present in different orders.
- 4, handling of repeated elements: The canonical solution's mechanism to decrement the count in 'seen' dictionary for the complement is flawed for handling repeated elements appropriately in certain cases, possibly giving incorrect results. There needs to be clarification or adjustment in logic to accurately track and decrement counts of elements used in pairs.

