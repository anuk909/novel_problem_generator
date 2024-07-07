# Task ID: hard/7

## Prompt

```python
def optimal_gem_distribution(gemstones, reviewers):
    """
    Imagine you are a consultant for a high-end gemstone mine, which has recently discovered treasures requiring unique expertise to evaluate. Each gemstone is unique in its value and rarity. Besides, there is a list of expert reviewers, each with a probability of approving a gemstone based on its characteristics.

    You need to distribute the gemstones among the reviewers such that the probability of getting all gemstones approved is maximized, even if the numbers of gemstones and reviewers are different.

    The gemstones are represented as a list of tuples (value, rarity) where value is an integer and rarity is a float.
    The reviewers are represented as a list of functions, where each function takes a gemstone tuple and returns the probability (0 <= p <= 1) of that reviewer approving the gemstone.

    The function should return a distribution list where each element is a tuple (reviewer_index, gemstone_index) indicating that the gemstone at gemstone_index is assigned to the reviewer at reviewer_index to maximize the overall probability of approval. If there are more gemstones than reviewers, each reviewer can review more than one gemstone; if there are more reviewers than gemstones, some reviewers may not receive a gemstone.

    Example:
    gemstones = [(10, 0.2), (20, 0.5), (30, 0.3)]
    reviewers = [
        lambda g: 0.9 if g[1] < 0.3 else 0.2,
        lambda g: 0.7 if g[0] > 15 else 0.1
    ]
    The output should be [(0, 0), (1, 1), (0, 2)] as it maximizes the overall probability of approval.

    Note:
    - Be sure to handle the cases where the number of gemstones and reviewers are different.
    """
```

## Canonical Solution

```python
    from itertools import permutations
    import numpy as np
    def total_probability(distribution):
        product = 1
        for reviewer_idx, gemstone_idx in distribution:
            product *= reviewers[reviewer_idx](gemstones[gemstone_idx])
        return product

    max_probability = 0
    optimal_distribution = []
    for perm in permutations(range(len(reviewers)), len(gemstones)):
        distribution = list(zip(range(len(reviewers)), np.random.permutation(perm)))
        current_probability = total_probability(distribution)
        if current_probability > max_probability:
            max_probability = current_probability
            optimal_distribution = distribution

    return optimal_distribution
```

## Test Cases

```python
def check(candidate):
    gemstones1 = [(10, 0.2), (20, 0.5), (30, 0.3)]
    reviewers1 = [
        lambda g: 0.9 if g[1] < 0.3 else 0.2,
        lambda g: 0.7 if g[0] > 15 else 0.1
    ]
    assert set(candidate(gemstones1, reviewers1)) == set([(0, 0), (1, 1), (0, 2)])

    gemstones2 = [(5, 0.5), (15, 0.1), (25, 0.4), (35, 0.2)]
    reviewers2 = [
        lambda g: 0.8 if g[1] < 0.25 else 0.3,
        lambda g: 0.6 if g[0] < 20 else 0.2
    ]
    assert set(candidate(gemstones2, reviewers2)) == set([(0, 1), (0, 3), (1, 0), (1, 2)])

    gemstones3 = [(12, 0.15), (22, 0.55)]
    reviewers3 = [
        lambda g: 0.85 if g[1] < 0.5 else 0.15,
        lambda g: 0.65 if g[0] > 20 else 0.05
    ]
    assert set(candidate(gemstones3, reviewers3)) == set([(0, 0), (1, 1)])

    gemstones4 = [(10, 0.1)]
    reviewers4 = [lambda g: 0.8 if g[1] < 0.2 else 0.1, lambda g: 0.9 if g[1] < 0.2 else 0.2]
    assert set(candidate(gemstones4, reviewers4)) == set([(1, 0)])

    gemstones5 = [(10, 0.1), (15, 0.2), (20, 0.3)]
    reviewers5 = [lambda g: 0.9 if g[1] < 0.3 else 0.1]
    assert set(candidate(gemstones5, reviewers5)) == set([(0, 0), (0, 1), (0, 2)])
```

## Entry Point

`optimal_gem_distribution`

## Extra Info

## Topics

['Probability and Statistics', 'Jarvis March']

## Cover Story

['gemstone mine', 'restaurant']

## Cleaned Prompt

```python
Write a function that takes a list of gemstone tuples (value, rarity) and a list of reviewer functions. Each reviewer function takes a gemstone tuple and returns the probability of approving the gemstone. The function should return a list of tuples (reviewer_index, gemstone_index) to maximize the probability of all gemstones getting approved. - Gemstones are represented as (value, rarity) tuples. - Reviewers are functions returning probabilities based on gemstone characteristics. - Handle different counts of gemstones and reviewers. Each reviewer can handle multiple gemstones or may not receive any, depending on the counts.
```

## Warnings

- Solution failed correctness check. reason: failed: invalid syntax (<string>, line 22)
- 4, Ambiguity in Problem Statement: The problem statement is unclear about the expected behaviour or method of 'maximizing the overall probability of approval' when the distribution possibilities of gemstones to reviewers can significantly vary. This results in an exponential number of combinations to evaluate, which may not be tractable for a larger set of gemstones and reviewers.
- 5, Unsolvable Complexity: No feasible solution is provided to handle combinations efficiently when the number of gemstones and reviewers differ. The combinations’ factor increases non-linearly, making brute-force or permutation-based approaches impractical for larger inputs. The solution attempts to utilize permutations, but it falls short of efficiently handling complex cases and large inputs.
- 5, Inequity in Assignment Distribution Strategy: The problem does not specify how to ensure fairness or a technically sound distribution when there are more reviewers than gemstones or vice versa. Without such guidance or constraints, solutions might be overly simplified or unfairly distribute workloads, leading to suboptimal or misunderstood implementation efforts.

