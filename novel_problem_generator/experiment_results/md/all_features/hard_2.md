# Task ID: hard/2

## Prompt

```python
def enchanted_invisibility_cloak(serial_codes):
    """
    In an enchanted marketplace, invisibility cloaks are encoded with magical serial codes. Each serial code is a string made up of lowercase English letters. The enchantment's power is determined by the ability to partition the serial code into the smallest possible number of palindromic substrings.

    A palindromic substring is a sequence of characters which reads the same backward as forward.

    Write a function `enchanted_invisibility_cloak` that takes a list of serial codes and returns a list where each element corresponds to the minimal number of palindromic substrings the respective serial code can be partitioned into.

    Example:
    If the input is ['abc', 'aabb', 'racecar', 'madam'], the output should be [3, 2, 1, 1].
    - 'abc' can be partitioned as ['a', 'b', 'c'] (3 parts)
    - 'aabb' can be parted as ['aa', 'bb'] (2 parts)
    - 'racecar' is already a palindrome (1 part)
    - 'madam' is already a palindrome (1 part)

    Notes:
    - Assume all input strings are non-empty and consist only of lowercase English characters.
    """
    # Implementation here
```

## Canonical Solution

```python
def enchanted_invisibility_cloak(serial_codes):
    def is_palindrome(s):
        return s == s[::-1]

    def min_partitions(string):
        n = len(string)
        if is_palindrome(string):
            return 1
        # Create a DP array
        dp = [0] * (n + 1)
        # Base case
        dp[0] = 0

        for i in range(1, n + 1):
            min_cut = float('inf')

            for j in range(1, i + 1):
                if is_palindrome(string[i-j:i]):
                    min_cut = min(min_cut, dp[i-j] + 1)

            dp[i] = min_cut

        return dp[n]
    return [min_partitions(code) for code in serial_codes]
```

## Test Cases

```python
def check(candidate):
    assert candidate(['abc']) == [3]
    assert candidate(['aabb', 'racecar']) == [2, 1]
    assert candidate(['madam', 'noon', 'xyz']) == [1, 1, 3]
    assert candidate(['level', 'civic', 'deified']) == [1, 1, 1]
    assert candidate(['ab', 'aa', 'aba']) == [2, 1, 1]
```

## Entry Point

`enchanted_invisibility_cloak`

## Extra Info

## Topics

['Palindrome Partitioning']

## Cover Story

['invisibility cloak', 'enchanted marketplace']

## Cleaned Prompt

```python
def enchanted_invisibility_cloak(serial_codes):
    """
    Takes a list of serial codes and returns a list of the minimal number of palindromic substrings each code can be partitioned into.

    A palindromic substring is a sequence of characters which reads the same backward as forward.

    Examples:
    - Input: ['abc'], Output: [3]
    - Input: ['aabb', 'racecar'], Output: [2, 1]
    - Input: ['madam', 'noon', 'xyz'], Output: [1, 1, 3]

    Assume all strings only contain lowercase letters and are non-empty.
    """
```

## Warnings

- 5, Ambiguity in Solution Example: The problem ambiguously describes the expected output format for the partition process, focusing mainly on the number of partitions required for palindromic substrings without explicit rules or guidelines on how substrings are chosen in serial codes with multiple valid partitions. This could lead to multiple valid outputs based on differing interpretations, affecting grading and validation systems.

