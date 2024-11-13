# This problem is based on Problem 2.7.7 from the textbook

def is_palindrome_recursive(s):
    s = ''.join(filter(str.isalnum, s.lower()))
    """Check if a string is a palindrome using recursion."""
    # Base cases: empty string or single character string is a palindrome
    if len(s) <= 1:
        return True

    # Recursive case: Check first and last characters, then recurse
    if s[0] == s[-1]:
        # This part here loops the function and passes value s such
        # that two elements at both endpoints are reduced.
        # The string is shrunk from outside to inside until the string is
        # symmetrically eliminated or remain with only 1 char.
        return is_palindrome_recursive(s[1:-1])

    # If the first and last characters do not match, it's not a palindrome
    return False

#Quiz 5, Q9
print(is_palindrome_recursive("Able was I ere I saw Elba"))  # Expected output: True

#Original test cases
# print(is_palindrome_recursive("racecar"))  # Expected output: True
# print(is_palindrome_recursive("hello"))  # Expected output: False
# print(is_palindrome_recursive("madam"))  # Expected output: True
# print(is_palindrome_recursive("a"))  # Expected output: True
# print(is_palindrome_recursive(""))  # Expected output: True
# print(is_palindrome_recursive("hei-roh"))