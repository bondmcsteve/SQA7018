"""This problem is based on Problem 4.3.2 from the textbook"""

"""ROT 13 substitution is designed to substitute a letter as such that 
its substitution is 13 places upward away in rotational manner"""
def rot13(word):
    """Apply ROT13 cipher to a word containing lowercase letters only."""
    return ''.join(
        chr(((ord(char) - ord('a') + 13) % 26) + ord('a')) if 'a' <= char <= 'z' else char
        for char in word
    )

"""
the above also the same with the below and it is easy to understand

def rot13(word):
    result = ''
    for char in word:
        if 'a' <= char <= 'z':
            # Shift character by 13, wrapping around at 'z'
            result += chr(((ord(char) - ord('a') + 13) % 26) + ord('a'))
        else:
            # Keep non-lowercase characters as is
            result += char
    return result
"""

def rot13_sentence(sentence):
    """Apply ROT13 cipher to a sentence of lowercase words separated by spaces."""
    return ' '.join(rot13(word) for word in sentence.split())


word = "hello"
encoded_word = rot13(word)
print("Encoded word:", encoded_word)  # Expected: "uryyb"


sentence = "hello world this is rot13"
encoded_sentence = rot13_sentence(sentence)
print("Encoded sentence:", encoded_sentence)  # Expected ROT13 encoded sentence
