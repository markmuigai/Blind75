"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.
"""
def characterReplacement(s, k):
    char_count = {}  # Create a dictionary to store the count of each character.
    max_length = 0   # Initialize the maximum substring length.
    start = 0        # Initialize the start of the sliding window.
    max_count = 0    # Initialize the maximum character count in the current window.
    
    for end in range(len(s)):
        char = s[end]
        char_count[char] = char_count.get(char, 0) + 1
        # Update the count of the current character in the window.
        
        max_count = max(max_count, char_count[char])
        # Update the maximum character count in the window.
        
        # Calculate the length of the current window.
        window_length = end - start + 1
        
        # If the window size minus the maximum character count exceeds k,
        # it means we can't replace more than k characters to make all characters the same.
        # In this case, we need to shrink the window from the start.
        if window_length - max_count > k:
            char_count[s[start]] -= 1
            start += 1
        
        # Update the maximum substring length.
        max_length = max(max_length, window_length)
    
    return max_length

# Example 1
s1 = "ABAB"
k1 = 2
result1 = characterReplacement(s1, k1)  # The result is 4.
print(result1)

# Example 2
s2 = "AABABBA"
k2 = 1
result2 = characterReplacement(s2, k2)  # The result is 4.
print(result2)

"""
The "window" in this context refers to a substring of the original string s. It's a portion of the string that we examine to find the longest substring with the same character count. The window starts at the start index and ends at the end index.

window_length represents the length of the current window. It is calculated as end - start + 1, which gives us the number of characters in the window.

max_count is the maximum count of any single character within the current window. It keeps track of the character that appears most frequently within the window.

The condition window_length - max_count > k checks whether we can transform the characters in the current window into a substring with the same character count by replacing no more than k characters.

If window_length - max_count > k, it means that the difference between the total characters in the window and the maximum character count exceeds k. In other words, we can't make all characters the same within the given k replacements.

To address this, we need to shrink the window from the start. We do this by moving the start index one step to the right and updating the character count accordingly. This effectively shortens the window, allowing us to explore new possibilities for a longer substring with the same character count while keeping the total replacements within k.
"""