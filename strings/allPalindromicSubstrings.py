"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""

def countPalindromes(s):
    n = len(s)
    count = 0  # Initialize a variable to count palindromic substrings.

    # Initialize a 2D boolean table to store whether substrings are palindromes.
    dp = [[False] * n for _ in range(n)]

    # All substrings of length 1 are palindromes.
    for i in range(n):
        dp[i][i] = True
        count += 1  # Increment the count for each single character palindrome.

    # Check for palindromic substrings of length 2.
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            count += 1  # Increment the count for each two-character palindrome.

    # Check for palindromic substrings of length greater than 2.
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1  # Ending index of the current substring.
            # Check if the substring is a palindrome and the characters at both ends match.
            if dp[i + 1][j - 1] and s[i] == s[j]:
                dp[i][j] = True
                count += 1  # Increment the count for each longer palindrome.

    return count

# Example 1
s1 = "abc"
result1 = countPalindromes(s1)  # Output: 3
print(result1)

# Example 2
s2 = "aaa"
result2 = countPalindromes(s2)  # Output: 6
print(result2)

"""
We define a function countPalindromes that takes a string s as input.

We determine the length of the input string s and initialize a variable count to count the palindromic substrings.

We initialize a 2D boolean table dp of size n x n (where n is the length of s) to store whether substrings are palindromes.

We iterate through each character in the input string s and set the corresponding diagonal elements in dp to True because all substrings of length 1 are palindromes. For each of these substrings, we increment the count variable.

We check for palindromic substrings of length 2. For each pair of adjacent characters, if they are the same, we set dp[i][i + 1] to True to mark them as palindromes. For each of these substrings, we increment the count variable.

We check for palindromic substrings of length greater than 2.

We iterate over different lengths (length) starting from 3 to the length of the input string s.
For each length, we iterate through all possible starting indices i of the substring.

We calculate the ending index j of the current substring.

We check if the substring from i to j is a palindrome by verifying that the characters at both ends match (s[i] == s[j]) and that the substring inside the current endpoints (dp[i+1][j-1]) is also a palindrome.

If the substring is a palindrome, we set dp[i][j] to True to mark it as a palindrome. For each of these substrings, we increment the count variable.

After all iterations, we return the count variable, which represents the total number of palindromic substrings found.

21-28. We demonstrate the code's functionality with two examples, printing the results for each.

This code efficiently counts the number of palindromic substrings using a dynamic programming approach and has a time complexity of O(n^2), where "n" is the length of the input string s.
"""

"""
OPTIMAL SOLUTION IN LINEAR TIME O(n) - Manacher's Algorithm
"""
def countPalindromes(s):
    # Transform the input string to include special characters to handle even-length palindromes.
    transformed_s = '#'.join('^{}$'.format(s))

    n = len(transformed_s)
    p = [0] * n  # Initialize an array to store palindrome lengths.
    C, R = 0, 0  # Initialize center and right boundary of the current palindrome.

    for i in range(1, n - 1):
        # Calculate the mirror index of the current index.
        mirror = 2 * C - i

        if i < R:
            # Check if the current index is within the right boundary of the current palindrome.
            p[i] = min(R - i, p[mirror])

        # Attempt to expand around the current index.
        while transformed_s[i + p[i] + 1] == transformed_s[i - p[i] - 1]:
            p[i] += 1

        if i + p[i] > R:
            # Update the center and right boundary if needed.
            C, R = i, i + p[i]

    # Calculate the total count of palindromic substrings (excluding special characters).
    total_count = sum((l + 1) // 2 for l in p)

    return total_count

# Example 1
s1 = "abc"
result1 = countPalindromes(s1)  # Output: 3
print(result1)

# Example 2
s2 = "aaa"
result2 = countPalindromes(s2)  # Output: 6
print(result2)

"""
We define a function countPalindromes that takes a string s as input.

We transform the input string s to include special characters (#) between each character and add start (^) and end ($) markers to handle even-length palindromes.

We determine the length of the transformed string transformed_s.

We initialize an array p of length n to store the lengths of palindromes centered at each index. All elements are initially set to 0.

We initialize two variables, C and R, to represent the center and right boundary of the current palindrome.

We iterate through the transformed string transformed_s from index 1 to n - 2 (excluding the start and end markers).

We calculate the mirror index of the current index i to optimize palindrome length calculation.

If the current index i is within the right boundary R, we calculate p[i] as the minimum of two values: R - i and the palindrome length at the mirror index mirror.

We attempt to expand around the current index i by comparing characters on both sides. If they match, we increment p[i] to expand the palindrome.

If the expanded palindrome reaches beyond the right boundary R, we update C (center) and R (right boundary) accordingly.

After processing all indices in the transformed string, we calculate the total count of palindromic substrings. We sum (l + 1) // 2 for each palindrome length l to account for both odd and even-length palindromes.

Finally, we return the total count of palindromic substrings.
"""