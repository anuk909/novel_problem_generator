# Task ID: hard/8

## Prompt

```python
def find_rare_operations(expression, operations):
    """
    Given a mathematical expression as a string and a list of rare operations as strings, your task is to return a list of all the rare operations found in the expression in the order they appear.

    - The expression will only contain characters in [0-9], [a-zA-Z], and common operators (+, -, *, /).
    - Rare operations are given as subsets of characters that denote custom operations not typically found in standard arithmetic expressions.
    - The match must be exact and not a subset of a larger segment that includes numbers or letters.
    - If no rare operations are found, return an empty list.
    - Operations appearing more than once in the expression should be listed each time they appear.

    Examples:
    find_rare_operations('12abc34def55abc9x', ['abc', 'def', 'xx']) returns ['abc', 'def', 'abc']
    find_rare_operations('235+678', ['**', '^^']) returns []
    find_rare_operations('100%%%20^2###3', ['%%', '^', '###']) returns ['%%', '^', '###']
    """

```

## Canonical Solution

```python
    import re
    def find_rare_operations(expression, operations):
        pattern = '|'.join(map(re.escape, operations))
        matches = re.findall(pattern, expression)
        return matches
```

## Test Cases

```python
def check(candidate):
    assert candidate('12abc34def55abc9x', ['abc', 'def', 'xx']) == ['abc', 'def', 'abc']
    assert candidate('235+678', ['**', '^^']) == []
    assert candidate('100%%%20^2###3', ['%%', '^', '###']) == ['%%', '^', '###']
    assert candidate('88&&&87**&&', ['&&&', '**']) == ['&&&', '**']
    assert candidate('no operations here', ['!', '@', '#']) == []
    assert candidate('', ['abc', 'def']) == []
```

## Entry Point

`find_rare_operations`

## Extra Info

## Cleaned Prompt

```python
Find all rare operations from a list in the given expression string. Each instance should be returned in the order of appearance. Rare operations are exact matches outside typical numeric values and common operators. Return an empty list if none or not found.
```

## Warnings

- Solution failed correctness check. reason: failed: 
- 5, Ambiguity in Definition of Rare Operations: The problem statement does not explicitly clarify what constitutes a rare operation other than saying it is not a standard arithmetic operation. This ambiguity can lead to confusion about what characters or patterns enforce a match as a "rare operation." Clear specifications or inclusion of edge examples could help, especially when operations contain alphanumeric characters.
- 5, Unclear Matching Requirements: The prompt states that matches must be exact and not part of larger segments including numbers or letters, but the canonical solution simply uses regex findall without ensuring this condition. This misalignment between the problem description and the provided solution can result in incorrect findings where the operation is a subset of a larger alphanumeric string, which is contrary to the requirements.
- 4, Overlap and Repetition Handling: The provided solution and prompt do not address scenarios where rare operations might overlap in the expression or how to handle repeated operations particularly when they interweave (e.g., '&&&&' for '&&'). This could lead to unexpected behavior or incorrect outputs if rare operations can overlap in various complex ways.

