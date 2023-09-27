"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""

def wordBreak(s, wordDict):
    # Create a set from the wordDict for faster word lookup.
    wordSet = set(wordDict)
    
    # Initialize a list dp to track whether substrings of s can be segmented.
    # dp[i] will be True if s[:i] (substring up to index i) can be segmented.
    dp = [False] * (len(s) + 1)
    
    # The empty string can always be segmented.
    dp[0] = True
    
    # Iterate through the characters of the string s.
    for i in range(1, len(s) + 1):
        for j in range(i):
            # Check if dp[j] is True (substring up to index j can be segmented)
            # and if s[j:i] (substring from j to i) is in the wordSet.
            if dp[j] and s[j:i] in wordSet:
                # If both conditions are met, mark dp[i] as True, indicating
                # that s[:i] can be segmented.
                dp[i] = True
                break
    
    # dp[len(s)] represents whether the entire string s can be segmented.
    return dp[len(s)]

# Example usage:
s1 = "leetcode"
wordDict1 = ["leet", "code"]
result1 = wordBreak(s1, wordDict1)
print("Can be segmented:", result1)

s2 = "applepenapple"
wordDict2 = ["apple", "pen"]
result2 = wordBreak(s2, wordDict2)
print("Can be segmented:", result2)

s3 = "catsandog"
wordDict3 = ["cats", "dog", "sand", "and", "cat"]
result3 = wordBreak(s3, wordDict3)
print("Can be segmented:", result3)
