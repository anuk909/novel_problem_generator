# Task ID: hard/2

## Prompt

```python
def assign_superpower(blocks):
    """
    Imagine a world populated by superheroes and sentient rocks. In this world, a blockchain-like system exists where each block represents a sentient rock and its attributes. Superheroes are assigned to protect the sentient rocks based on the attributes stored in these blocks.

    Each block in the blockchain is a dictionary that includes the following keys:
    - id: a unique identifier for the block
    - timestamp: a timestamp when the block was created
    - data: a dictionary that includes attributes of the sentient rock
    - previous_hash: a string representing the hash of the previous block

    You are given a list of such blocks. The blockchain system needs a function that, based on the attributes of each sentient rock, assigns a specific superpower to protect it. Superpowers are assigned as follows:
    - If 'size' is greater than 100, 'strength' superpower is assigned.
    - If 'intelligence' level is higher than 70, 'mind-control' superpower is assigned.
    - If 'age' is less than 10 years, 'speed' superpower is assigned.

    If a sentient rock qualifies for multiple criteria, all applicable superpowers are assigned in a list.

    Your task is to write a function that accepts a list of blocks and returns a dictionary mapping each block's id to a list of assigned superpowers. Return an empty list for blocks where no criteria matches.

    Example input: 
    [{'id': 'rock1', 'timestamp': '2021-09-11T10:09:08Z', 'data': {'size': 50, 'intelligence': 80, 'age': 5}, 'previous_hash': 'xxx'},
     {'id': 'rock2', 'timestamp': '2022-01-01T00:00:00Z', 'data': {'size': 150, 'intelligence': 60, 'age': 20}, 'previous_hash': 'yyy'}]

    Example output: 
    {'rock1': ['mind-control', 'speed'], 'rock2': ['strength']}
    """

```

## Canonical Solution

```python
    def assign_superpower(blocks):
        result = {}
        for block in blocks:
            powers = []
            data = block['data']
            if data['size'] > 100:
                powers.append('strength')
            if data['intelligence'] > 70:
                powers.append('mind-control')
            if data['age'] < 10:
                powers.append('speed')
            result[block['id']] = powers
        return result

```

## Test Cases

```python
def check(candidate):
    blocks = [
        {'id': 'rock1', 'timestamp': '2021-09-11T10:09:08Z', 'data': {'size': 50, 'intelligence': 80, 'age': 5}, 'previous_hash': 'xxx'},
        {'id': 'rock2', 'timestamp': '2022-01-01T00:00:00Z', 'data': {'size': 150, 'intelligence': 60, 'age': 20}, 'previous_hash': 'yyy'},
        {'id': 'rock3', 'timestamp': '2023-03-15T15:15:15Z', 'data': {'size': 120, 'intelligence': 90, 'age': 9}, 'previous_hash': 'zzz'},
        {'id': 'rock4', 'timestamp': '2024-04-20T20:20:20Z', 'data': {'size': 90, 'intelligence': 50, 'age': 11}, 'previous_hash': 'aaa'},
        {'id': 'rock5', 'timestamp': '2025-05-30T30:30:30Z', 'data': {'size': 40, 'intelligence': 60, 'age': 30}, 'previous_hash': 'bbb'}
    ]
    expected = {
        'rock1': ['mind-control', 'speed'],
        'rock2': ['strength'],
        'rock3': ['strength', 'mind-control', 'speed'],
        'rock4': [],
        'rock5': []
    }
    assert candidate(blocks) == expected

    empty_blocks = []
    assert candidate(empty_blocks) == {}

```

## Entry Point

`assign_superpower`

## Extra Info

## Topics

['data structures', 'blockchain fundamentals', 'logical decision making']

## Field

['Blockchain Technology']

## Cover Story

['superheroes', 'sentient rocks', 'blockchain']

## Cleaned Prompt

```python
def assign_superpower(blocks):
    """
    The function assigns superpowers based on attributes like 'size', 'intelligence', and 'age'.
    - 'strength' for size > 100.
    - 'mind-control' for intelligence > 70.
    - 'speed' for age < 10.

    It returns a dictionary mapping block ids to a list of applicable superpowers, or an empty list if no criteria are met.

    Example input: 
    [{'id': 'rock1', 'timestamp': '2021-09-11T10:09:08Z', 'data': {'size': 50, 'intelligence': 80, 'age': 5}, 'previous_hash': 'xxx'}, {'id': 'rock2', 'timestamp': '2022-01-01T00:00:00Z', 'data': {'size': 150, 'intelligence': 60, 'age': 20}, 'previous_hash': 'yyy'}]

    Example output: 
    {'rock1': ['mind-control', 'speed'], 'rock2': ['strength']}
    """

```

## Warnings

- Only 2 test cases found. Minimum recommended is 5.
- Solution failed correctness check. reason: failed: 
- 5, Unrealistic Timestamp: The problem provides a timestamp '2025-05-30T30:30:30Z' for a 'block' which contains an invalid time format as there is no 30th hour or a 30th minute beyond the normal bounds of time representation.
- 5, Test Case Error: The test case in the provided `check` function assumes a date string format that includes an invalid date and time such as '2025-05-30T30:30:30Z'. This incorrect timestamp could potentially lead to errors or exceptions when running the test if the system attempts to parse it as a real datetime.

