# Task ID: hard/5

## Prompt

```python
def classify_plant_species(descriptions):
    """
    In the Greenthumb Gorge, scientists have documented several unique plant species. Each plant species has been described textually, revealing attributes such as color, size, and leaf shape. Your task is to develop a function that classifies these plants into specific categories based on their textual descriptions.

    Your function should take a list of descriptions and return a list of predicted categories for each description. Implement text processing, feature extraction, and machine learning classification algorithms to classify each plant properly.

    Example:
        Input:  ['Small plant with needle-like leaves and red flowers', 'Large tree with broad leaves and round fruits']
        Output: ['Cactus', 'Fruit Tree']

    Note:
    - The categories you need to classify are 'Cactus', 'Fruit Tree', 'Palm Tree', 'Sunflower', 'Vine', 'Carnivorous Plant', 'Rose', 'Oak Tree', 'Bush'.
    - Use any necessary NLP techniques and Machine Learning models (e.g., SVM, RandomForest).
    """
```

## Canonical Solution

```python
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.preprocessing import LabelEncoder
        from sklearn.svm import SVC

        # Training data and labels (example, real dataset should be provided or accessed for actual usage)
        descriptions = ['Small plant with needle-like leaves and red flowers', 'Large tree with broad leaves and round fruits']
        labels = ['Cactus', 'Fruit Tree']

        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(descriptions)

        label_encoder = LabelEncoder()
        y = label_encoder.fit_transform(labels)

        model = SVC()
        model.fit(X, y)

        def classify_plant_species(descriptions):
            transformed_descriptions = vectorizer.transform(descriptions)
            predictions = model.predict(transformed_descriptions)
            return label_encoder.inverse_transform(predictions)
```

## Test Cases

```python
def check(candidate):
    assert candidate(['Small cactus with spiky silhouette','Tall palm tree with coconuts']) == ['Cactus', 'Palm Tree']
    assert candidate(['Flowering plant with large yellow petals', 'Vine with round grapes']) == ['Sunflower', 'Vine']
    assert candidate(['Carnivorous plant with sharp trap', 'Rose with thorns and red petals']) == ['Carnivorous Plant', 'Rose']
    assert candidate(['Oak tree with hard bark and acorns', 'Small prickly bush with blueberries']) == ['Oak Tree', 'Bush']
    assert candidate([]) == []
```

## Entry Point

`classify_plant_species`

## Extra Info

## Topics

['Machine Learning', 'Natural Language Processing', 'Text Classification']

## Field

['Computer Science']

## Cover Story

['Greenthumb Gorge', 'plant species']

## Cleaned Prompt

```python
Develop a function to classify plant species based on textual descriptions using text processing and machine learning. Example input: ['Small plant with needle-like leaves and red flowers'] outputs 'Cactus'. Define specific categories such as 'Cactus', 'Fruit Tree', etc., for classification.
```

## Warnings

- Solution failed correctness check. reason: failed: invalid syntax (<string>, line 14)
- 5, Missing Data: The problem description suggests building a machine learning model to classify plant species from descriptions but does not provide a dataset for training the model. It only provides a minimal example, which is insufficient for training a robust classifier.
- 4, Training in Function: The canonical solution indicates that feature extraction and model training occurs within the function. This is a flawed practice as training should only happen once, and the trained model should be callable or utilized for predictions without retraining at each function call.
- 5, Unclear Problem Scope: The problem assumes the implementation of advanced text processing and machine learning algorithms without clear constraints or requirements on the algorithm's performance, computational efficiency, or the handling of ambiguous or unseen descriptions.

