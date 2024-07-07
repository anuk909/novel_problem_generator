# Task ID: hard/6

## Prompt

```python
def find_treasure_path(dna_sequences, paths):
    """
    In a mythical world filled with mountains and an enchanted forest, treasure is hidden and protected by the unique sequence of Runic DNA that governs the growth of the forest.
    Each mountain pass has a unique DNA sequence stamped into its stone. The treasure can only be reached if one can find a mountain pass whose DNA sequence is a subsequence of the Enchanted Forest's DNA.

    You are given a list of DNA sequences from various mountain passes (`paths`) and the DNA of the enchanted forest (`dna_sequences`), a string.
    Write a function that takes the DNA of the enchanted forest and a list of DNA sequences from the mountain passes.
    The function should return the index of the mountain pass DNA in the list that is a subsequence of the Enchanted Forest's DNA, if such a pass exists, or -1 if no such path can be found.

    A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.

    Example:
    find_treasure_path('ACGTACGTACGT', ['CGT', 'GTAG', 'TAC']) should return 2 because 'TAC' is a subsequence of 'ACGTACGTACGT' while none of the others are.
    find_treasure_path('GATTACA', ['TAG', 'GGG', 'ACA']) should return 2 because 'ACA' is a subsequence of 'GATTACA'.
    find_treasure_path('', ['TAG', 'GGG', 'ACA']) should return -1 for an empty 'dna_sequences'.
    find_treasure_path('GATTACA', []) should return -1 when 'paths' list is empty.
    find_treasure_path('AAAA', ['AAAA', 'AAAA']) should return 0 when all characters in 'paths' are the same as 'dna_sequences'.

    Note:
    The given 'dna_sequences' and the 'paths' are all in uppercase and contain only the characters 'A', 'C', 'G', and 'T'.
    """

```

## Canonical Solution

```python
    def is_subsequence(dna, subseq):
        it = iter(dna)
        return all(c in it for c in subseq)
    for index, path in enumerate(paths):
        if is_subsequence(dna_sequences, path):
            return index
    return -1
```

## Test Cases

```python
def check(candidate):
    assert candidate('ACGTACGTACGT', ['CGT', 'GTAG', 'TAC']) == 2
    assert candidate('GATTACA', ['TAG', 'GGG', 'ACA']) == 2
    assert candidate('AGGTCCAGTACG', ['TTA', 'AGGTCC', 'CAGT']) == 1
    assert candidate('CCCCCCCC', ['AA', 'CC', 'TT']) == 1
    assert candidate('AAAA', ['A', 'AA', 'AAA', 'AAAA', 'AAAAA']) == 3
    assert candidate('TGGATCCGA', ['GGG', 'ATC', 'GGAT']) == 2
    assert candidate('', ['TAG', 'GGG', 'ACA']) == -1
    assert candidate('GATTACA', []) == -1
    assert candidate('AAAA', ['AAAA', 'AAAA']) == 0
```

## Entry Point

`find_treasure_path`

## Extra Info

## Field

['Bioinformatics']

## Cover Story

['mountains', 'enchanted forest']

## Cleaned Prompt

```python
Write a function `find_treasure_path(dna_sequences, paths)` where `dna_sequences` is a string representing the DNA of the enchanted forest and `paths` is a list of strings representing DNA sequences from various mountain passes.
The function should return the index of the mountain path whose DNA sequence is a subsequence of the enchanted forest's DNA; if no such sequence exists, return -1.
Examples:
find_treasure_path('ACGTACGTACGT', ['CGT', 'GTAG', 'TAC']) should return 2.
find_treasure_path('GATTACA', ['TAG', 'GGG', 'ACA']) should return 2.
```

## Warnings

- Solution failed correctness check. reason: failed: 
- 5, Ambiguous_parameter_ordering: The problem description ambiguously describes that the function takes "the DNA of the enchanted forest and a list of DNA sequences from the mountain passes," without explicitly stating the order of these parameters. It needs to clearly specify the sequence in which parameters should be passed to the function.
- 4, Potential_edge_case_omission: The problem's examples and explanations do not adequately cover or clarify behavior when 'dna_sequences' contains repeating patterns or overlapping potential matches within 'paths'. This could lead to uncertainties in expected function behavior during implementation.

