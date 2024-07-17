# Task ID: hard/9

## Prompt

```python
def magical_gallery(arr):
    """
    In an enchanted art gallery, each piece of art has a value that changes daily. The curator of the gallery wants to know if there is any combination of three art pieces whose values sum up to zero. Your task is to write a function 'magical_gallery' that takes a list of integers representing today's values of art pieces and returns a list of unique triplets [a, b, c] from the list such that a + b + c = 0. Each triplet should be sorted in non-descending order, and the result list should also be sorted accordingly.

    Example:
    Input: [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]

    Note:
    - The input list can include duplicates which may lead to duplicate triplets if not handled.
    - The result should not contain duplicate triplets.
    - If no such triplet exists, return an empty list.
    """

```

## Canonical Solution

```python
    arr.sort()
    result = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        left, right = i + 1, len(arr) - 1
        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            if sum == 0:
                result.append([arr[i], arr[left], arr[right]])
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif sum < 0:
                left += 1
            else:
                right -= 1
    return result
```

## Test Cases

```python
def check(candidate):
    assert candidate([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert candidate([0, 0, 0, 0]) == [[0, 0, 0]]
    assert candidate([3, -1, -7, 2, -4, 10]) == []
    assert candidate([34, -21, -36, 22, 14, -49, 10, 25]) == [[-21, -36, 10, 25]]
    assert candidate([1, 2, -3, 0, 5, 7, -2, -1]) == [[-3, 1, 2], [-2, -1, 3]]
```

## Entry Point

`magical_gallery`

## Extra Info

## Topics

['3-Sum Problem']

## Field

['Reinforcement Learning']

## Cover Story

['crystal ball', 'art gallery']

## Cleaned Prompt

```python
Given a list of integers representing the values for today's art pieces in a gallery, return all unique triplets where the sum of their values is zero and each triplet is sorted in non-descending order. If no such triplet exists, return an empty list. Each triplet should be unique, and the result list should be sorted.

Example:
Input: [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
```

## Warnings

- Solution failed correctness check. reason: failed: 
- 4, ambiguous_output_format: The output format specification and example do not clearly specify if the output triplets must always be sorted within each individual triplet as well as the entire list of triplets sorted among themselves. This ambiguity can lead to variations in valid outputs that could be considered incorrect if not consistently defined.
- 5, logical_error_in_example: In the provided examples within the 'test' section, some of the outputs mentioned do not correctly sum up to zero, creating a misconception or misleading guidance for anyone developing or testing similar functions as the one described. This could challenge the validity and reliability of assuming the problem statement and example outputs are correct, leading to erroneous implementations.

