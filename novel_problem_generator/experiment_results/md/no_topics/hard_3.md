# Task ID: hard/3

## Prompt

```python
def decrypt_message(cipher_text, key):
    """
    As a secret agent, you've intercepted a string of cipher text transmitted from the sorcerer's tower. This cipher text has been encoded using a custom cyclic key encryption based on Caesar Cipher but with a repeating sequence key.

    Your job is to decrypt it using the known key which consists of a list of integer shifts. Each integer in the list shifts a corresponding character in the cipher text back by that many places in the alphabet.

    The key repeats if the cipher text is longer than the key itself. If the text includes any non-alphabetic characters, they should be left untouched.

    Given the encrypted string 'cipher_text' and a list of integers 'key' representing the cyclic shifts, return the decrypted message as a string.

    Example:
    If the input is cipher_text = "Vdqdqhvflv" and key = [3, 1, 4], the output should be "Sasquatch" since applying the shifts -3, -1, -4 cyclically to each character in 'Vdqdqhvflv' results in 'Sasquatch'.

    Note:
    - Non-alphabet characters must remain unchanged in their position.
    - The decryption preserves the case of the input to handle both uppercase and lowercase letters correctly.
    - The function should handle empty strings smoothly.
    """
```

## Canonical Solution

```python
    def decrypt_character(c, shift):
        if c.isalpha():
            start = ord('a') if c.islower() else ord('A')
            return chr((ord(c) - start - shift) % 26 + start)
        else:
            return c

    result = ''
    key_length = len(key)
    for index, character in enumerate(cipher_text):
        shift = key[index % key_length]
        result += decrypt_character(character, shift)
    return result
```

## Test Cases

```python
def check(candidate):
    assert candidate("Vdqdqhvflv", [3, 1, 4]) == "Sasquatch"
    assert candidate("", [1, 2, 3]) == ""
    assert candidate("Hello, World!", [1, 0, 0]) == "Gdkkn, World!"
    assert candidate("AbC", [1, -1, 1]) == "ZaA"
    assert candidate("Complex123", [3, -3, 5, -5]) == "Zljmgdy123"
```

## Entry Point

`decrypt_message`

## Extra Info

## Field

['Cybersecurity']

## Cover Story

['secret agent', "sorcerer's tower"]

## Cleaned Prompt

```python
Write a function that takes a string 'cipher_text' and a list of integers 'key' which represents cyclic shifts to decrypt a custom Caesar Cipher encrypted text. The key repeats for longer texts. Non-alphabetic characters remain untouched. The decryption preserves the case of incoming characters. For example, using cipher_text = "Vdqdqhvflv" and key = [3, 1, 4], the function should return "Sasquatch".
Given this prompt, ensure the problem description, test cases, and canonical solution are consistent regarding case sensitivity.
```

## Warnings

- Solution failed correctness check. reason: failed: invalid syntax (<string>, line 18)
- 4, Inconsistent Case Sensitivity Instruction: The problem statement mentions decryption should treat uppercase and lowercase alphabet characters equivalently, but the implementation provided in canonical solution, and expected outputs in tests, evidently maintain case sensitivity. This could cause uncertainty on how input case should be managed and whether or not case normalization is required before decryption.
- 5, Confusing Problem Description: The description indicates treating 'A' and 'a' as equivalent which contradicts the test cases and provided solutions that maintain distinct uppercase and lowercase characters in the output. This inconsistency introduces significant confusion on operational expectations and result format in the decryption process.

