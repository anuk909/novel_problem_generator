# Task ID: hard/8

## Prompt

```python
def rocket_optimal_launch_schedule(intervals):
    """
    Manage a streamlined rocket launch scheduling by determining the most efficient times to launch rockets. This means finding the maximum number of rockets that can be launched within their scheduled intervals without any overlap.

    Each rocket's available launch window is defined by an interval [start, end), where 'start' is the inclusive starting time, and 'end' is the exclusive ending time. No two rockets can launch if their designated intervals overlap.

    Given a list of intervals (each representing a rocket's launch window), your task is to compute the maximum number of rockets you can launch such that their intervals do not overlap.

    Example:
    Input: intervals = [[1,3], [2,4], [3,5]]
    Output: 2
    Explanation: Schedules for launching rockets in intervals [1,3] and [3,5] can be arranged without overlapping, however [1,3] and [2,4] do overlap.

    Another example:
    Input: intervals = [[6,8], [9,10], [1,3]]
    Output: 3
    Explanation: All intervals are non-overlapping, enabling the launch of all rockets within their designated windows.
    """

```

## Canonical Solution

```python
    intervals.sort(key=lambda x: x[1])
    count = 0
    last_end = -1
    for start, end in intervals:
        if start >= last_end:
            count += 1
            last_end = end
    return count
```

## Test Cases

```python
def check(candidate):
    assert candidate([[1, 3], [2, 4], [3, 5]]) == 2
    assert candidate([[6, 8], [9, 10], [1, 3]]) == 3
    assert candidate([[7, 8], [8, 9], [9, 10], [6, 7]]) == 4
    assert candidate([[5, 10], [10, 15]]) == 2
    assert candidate([]) == 0
    assert candidate([[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 10
```

## Entry Point

`rocket_optimal_launch_schedule`

## Extra Info

## Topics

['Greedy Algorithms', 'Interval Scheduling']

## Field

Operations Research

## Cover Story

['rocket']

## Cleaned Prompt

```python
Write a function that determines the maximum number of non-overlapping intervals from a list of intervals. Each interval [start, end) represents a launch window for a rocket, where 'start' is inclusive and 'end' is exclusive. Return the maximum number of non-overlapping intervals. 

Example:
Input: [[1,3], [2,4], [3,5]]
Output: 2
```

## Warnings

- 5, Canonical Solution Incorrect Handling of Input Edge Cases: The canonical solution provided does not handle cases where the list of intervals may contain tuples of non-integer values, intervals that are not properly formatted (e.g., if an interval does not contain two elements), or intervals where the 'start' time is after the 'end' time, which could lead to unexpected behavior or runtime errors. Such issues should be covered in a robust solution or at least noted in the problem statement to ensure that inputs are well-formed.
- 4, Inadequate Problem Constraints: The problem does not define the size constraints for the interval list or the range of the integers that could possibly be an element of the intervals. Without these constraints, it's challenging to gauge the efficiency requirements of the solution and to understand what kind of edge cases need consideration (e.g., extremely large numbers, very large lists).

