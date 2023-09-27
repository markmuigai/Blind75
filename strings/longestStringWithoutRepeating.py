"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 # initialize left pointer to the beginning of the string
        right = 0 # initialize right pointer to the beginning of the string
        max_len = 0 # initialize the maximum length to 0
        char_set = set() # initialize an empty set to keep track of characters in the substring
        
        while right < len(s): # loop until the right pointer reaches the end of the string
            if s[right] not in char_set: # if the current character is not in the set
                char_set.add(s[right]) # add it to the set
                right += 1 # move the right pointer to the right
                max_len = max(max_len, len(char_set)) # update the maximum length if necessary
            else: # if the current character is in the set
                char_set.remove(s[left]) # remove the character at the left pointer from the set
                left += 1 # move the left pointer to the right
        
        return max_len # return the maximum length of a substring without repeating characters
