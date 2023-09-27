"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

def isPalindrome(s):
    # Initialize left and right pointers to the start and end of the string.
    left, right = 0, len(s) - 1
    
    while left < right:
        # Move the left pointer to the right until it points to an alphanumeric character.
        while left < right and not s[left].isalnum():
            left += 1
        
        # Move the right pointer to the left until it points to an alphanumeric character.
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Convert both characters to lowercase and compare them.
        if s[left].lower() != s[right].lower():
            return False
        
        # Move both pointers towards each other.
        left += 1
        right -= 1
    
    return True

# Example 1
s1 = "A man, a plan, a canal: Panama"
result1 = isPalindrome(s1)  # Output: true
print(result1)

# Example 2
s2 = "race a car"
result2 = isPalindrome(s2)  # Output: false
print(result2)

# Example 3
s3 = " "
result3 = isPalindrome(s3)  # Output: true
print(result3)

"""
We define a function isPalindrome that takes a string s as input.

We initialize two pointers, left and right, to the start and end of the string, respectively.

We enter a while loop that continues as long as left is less than right, which means we are still comparing characters from both ends of the string.

Inside the loop, we move the left pointer to the right until it points to an alphanumeric character using a while loop with the condition not s[left].isalnum().

Similarly, we move the right pointer to the left until it points to an alphanumeric character using another while loop.

We convert both characters to lowercase using the lower() method and compare them. If they are not equal, we return False because the string is not a palindrome.

If the characters match, we increment the left pointer and decrement the right pointer to continue checking the next pair of characters.

The loop continues until we have checked all valid alphanumeric characters in the string.

After the loop, if we haven't returned False, it means the string is a palindrome, and we return True.


"""