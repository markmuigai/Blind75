"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

def isValid(s):
    stack = []  # Create an empty stack to store open brackets.

    # Define a dictionary to map open brackets to their corresponding closing brackets.
    bracket_mapping = {')': '(', '}': '{', ']': '['}

    # Iterate through each character in the input string.
    for char in s:
        if char in bracket_mapping:
            # If the character is a closing bracket:
            # Pop the top element from the stack if it matches the corresponding open bracket.
            # If the stack is empty or the top element doesn't match, return False (invalid).
            top_element = stack.pop() if stack else '#'
            if top_element != bracket_mapping[char]:
                return False
        else:
            # If the character is an open bracket, push it onto the stack.
            stack.append(char)

    # After iterating through the entire string, if the stack is empty, it's valid; otherwise, it's invalid.
    return not stack

# Example 1
s1 = "()"
result1 = isValid(s1)  # Output: true
print(result1)

# Example 2
s2 = "()[]{}"
result2 = isValid(s2)  # Output: true
print(result2)

# Example 3
s3 = "(]"
result3 = isValid(s3)  # Output: false
print(result3)


"""
We define a function isValid that takes a string s as input.

We create an empty stack (implemented as a list) to store open brackets encountered while iterating through the string.

We define a dictionary bracket_mapping to map closing brackets to their corresponding open brackets. This mapping is essential for checking the validity of the brackets.

We iterate through each character in the input string s.

For each character, we check if it is a closing bracket (')', '}', or ']') by looking it up in the bracket_mapping dictionary.

If the character is a closing bracket, we pop the top element from the stack if the stack is not empty. This popped element should be the corresponding open bracket. If it doesn't match, we return False because it's invalid.

If the character is an open bracket ('(', '{', or '['), we simply push it onto the stack.

After iterating through the entire string, if the stack is empty, it means all open brackets were correctly closed, and the string is valid. If the stack is not empty, there are unmatched open brackets, and the string is invalid.

We return not stack to return True if the stack is empty (valid) and False if the stack is not empty (invalid).

This code efficiently checks the validity of bracket pairs in the string and has a time complexity of O(n), where "n" is the length of the input string s.
"""