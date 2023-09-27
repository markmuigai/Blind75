"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 
Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""

from collections import Counter

def min_window_substring(s, t):
    # Initialize variables to keep track of character counts.
    t_counter = Counter(t)  # Counter for characters in t.
    s_counter = Counter()   # Counter for characters in the current window.
    
    # Initialize pointers and other variables.
    left = 0               # Left pointer of the sliding window.
    min_len = float('inf')  # Initialize the minimum window length.
    min_window = ""         # Initialize the minimum window substring.
    required_chars = len(t_counter)  # Count of unique characters in t.
    formed_chars = 0        # Count of unique characters formed in the window.
    
    # Iterate through the string s using the right pointer.
    for right in range(len(s)):
        char = s[right]
        
        # Update the character count in the current window.
        s_counter[char] += 1
        
        # Check if the current character forms a required character in the window.
        if char in t_counter and s_counter[char] == t_counter[char]:
            formed_chars += 1
        
        # Try to minimize the window by moving the left pointer.
        while left <= right and formed_chars == required_chars:
            # Calculate the current window length.
            current_len = right - left + 1
            
            # Update the minimum window information if needed.
            if current_len < min_len:
                min_len = current_len
                min_window = s[left:right+1]
            
            # Move the left pointer to the right to shrink the window.
            left_char = s[left]
            s_counter[left_char] -= 1
            if left_char in t_counter and s_counter[left_char] < t_counter[left_char]:
                formed_chars -= 1
            
            left += 1
    
    return min_window

# Example 1
s1 = "ADOBECODEBANC"
t1 = "ABC"
result1 = min_window_substring(s1, t1)  # Output: "BANC"
print(result1)

# Example 2
s2 = "a"
t2 = "a"
result2 = min_window_substring(s2, t2)  # Output: "a"
print(result2)

# Example 3
s3 = "a"
t3 = "aa"
result3 = min_window_substring(s3, t3)  # Output: ""
print(result3)


"""
We import the Counter class from the collections module to count the characters in t and the current window.

We initialize two counters: t_counter to count characters in t and s_counter to count characters in the current window.

We initialize pointers and variables: left (left pointer), min_len (minimum window length), min_window (minimum window substring), required_chars (count of unique characters in t), and formed_chars (count of unique characters formed in the window).

We iterate through the string s using the right pointer (right).

For each character char at the right position, we update the character count in the current window (s_counter).

We check if the current character char forms a required character in the window by comparing its count in s_counter with the count in t_counter. If they are equal, it means we have formed a required character, so we increment formed_chars.

We then attempt to minimize the window by moving the left pointer (left) to the right while keeping track of character counts.

We calculate the current window length (current_len) and update the minimum window information (min_len and min_window) if the current window is smaller.

We move the left pointer to the right by decrementing the count of the character at the left end of the window (left_char) and updating formed_chars if necessary.

The loop continues until we cannot minimize the window further while still satisfying the required characters condition.

Finally, we return min_window, which contains the minimum window substring that includes all characters in t.

This code efficiently finds the minimum window substring with a time complexity of O(m + n), where m is the length of s and n is the length of t.

"""