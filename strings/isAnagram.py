"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
def isAnagram(s, t):
    # Check if the lengths of both strings are different; if so, they can't be anagrams.
    if len(s) != len(t):
        return False

    # Create dictionaries to count character occurrences in both strings.
    s_count = {}
    t_count = {}

    # Count character occurrences in string s.
    for char in s:
        s_count[char] = s_count.get(char, 0) + 1

    # Count character occurrences in string t.
    for char in t:
        t_count[char] = t_count.get(char, 0) + 1

    # Compare the character counts in both dictionaries.
    return s_count == t_count

# Example 1
s1 = "anagram"
t1 = "nagaram"
result1 = isAnagram(s1, t1)  # Output: true
print(result1)

# Example 2
s2 = "rat"
t2 = "car"
result2 = isAnagram(s2, t2)  # Output: false
print(result2)

"""
We define a function isAnagram that takes two strings, s and t, as input.

We check if the lengths of s and t are different. If they have different lengths, they cannot be anagrams, so we return False.

We create two dictionaries, s_count and t_count, to count the occurrences of characters in both strings.

We iterate through string s and count the occurrences of each character, storing them in the s_count dictionary.

Similarly, we iterate through string t and count the occurrences of each character, storing them in the t_count dictionary.

After counting the character occurrences in both strings, we compare the two dictionaries (s_count and t_count) to check if they are equal. If they are equal, it means that the two strings have the same characters with the same counts, so we return True. Otherwise, we return False.

This code efficiently checks if two strings are anagrams of each other. It runs in O(n) time complexity, where n is the length of the longer string among s and t.

Unicode Characters Consideration (Follow-up):

If the inputs contain Unicode characters, you can adapt the solution by using a dictionary to count character occurrences in both strings, just as demonstrated above. The code will work for Unicode characters as well because dictionaries in Python can handle Unicode characters without any issues. The core logic remains the same; only the character set becomes larger due to Unicode.
"""