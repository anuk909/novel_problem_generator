# Task ID: hard/2

## Prompt

```python
def reverse_linked_list_visualizer(data_set):
    """
    Imagine you have a sequence of video frames where each frame uniquely represents a node in a singly linked list. Each node consists of a 'value' and a 'next pointer', which can be visualized as lines or arrows extending to the next node in a subsequent frame. The list starts from the first frame and ends when 'next pointers' no longer point to another node. Your goal is to produce a new sequence where the list is shown in reversed order.

    Write a function that takes a list of frames, each represented as a dictionary with 'value' and 'next_index'. The 'next_index' indicates the index of the next node, akin to a 'next pointer' in a linked list. The function should return a new list of frames showing the linked list in reversed orientation.

    - Input: data_set: List of dictionaries, where each dictionary has a 'value' and a 'next_index' (index of the next node or None for list's end).
    - Output: A list of dictionaries with the reversed linked list.

    Example:
    Input data_set is [{"value": 1, "next_index": 1}, {"value": 2, "next_index": None}].
    The function should return [{"value": 2, "next_index": 0}, {"value": 1, "next_index": None}].

    Note:
    - Empty data sets or those with a single element should be handled correctly.
    - Assumes no cyclic loops or other structural anomalies.
    """
```

## Canonical Solution

```python
	def reverse_linked_list_visualizer(data_set):
	    if not data_set:
	        return []
	    index_map = {i: node['next_index'] for i, node in enumerate(data_set) if node['next_index'] is not None}
	    index_map[None] = None
	    current_index = 0
	    for node in data_set:
	        if node['next_index'] is None:
	            current_index = data_set.index(node)
	            break
	    new_data_set = [None] * len(data_set)
	    prev_index = None
	    while current_index is not None:
	        current_node = data_set[current_index].copy()
	        current_node['next_index'] = prev_index
	        new_data_set[current_index] = current_node
	        prev_index = current_index
	        current_index = index_map[current_index] if current_index in index_map else None
	    return new_data_set
```

## Test Cases

```python
def check(candidate):
    assert candidate([]) == []
    assert candidate([{"value": 1, "next_index": None}]) == [{"value": 1, "next_index": None}]
    assert candidate([{"value": 1, "next_index": 1}, {"value": 2, "next_index": None}]) == [{"value": 2, "next_index": 0}, {"value": 1, "next_index": None}]
    assert candidate([{"value": 1, "next_index": 1}, {"value": 2, "next_index": 2}, {"value": 3, "next_index": None}]) == [{"value": 3, "next_index": 1}, {"value": 2, "next_index": 0}, {"value": 1, "next_index": None}]
    assert candidate([{"value": 3, "next_index": None}, {"value": 1, "next_index": 0}]) == [{"value": 1, "next_index": 1}, {"value": 3, "next_index": None}]
    assert candidate([{"value": 1, "next_index": 2}, {"value": 2, "next_index": None}, {"value": 3, "next_index": 1}]) == "Handle cyclic or incorrect structures appropriately"
```

## Entry Point

`reverse_linked_list_visualizer`

## Extra Info

## Topics

['Data Manipulation', 'Reverse Linked List', 'Computer Vision']

## Field

Computer Vision

## Cover Story

['Video Sequence', 'Frames', 'Nodes', 'LinkedList']

## Cleaned Prompt

```python
Write a function to reverse a visual representation of a linked list, given as a list of frames where each frame (node) includes a 'value' and a 'next_index', indicating the next node in the sequence. The function should take this list and return a new list with the linked list visually reversed.
```

## Warnings

- Solution failed correctness check. reason: failed: invalid syntax (<string>, line 17)
- 5, Ambiguous input/output structure: The prompt states that the function should return a new list of dictionaries showing the linked list in reversed order, but it doesn't clarify if the list's order itself should be reversed or just the 'next_index' pointers. This can cause confusion in interpreting the function's purpose and expected behavior.
- 4, Inconsistent data type handling: The canonical solution does not address varied input data types and does not include error checks for incorrect or unexpected data types (like non-integer 'next_index', or non-dictionary elements in the list), leading to potential runtime errors during function execution.
- 5, Lack of cyclic structure handling: The problem prompt and the canonical solution do not account for a cyclic linked list, which is mentioned in the test cases. This lack of handling can cause an infinite loop or incorrect outputs, rendering the solution incomplete and the function potentially unsafe for certain inputs.
- 5, Ignoring incorrect/irregular linked list structures: The problem statement and solution assume that the input linked list is well-formed (each 'next_index' correctly points to a valid index or None), but does not handle cases where 'next_index' might point to out-of-bounds indices or incorrect list structures. This results in the function being unreliable.

