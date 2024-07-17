# Task ID: hard/8

## Prompt

```python
def longest_balanced_altitude(nums):
    """
    Imagine you are on a unique adventure where you are cycling across a range of altitudes represented by a list of integers, and occasionally, you also get the opportunity to float in a hot air balloon. This represents times when the altitude values stay constant for a while before you start biking again.

    Your goal during this adventure is to find the longest continuous subarray where the sum of the integers (altitude changes) is exactly zero, indicating periods where you floated in level flight without ascending or descending.

    You should use Manacher's Algorithm, an efficient method typically used for finding the longest palindromic substring, in a novel way to solve this problem.

    Examples:
    - longest_balanced_altitude([0, 0, 0, 0, 0]) should return 5 as the altitude never changed.
    - longest_balanced_altitude([3, -3, 2, -2, 0]) should return 2, with the longest balanced segment being from indices 0 to 1 or 2 to 3.
    - longest_balanced_altitude([1, -1, 1, -1, 1]) should return 4 (either indices 0 to 3 or 1 to 4).

    Note:
    - All integers in the input list represent altitude changes, and the goal is to identify the longest segment where the change cancels out to zero.
    - If no such segment exists, the function should return 0.
    - If the entire list results in a total change of zero, return the length of the list.
    """

```

## Canonical Solution

```python
    def compute_prefix_sums(nums):
        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)
        return prefix_sums

    def longest_balanced_altitude(nums):
        prefix_sums = compute_prefix_sums(nums)
        indices = {}
        longest = 0
        for i, prefix_sum in enumerate(prefix_sums):
            if prefix_sum in indices:
                longest = max(longest, i - indices[prefix_sum])
            else:
                indices[prefix_sum] = i
        return longest

```

## Test Cases

```python
def check(candidate):
    assert candidate([0, 0, 0, 0, 0]) == 5
    assert candidate([3, -3, 2, -2, 0]) == 2
    assert candidate([1, -1, 1, -1, 1]) == 4
    assert candidate([1, 1, 1, -1, -1]) == 0
    assert candidate([-5, 5, -3, 3, 2, -2, 1, -1, 0]) == 9
    assert candidate([]) == 0
    assert candidate([-2, 2, -3, 3, 4, -4, 5, -5, 6, -6]) == 10
    assert candidate([100, -100, 1, -1, 2, -2, 3, -3, 4, -4]) == 10

```

## Entry Point

`longest_balanced_altitude`

## Extra Info

## Topics

['Number Theory', "Manacher's Algorithm"]

## Field

['Quantum Computing']

## Cover Story

['bicycle', 'hot air balloon']

## Cleaned Prompt

```python
def longest_balanced_altitude(nums):
    """
    Finds the longest continuous subarray with a sum of zero in a list representing altitude changes.
    Use Manacher's Algorithm to facilitate this.

    For example:
    - If the input is [0, 0, 0, 0, 0], the output should be 5.
    - If the input is [3, -3, 2, -2, 0], the output should be 2.
    - If the input is [1, -1, 1, -1, 1], the output should be 4.
    """

```

## Warnings

- Solution failed correctness check. reason: failed: 
- 5, Algorithm Misuse: The problem prompt suggests the use of Manacher's Algorithm, which is specifically designed for finding the longest palindromic substring in a string, not for finding the longest subarray with a sum of zero in an array of integers. This misalignment in the application of the algorithm could lead to confusion and might not yield the correct solution for the problem described.
- 4, Unrelated Topics: The problem tags include "Quantum Computing", which bears no relevance to the problem as described. This could mislead participants about the knowledge or techniques expected to solve the problem, leading to unnecessary confusion.

