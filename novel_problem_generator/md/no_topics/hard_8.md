# Task ID: hard/8

## Prompt

```python
def plant_portal_classifier(species_data, test_data, k):
    """
    Imagine a fictional world where portals to various dimensions exist, which have distinct characteristics based on the flora (plants) in them. Each portal can be identified based on the plant species it contains. 

    Your task is to develop a machine learning classifier that predicts the portal based on characteristics of plants observed. For instance, a particular portal might have taller plants, another might have plants with wider leaves, etc.

    Each entry in species_data is a dictionary with the following structure:
    {
        'portal_id': int,
        'features': [float]
    }

    test_data is a list of features where each feature list needs to be classified into one of the portal ids. The value of k determines the number of nearest neighbors to consider for classification.

    Implement a k-Nearest Neighbours classifier from scratch to classify test data based on the provided training data (species_data).

    Your implementation should handle:
    - Calculation of Euclidean distance between feature vectors.
    - Determination of k-nearest vectors.
    - Majority vote mechanism for classification based on the nearest vectors' portal ids.

    Example:
    species_data = [
        {'portal_id': 1, 'features': [10, 0.5, 0.2]},
        {'portal_id': 2, 'features': [20, 0.3, 0.1]},
        {'portal_id': 1, 'features': [11, 0.4, 0.2]},
        {'portal_id': 2, 'features': [19, 0.2, 0.1]}
    ]
    test_data = [[10, 0.5, 0.3], [20, 0.3, 0.2]]
    k = 3
    Output should be: [1, 2]
    """

```

## Canonical Solution

```python
    def euclidean_distance(a, b):
        return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5

    def k_nearest(species_data, features, k):
        distances = [(euclidean_distance(entry['features'], features), entry['portal_id']) for entry in species_data]
        distances.sort()
        nearest = [portal_id for _, portal_id in distances[:k]]
        return max(set(nearest), key=nearest.count)

    result = []
    for features in test_data:
        portal_id = k_nearest(species_data, features, k)
        result.append(portal_id)
    return result
```

## Test Cases

```python
def check(candidate):
    species_data1 = [
        {'portal_id': 1, 'features': [10, 0.5, 0.2]},
        {'portal_id': 2, 'features': [20, 0.3, 0.1]},
        {'portal_id': 1, 'features': [11, 0.4, 0.2]},
        {'portal_id': 2, 'features': [19, 0.2, 0.1]}
    ]
    test_data1 = [[10, 0.5, 0.3], [20, 0.3, 0.2]]
    assert candidate(species_data1, test_data1, 3) == [1, 2]

    species_data2 = [
        {'portal_id': 1, 'features': [10, 0.5, 0.2]}
    ]
    test_data2 = [[10, 0.5, 0.2]]
    assert candidate(species_data2, test_data2, 1) == [1]

    species_data3 = [
        {'portal_id': 1, 'features': [2, 0.5, 0.2]},
        {'portal_id': 2, 'features': [5, 0.3, 0.1]}
    ]
    test_data3 = [[7, 0.6, 0.3]]
    assert candidate(species_data3, test_data3, 2) == [2]

    species_data4 = [
        {'portal_id': 1, 'features': [120, 0.5, 0.2]},
        {'portal_id': 2, 'features': [220, 0.3, 0.1]},
        {'portal_id': 1, 'features': [119, 0.4, 0.2]},
        {'portal_id': 2, 'features': [215, 0.25, 0.15]}
    ]
    test_data4 = [[120, 0.5, 0.2], [220, 0.3, 0.15], [115, 0.45, 0.25]]
    assert candidate(species_data4, test_data4, 3) == [1, 2, 1]

    species_data5 = [
        {'portal_id': 1, 'features': [5, 0.5, 0.4]}
    ]
    test_data5 = [[5, 0.5, 0.4]]
    assert candidate(species_data5, test_data5, 1) == [1]
```

## Entry Point

`plant_portal_classifier`

## Extra Info

## Field

['Machine Learning']

## Cover Story

['portal', 'living plants']

## Cleaned Prompt

```python
Develop a machine learning classifier that predicts the portal based on characteristics of plants. Implement a k-Nearest Neighbours classifier to classify test data. Handle Euclidean distance calculation, determination of k-nearest vectors, and majority vote for classification.
    Example:
    Input: species_data=[{'portal_id': 1, 'features': [10, 0.5, 0.2]}, {'portal_id': 2, 'features': [20, 0.3, 0.1]}], test_data=[[10, 0.5, 0.3], [20, 0.3, 0.2]], k=3
    Output: [1, 2]
```

## Warnings

- Solution failed correctness check. reason: failed: 
- 5, Unclear Data Structure: The problem statement provides an overly complex description of handling the ML model but does not provide adequate exploration of expected feature data characteristics and edge cases like feature normalization, handling categorical data, or missing values, which can significantly impact the model's performance in real scenarios.
- 4, Inadequate Error Handling: The problem does not provide guidance on error handling conditions such as when k is larger than the number of available data points, or when all nearest neighbors have the same distance but different portal IDs, which can lead to ambiguous results.

