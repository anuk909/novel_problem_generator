# Task ID: hard/6

## Prompt

```python
def locate_submarine_cables(images):
    """
    An Arctic research group is using a combination of underwater photogrammetry and sonar images to map locations of submarine cables. They receive multiple sorted lists of images with metadata, where each image is represented by a dictionary including 'timestamp', 'longitude', 'latitude', and 'probability' (that there is a cable in the image).

    Each list represents a separate surveying session along different paths. The output should be a single sorted list of images that efficiently integrates all the lists based on the timestamps to provide a chronological sequence of imagery for analysis.

    The function should also clean up and remove duplicates, considering images within a 5-second window and close proximity (less than 0.01 degrees in both longitude and latitude) as duplicates, keeping only the highest probability image within such groups.

    Example:
    input_list1 = [
        {'timestamp': 100, 'longitude': 5.0001, 'latitude': 59.0001, 'probability': 0.95},
        {'timestamp': 105, 'longitude': 5.0003, 'latitude': 59.0003, 'probability': 0.88}
    ]
    input_list2 = [
        {'timestamp': 102, 'longitude': 5.0002, 'latitude': 59.0002, 'probability': 0.90}
    ]
    Result = [
        {'timestamp': 100, 'longitude': 5.0001, 'latitude': 59.0001, 'probability': 0.95},
        {'timestamp': 105, 'longitude': 5.0003, 'latitude': 59.0003, 'probability': 0.88}
    ]
    """

```

## Canonical Solution

```python
    from heapq import heappop, heappush, heapify
    from collections import defaultdict

    def is_duplicate(img1, img2):
        return abs(img1['timestamp'] - img2['timestamp']) <= 5 and abs(img1['longitude'] - img2['longitude']) < 0.01 and abs(img1['latitude'] - img2['latitude']) < 0.01

    def merge_and_deduplicate(lists):
        heap = []
        result = []
        for image_list in lists:
            for image in image_list:
                heappush(heap, (image['timestamp'], image))

        while heap:
            time, current_image = heappop(heap)
            if not result or not is_duplicate(result[-1], current_image):
                result.append(current_image)
            elif result[-1]['probability'] < current_image['probability']:
                result[-1] = current_image

        return result
    return merge_and_deduplicate
```

## Test Cases

```python
def check(candidate):
    assert candidate([
        [{'timestamp': 100, 'longitude': 5.0001, 'latitude': 59.0001, 'probability': 0.95}],
        [{'timestamp': 101, 'longitude': 5.00011, 'latitude': 59.00011, 'probability': 0.92}]
    ]) == [{'timestamp': 100, 'longitude': 5.0001, 'latitude': 59.0001, 'probability': 0.95}]
    assert candidate([
        [{'timestamp': 100, 'longitude': 5.0, 'latitude': 59.0, 'probability': 0.9}],
        [{'timestamp': 105, 'longitude': 5.0005, 'latitude': 59.0005, 'probability': 0.95}]
    ]) == [{'timestamp': 100, 'longitude': 5.0, 'latitude': 59.0, 'probability': 0.9}, {'timestamp': 105, 'longitude': 5.0005, 'latitude': 59.0005, 'probability': 0.95}]
    assert candidate([]) == []
    assert candidate([
        []
    ]) == []
    assert candidate([
        [{'timestamp': 100, 'longitude': 5.0, 'latitude': 59.0, 'probability': 0.9}],
        [{'timestamp': 100, 'longitude': 5.0001, 'latitude': 59.0001, 'probability': 0.95}]
    ]) == [{'timestamp': 100, 'longitude': 5.0, 'latitude': 59.0, 'probability': 0.95}]

```

## Entry Point

`locate_submarine_cables`

## Extra Info

## Topics

['Database', 'Merge k Sorted Lists']

## Field

['Computer Vision']

## Cover Story

['arctic', 'underwater']

## Cleaned Prompt

```python
Given multiple sorted lists each containing image metadata {'timestamp', 'longitude', 'latitude', 'probability'}, merge them into a single sorted list by chronological order. Remove duplicate images considering a 5-second time window and 0.01 degrees proximity in both longitude and latitude, keeping the image with the highest probability in case of duplicates.
Example:
input_list1 = [
    {'timestamp': 100, 'longitude': 5.0001, 'latitude': 59.0001, 'probability': 0.95}
]
input_list2 = [
    {'timestamp': 102, 'longitude': 5.0002, 'latitude': 59.0002, 'probability': 0.90}
]
Result = [
    {'timestamp': 100, 'longitude': 5.0001, 'latitude': 59.0001, 'probability': 0.95}
]
```

## Warnings

- Solution failed correctness check. reason: failed: 
- 5, Undefined behavior for duplicate removal: The problem statement lacks clarity on the behavior when processing multiple images that are duplicates according to the defined criteria. For instance, if multiple images from different lists fall within the 5-second window and 0.01 degrees proximity, the problem spec is not clear on whether to keep images from different lists or just from the same list.
- 4, Potential flaw in duplicate determination logic: The function 'is_duplicate' depends on a heuristic, and there could be ambiguous cases not covered by the example. For example, if images with identical coordinates but a probability difference that is minuscule (e.g., 0.94 vs. 0.939999), it's uncertain if such images would reasonably be identified as duplicates.
- 4, Inconsistent outputs in example and test cases: The given example in the prompt does not follow the same logic that the test case seems to imply (especially considering timestamp proximity). In the example, images from input_list2 don't appear in the result though they might not necessarily be considered duplicates based on the distance although the timestamp difference is less than 5. This discrepancy could lead to confusion.

