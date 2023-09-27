"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
def groupAnagrams(strs):
    anagram_groups = {}  # Create a dictionary to store groups of anagrams.
    
    for word in strs:
        # Sort the characters in the word and use it as a key for grouping.
        sorted_word = ''.join(sorted(word))
        
        # If the sorted word is not in the dictionary, create a new group.
        if sorted_word not in anagram_groups:
            anagram_groups[sorted_word] = [word]
        else:
            # If the sorted word is already a key, append the word to its group.
            anagram_groups[sorted_word].append(word)

    # Convert the values of the dictionary (anagram groups) to a list of lists.
    result = list(anagram_groups.values())

    return result

# Example 1
strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
result1 = groupAnagrams(strs1)
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(result1)

# Example 2
strs2 = [""]
result2 = groupAnagrams(strs2)
# Output: [[""]]
print(result2)

# Example 3
strs3 = ["a"]
result3 = groupAnagrams(strs3)
# Output: [["a"]]
print(result3)

"""
We define a function groupAnagrams that takes an array of strings strs as input.

We create an empty dictionary anagram_groups to store groups of anagrams. The keys of this dictionary will be sorted strings (anagram patterns), and the values will be lists of words that share the same sorted pattern.

We iterate through each word in the input strs.

For each word, we sort its characters alphabetically and join them back into a string to create a sorted word (sorted_word). This sorted word will be used as a key for grouping anagrams.

We check if the sorted_word is not already a key in the anagram_groups dictionary. If it's not, we create a new group by assigning the word to a list in the dictionary with the sorted word as the key.

If the sorted_word is already a key, it means we've encountered another anagram of the same pattern, so we append the word to the existing group.

After processing all words in strs, we have groups of anagrams organized in the anagram_groups dictionary.

To obtain the final result, we convert the values of the anagram_groups dictionary (which are lists of anagrams) into a list of lists and store it in the result variable.

We return the result, which contains groups of anagrams.

This code efficiently groups anagrams together and has a time complexity of O(n * k * log(k)), where "n" is the number of strings in strs, and "k" is the maximum length of a string in strs. The most time-consuming part is the sorting of characters within each string.
"""