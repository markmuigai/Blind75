"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""

def longestCommonSubsequence(text1, text2):
    # Get the lengths of the two input strings.
    m, n = len(text1), len(text2)
    
    # Create a 2D DP (Dynamic Programming) table to store the length of the longest common subsequence.
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Iterate through the characters of both strings to fill the DP table.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If the characters match, extend the length of the common subsequence by 1.
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            # If the characters don't match, take the maximum of the lengths without the current characters.
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # The value at dp[m][n] represents the length of the longest common subsequence.
    return dp[m][n]

# Example usage:
text1 = "abcde"
text2 = "ace"
result1 = longestCommonSubsequence(text1, text2)
print("Longest common subsequence length:", result1)

text3 = "abc"
text4 = "def"
result2 = longestCommonSubsequence(text3, text4)
print("Longest common subsequence length:", result2)



"""
Easiest solution O(m * n)
"""

def longestCommonSubsequence(text1, text2):
    # Initialize two pointers, p1 and p2, to 0. These will represent positions in text1 and text2, respectively.
    p1, p2 = 0, 0
    
    # Initialize a variable count to 0. It will keep track of the length of the common subsequence.
    count = 0

    # Start a loop that continues as long as both p1 and p2 are within the bounds of their respective strings.
    while p1 < len(text1) and p2 < len(text2):
        # Compare the characters at text1[p1] and text2[p2].
        if text1[p1] == text2[p2]:
            # If the characters match, it means a common character is found in the subsequence.
            # Increment both p1 and p2 by 1 to move to the next characters in both strings.
            count += 1
            p1 += 1
            p2 += 1
        else:
            # If the characters don't match, decide which pointer to increment based on which character should be skipped.
            # We choose to increment the pointer that leads to the shorter remaining substring.
            if len(text1) - p1 > len(text2) - p2:
                p1 += 1
            else:
                p2 += 1

    # After the loop, count represents the length of the longest common subsequence.
    return count

# Example usage:
text1 = "abcde"
text2 = "ace"
result = longestCommonSubsequence(text1, text2)
print("Longest common subsequence length:", result)