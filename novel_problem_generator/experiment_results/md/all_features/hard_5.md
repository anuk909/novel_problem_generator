# Task ID: hard/5

## Prompt

```python
def sentinel_rock_cipher(message, rocks):
    """
    Write a function that takes a string message and a list of integers rocks. Each integer in rocks represents a valued rock. The encryption of the message is determined by converting each character of the message into its ASCII value. Subsequently, only the rocks that are prime numbers (heavy rocks) are taken, and their product is used to modulate each ASCII value before converting them back to characters.

    If there are no prime numbers in rocks (no heavy rocks), the function should return the original message.

    This encryption ensures that the characters are shuffled in a way that their new values are the remainder when their ASCII values are divided by the product of the heavy rocks.

    Examples:
    - If rocks are [2, 3, 6, 7, 10], the heavy rocks are [2, 3, 7]. The product of these prime-valued rocks is 42. Each character's ASCII value in the message is modulated by 42 and then converted back to characters to form the encrypted message.
    - If there are no heavy rocks, like in rocks = [4, 6, 8], the original message is returned.

    Note: The function might return non-printable or special characters as part of the encrypted message due to the modulation operation.
    """

```

## Canonical Solution

```python
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    modulus = 1
    for rock in rocks:
        if is_prime(rock):
            modulus *= rock
    if modulus == 1:
        return message
    else:
        encrypted_message = ''.join(chr(ord(char) % modulus) for char in message)
        return encrypted_message
```

## Test Cases

```python
def check(candidate):
    assert candidate("Hello, world!", [2, 3, 6, 7, 10]) == "]6JU!I12JU@"
    assert candidate("Desert rocks", [11, 13, 16]) == "3M46C1*3CK2"
    assert candidate("No primes", []) == "No primes"
    assert candidate("abc", [999]) == "abc"
    assert candidate("12345", [2, 5, 7, 11]) == "N)*+*"
    assert candidate("Test with non-prime", [4, 6, 8, 10]) == "Test with non-prime"
```

## Entry Point

`sentinel_rock_cipher`

## Extra Info

## Topics

['Cryptography', 'Number Theory']

## Field

['Cybersecurity']

## Cover Story

['desert', 'sentient rocks']

## Cleaned Prompt

```python
Write a function sentinel_rock_cipher(message, rocks) that takes a message (string) and rocks (list of integers). Encrypt the message by converting each character to its ASCII value and then modulating by the product of the prime-values in rocks, converting the result back to characters. If there are no prime values in rocks, return the original message.
```

## Warnings

- Solution failed correctness check. reason: failed: 
- 4, Overflow risk in product of heavy rocks: There is no safeguard in the function against overflow or extremely large values when calculating the product of prime-valued rocks ('heavy rocks'). This could lead to incorrect results or runtime errors due to integer overflow, especially for large inputs.

