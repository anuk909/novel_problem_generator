# Task ID: hard/10

## Prompt

```python
def ascii_art_symmetry(art):
    """
    Given a list of strings representing an ASCII art (where each string is a line of the art), determine if this art is horizontally symmetric, vertically symmetric, or both.

    Example 1: For the art represented by ['****', '*  *', '****'], the function should return 'Both' because it is symmetric both horizontally and vertically.

    Example 2: For the art represented by ['****', '*  *', '*  *', '****'], the function should return 'Vertical' because it is only symmetric vertically.

    Example 3: For the art represented by ['****', '****', '****', '****'], the function should return 'Horizontal' because it is only symmetric horizontally since all lines are the same.

    Example 4: For the art represented by ['****', '*  *', '*** '], the function should return 'Neither' because it is neither horizontally nor vertically symmetric.
    """

```

## Canonical Solution

```python
    def is_horizontal_symmetric(art):
        return all(line == line[::-1] for line in art)

    def is_vertical_symmetric(art):
        return art == art[::-1]

    horizontal_symmetric = is_horizontal_symmetric(art)
    vertical_symmetric = is_vertical_symmetric(art)

    if horizontal_symmetric and vertical_symmetric:
        return 'Both'
    elif horizontal_symmetric:
        return 'Horizontal'
    elif vertical_symmetric:
        return 'Vertical'
    else:
        return 'Neither'
```

## Test Cases

```python
def check(candidate):
    assert candidate(['****', '*  *', '****']) == 'Both'
    assert candidate(['****', '*  *', '*  *', '****']) == 'Vertical'
    assert candidate(['****', '****', '****', '****']) == 'Horizontal'
    assert candidate(['****', '*  *', '*** ']) == 'Neither'
    assert candidate(['****', '* *', '****']) == 'Neither'
    assert candidate(['    ', '    ', '    ', '    ']) == 'Both'
    assert candidate(['*  *', ' * *', '*  *']) == 'Both'
    assert candidate(['* * ', ' ** ', '* * ']) == 'Horizontal'
```

## Entry Point

`ascii_art_symmetry`

## Extra Info

## Cleaned Prompt

```python
Given a list of strings representing an ASCII art, determine its symmetry type: 'Both' (horizontally and vertically symmetric), 'Horizontal', 'Vertical', or 'Neither'.
Examples:
['****', '*  *', '****'] -> 'Both'
['****', '*  *', '*  *', '****'] -> 'Vertical'
['****', '****', '****', '****'] -> 'Horizontal'
['****', '*  *', '*** '] -> 'Neither'
```

## Warnings

- Solution failed correctness check. reason: failed: 
- 5, Inconsistent definitions: The explanation and examples provided give contradictory definitions of horizontal and vertical symmetry. For instance, the example of ['****', '****', '****', '****'] is deemed 'Horizontal', but based on the given functions, it should also be 'Vertical', as all lines are identical when reflected or reversed. This inconsistency makes the prompt problematic for accurately assessing solutions.
- 5, Unclear prompt language: The definitions of "horizontally symmetric" and "vertically symmetric" are not clear from the prompt alone without reviewing the solution. This lack of clarity can lead to confusion about what constitutes horizontal versus vertical symmetry, especially for participants who might interpret these terms differently.
- 4, Incorrect example outputs: The example ['* * ', ' ** ', '* * '] provided in the tests is said to be 'Horizontal' symmetric, however, this is incorrect as none of the lines are symmetric when reversed, nor does the ASCII art look symmetric horizontally. This example can mislead participants about the expected behavior.

