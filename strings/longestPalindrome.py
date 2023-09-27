"""
Given a string s, return the longest 
palindromic
 
substring
 in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

def longestPalindrome(s):
    # Define a function to find the longest palindromic substring centered at a given index.
    def expandAroundCenter(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # Expand outward from the center while characters match.
            left -= 1
            right += 1
        return s[left + 1:right]  # Return the palindrome substring found.

    longest = ""  # Initialize a variable to store the longest palindrome.

    # Iterate through each character in the string.
    for i in range(len(s)):
        # For odd-length palindromes:
        palindrome1 = expandAroundCenter(i, i)  # Expand around the current character as the center.
        if len(palindrome1) > len(longest):
            # Update the longest palindrome if a longer one is found.
            longest = palindrome1

        # For even-length palindromes:
        palindrome2 = expandAroundCenter(i, i + 1)  # Expand around the current character and the next as centers.
        if len(palindrome2) > len(longest):
            # Update the longest palindrome if a longer one is found.
            longest = palindrome2

    return longest  # Return the longest palindromic substring found.

# Example 1
s1 = "babad"
result1 = longestPalindrome(s1)  # Output: "bab" (or "aba" is also valid)
print(result1)

# Example 2
s2 = "cbbd"
result2 = longestPalindrome(s2)  # Output: "bb"
print(result2)

"""
We define the longestPalindrome function.

Inside the function, we define the expandAroundCenter function to find palindromes centered at specific indices.

We initialize the longest variable as an empty string to store the longest palindrome found.

We start iterating through each character in the input string s using the variable i.

For the first character 'b':

We consider odd-length palindromes and call expandAroundCenter(i, i) to expand around 'b' as the center.
The expandAroundCenter function checks both sides of the center character ('b') and expands outward while characters match. In this case, it expands to 'bab', which is a palindrome.
We compare the length of this palindrome (len(palindrome1)) to the length of the longest palindrome found so far (len(longest)) and find that it's longer.
We update longest to 'bab'.
For the second character 'a':

We consider even-length palindromes and call expandAroundCenter(i, i + 1) to expand around 'a' and the next character 'b' as centers.
The expandAroundCenter function checks both sides of the centers ('a' and 'b') and expands outward while characters match. In this case, it expands to 'aba', which is a palindrome.
We compare the length of this palindrome (len(palindrome2)) to the length of the longest palindrome found so far (len(longest)) and find that it's also longer.
We update longest to 'aba'.
We continue this process for the remaining characters 'b', 'a', and 'd'.

After iterating through the entire string, we return the longest palindromic substring, which is 'bab' (or 'aba').

Finally, we print the result, which is 'bab' (or 'aba').
"""