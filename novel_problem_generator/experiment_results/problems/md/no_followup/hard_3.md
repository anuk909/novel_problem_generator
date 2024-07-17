# Task ID: hard/3

## Prompt

```python
def lost_documents_recovery(skip_list, pattern):
    """
    Imagine you are in a digital courtroom trying to recover documents from a disappeared civilization known as the lost city. The documents are partially recovered and stored in a Skip List, which dramatically speeds up the search process. Your task is to find specific patterns within these documents to present as evidence.

    The lost documents are represented as a series of words, and you are given specific search terms. Using an efficient search algorithm (Knuth-Morris-Pratt (KMP)) embedded within operations of the Skip List, identify and return how often a given pattern appears within the Skip List's data structure.

    For example:
    If the skip list contains ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'] and the pattern is 'the', the result should be 2.

    Note:
    - Assume the skip list's words are all lowercase and the search pattern is also provided in lowercase.
    - The list could contain any sequence of words but no punctuation, numbers, or special characters.
    """

```

## Canonical Solution

```python
    def kmp_search(text, pattern):
        n, m = len(text), len(pattern)
        if m == 0:
            return 0
        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length-1]
                else:
                    lps[i] = 0
                    i += 1
        i = j = count = 0
        while i < n:
            if pattern[j] == text[i]:
                i += 1
                j += 1
            if j == m:
                count += 1
                j = lps[j-1]
            elif i < n and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        return count

    count = 0
    for word in skip_list:
        count += kmp_search(word, pattern)
    return count
```

## Test Cases

```python
def check(candidate):
    assert candidate(['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'], 'the') == 2
    assert candidate(['lost', 'city', 'documents', 'are', 'lost', 'amidst', 'the', 'sands'], 'lost') == 2
    assert candidate(['seek', 'and', 'you', 'shall', 'find'], 'hidden') == 0
    assert candidate(['echoes', 'of', 'the', 'lost', 'city', 'the', 'lost', 'civilization'], 'the') == 3
    assert candidate(['one', 'last', 'hope', 'to', 'recover', 'the', 'lost', 'documents'], 'lost') == 1
```

## Entry Point

`lost_documents_recovery`

## Extra Info

## Topics

['Skip List', 'Knuth-Morris-Pratt (KMP) Algorithm']

## Field

['Machine Learning']

## Cover Story

['courtroom', 'lost city']

## Cleaned Prompt

```python
Write a function `lost_documents_recovery(skip_list, pattern)` that counts the occurrences of a pattern within a list of words (Skip List). Use the Knuth-Morris-Pratt algorithm to efficiently find the number of times the pattern appears in each word of the list. Examples:

- Input: ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'], pattern: 'the'. Output: 2.
- Input: ['lost', 'city', 'documents', 'are', 'lost', 'amidst', 'the', 'sands'], pattern: 'lost'. Output: 2.
```

## Warnings

- Solution failed correctness check. reason: failed: 
- 5, Misleading Problem Description: The use of 'Skip List' in the problem description is misleading because the function provided actually operates on a standard list of words, not on a self-adjusting data structure like a Skip List, which is designed to allow fast access, insertion, and deletion.
- 4, Inappropriate Algorithm Context: The Canonical solution has an underlying inefficiency because it applies the KMP searching algorithm to each individual word instead of to the whole sequence as a single searchable text. This contradicts the conventional application of KMP, which is typically meant for longer strings, where pattern occurrences could span across several combined elements.

