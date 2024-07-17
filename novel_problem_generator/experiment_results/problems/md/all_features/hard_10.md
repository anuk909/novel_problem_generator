# Task ID: hard/10

## Prompt

```python
def manage_documents(documents):
    """
    In a document management system, there are documents with unique identification and revision versions. Your task is to manage these documents effectively using AVL Tree and to find the longest palindromic sequence of document IDs after all insertions are complete.

    Each document is represented by a tuple (document_id, revision).
    The function should:
    - Insert new documents into the AVL Tree.
    - Delete documents from the AVL Tree when a revision supersedes the previous ones.
    - Return the length of the longest palindromic sequence of the document IDs in the AVL Tree.

    Input:
    - documents: A list of tuples. Each tuple represents a document as (document_id, revision).

    Output:
    - Return the length of the longest palindromic sequence of document IDs.

    Example:
    For documents = [(1, 1), (2, 1), (3, 1), (2, 2), (1, 2), (3, 2)], the longest palindromic sequence of IDs would be [1, 2, 3, 2, 1] which has a length of 5.
    """

```

## Canonical Solution

```python
    class AVLNode:
        def __init__(self, key):
            self.left = None
            self.right = None
            self.height = 1
            self.key = key
        def update_height(self):
            self.height = max((self.left.height if self.left else 0), (self.right.height if self.right else 0)) + 1

    class AVLTree:
        def __init__(self):
            self.root = None
        def insert(self, key):
            # Custom insert which handles revisions
        def delete(self, key):
            # Custom delete which handles revisions

        def find_longest_palindromic_sequence(self):
            # Convert tree keys to a list, sequence of document IDs
            # Apply Manacher's algorithm to find longest palindrome

    // Usage
    avl_tree = AVLTree()
    for document_id, revision in documents:
        avl_tree.insert(document_id, revision)
    return avl_tree.find_longest_palindromic_sequence()
```

## Test Cases

```python
def check(candidate):
    assert candidate([(1, 1), (2, 1), (3, 1), (2, 2), (1, 2), (3, 2)]) == 5
    assert candidate([(4, 1), (5, 1), (6, 1)]) == 1
    assert candidate([]) == 0
    assert candidate([(10, 1), (10, 2), (10, 3), (10, 4)]) == 1
    assert candidate([(7, 1), (8, 1), (8, 2), (7, 2), (9, 1)]) == 5
```

## Entry Point

`manage_documents`

## Extra Info

## Topics

['AVL Tree', "Manacher's Algorithm", 'Data Structures']

## Field

['Software Engineering']

## Cover Story

['document management system', 'revision management']

## Cleaned Prompt

```python
Write a function to manage documents using an AVL Tree for insertion and deletion. After inserting all documents, compute the longest palindromic sequence of document IDs using an efficient algorithm.

Input: List of tuples (document_id, revision). Output: Length of longest palindromic sequence of document IDs.

Example: For documents = [(1, 1), (2, 1), (3, 1), (2, 2), (1, 2), (3, 2)], the longest sequence would be [1, 2, 3, 2, 1] with length 5.
```

## Warnings

- Solution failed correctness check. reason: failed: expected an indented block (<string>, line 34)
- 5, Ambiguity in Problem Requirements: The problem prompt and example suggest handling both document numbers and revision numbers, but the details and method for handling revisions operationally (e.g., version control, how they affect the tree structure, order, etc.) are not specified. This lack of clarity can lead to multiple interpretations and implementations, which is problematic for ensuring consistent solutions among participants.
- 4, Misuse of Data Structures: The use of an AVL Tree to track document numbers and then extracting these numbers to find the longest palindromic sequence using Manacher's algorithm seems inefficient and inappropriate. AVL Trees are meant for fast lookups, insertions, and deletions, not for operations on sequential data like finding palindromes, which could be more directly and efficiently handled using other data structures or methods specifically suited for sequence analysis.
- 4, Incomplete Solution Template: The canonical solution provided lacks complete implementation details (e.g., the AVLTree _insert, _delete methods and Manacher's algorithm implementation are omitted), which can confuse participants about the expected level of detail and specific AVL and algorithmic knowledge required.

