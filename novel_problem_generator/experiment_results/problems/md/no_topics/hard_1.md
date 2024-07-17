# Task ID: hard/1

## Prompt

```python
def analyze_artifacts(artifact_signals):
    """
    Imagine you are at an archaeological dig site and have discovered a number of ancient artifacts. Each artifact emits a unique signal pattern that can be detected by your IoT devices deployed around the site. Your goal is to analyze these signal patterns to determine which of them might indicate the presence of a portal to an ancient civilization.

    Each signal pattern is represented as a list of integers, where each integer represents the strength of the signal detected at a certain time. A portal signal is defined by the following criteria:
    1. The signal strength must strictly alternate between increasing and decreasing over any eight consecutive measurements.
    2. The sum of all measurements in the signal pattern must be a prime number.

    Write a function that takes a list of signal patterns (where each signal pattern is a list of integers) and returns the number of signal patterns that match the criteria for a 'portal' signal. Only patterns with eight measurements or more can be considered as potential portal signals.

    Example input: [[5, 10, 5, 10, 5, 10, 5, 10], [3, 6, 3, 6, 3, 6, 6], [5, 10, 15]]
    Example output: 1 # Because the first pattern matches all criteria for a portal signal
    """

```

## Canonical Solution

```python
    from math import isqrt
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_alternating(sequence):
        if len(sequence) < 8:
            return False
        for i in range(len(sequence) - 7):
            if not all((sequence[j] < sequence[j+1] > sequence[j+2] < sequence[j+3]) for j in range(i, i+7, 3)):
                return False
        return True

    count = 0
    for pattern in artifact_signals:
        if len(pattern) >= 8 and sum(pattern) and is_prime(sum(pattern)) and is_alternating(pattern):
            count += 1
    return count
```

## Test Cases

```python
def check(candidate):
    assert candidate([[5, 10, 5, 10, 5, 10, 5, 10], [3, 6, 3, 6, 3, 6, 6], [5, 10, 15]]) == 1
    assert candidate([[2, 3], [4, 5, 4, 5, 4, 5, 4, 5], [1, 2, 1, 2, 1, 2, 1], [3, 1, 3, 1, 3, 1]]) == 0
    assert candidate([[10, 20, 10, 20, 10, 20, 10, 20], [1, 2, 3, 4, 5, 6, 7, 8], [5, 10, 5, 10, 5, 10, 5]]) == 1
    assert candidate([]) == 0
    assert candidate([[3, 2, 3, 2, 3, 2, 3, 2], [3, 2, 3, 2, 3, 2, 3], [7, 14, 7, 14, 7, 14, 7, 12], [7, 14, 7, 14, 7, 14, 11, 14]]) == 2
```

## Entry Point

`analyze_artifacts`

## Extra Info

## Field

['Internet of Things (IoT)']

## Cover Story

['archaeological dig', 'portal']

## Cleaned Prompt

```python
def analyze_artifacts(artifact_signals):
    Each signal pattern is a list of integers representing signal strength over time. A portal signal alternates strictly increasing and decreasing strength over any eight consecutive measurements and the sum of all measurements is a prime number. Only consider patterns with eight measurements or more. Return the number of 'portal' signal patterns.
```

## Warnings

- Solution failed correctness check. reason: failed: 
- 5, Logical Flaw in Signal Checking: The provided method 'is_alternating' in the canonical solution checks if the signal alternates strictly between increasing and decreasing over at least eight consecutive measurements incorrectly. It assumes a fixed pattern ([j] < [j+1] > [j+2] < [j+3]) repeatedly, which is not required by the problem statement that indicates any alternating pattern over any eight consecutive measurements is valid. Consequently, this prevents valid alternating sequences that do not match this fixed pattern from being recognized, which leads to incorrect results.
- 4, Inconsistent Definition: The problem statement and the canonical solution provide different requirements regarding the sequence length for identification of a 'portal' signal. The statement mentions that "Only patterns with eight measurements or more can be considered", yet the check of 'is_alternating' is applied using a looping window without direct reference to ensure each assessment involves all measures of sequences of exactly eight only or at least eight under same conditions; it merely checks from the first position without looping over possible sequences of eight within a longer list.

