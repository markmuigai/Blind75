"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.
"""

# Define a TrieNode class to represent nodes in the Trie.
class TrieNode:
    def __init__(self):
        # Initialize an empty dictionary to store children nodes.
        self.children = {}
        # Initialize a flag to mark the end of a word.
        self.is_end_of_word = False

# Define the WordDictionary class.
class WordDictionary:

    def __init__(self):
        # Initialize the Trie with an empty root node.
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # Start at the root node.
        node = self.root
        # Traverse each character in the word.
        for char in word:
            # If the character is not in the children of the current node,
            # create a new TrieNode for it and add it to the children.
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the next node (character).
            node = node.children[char]
        # Mark the last node as the end of a word.
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        # Define a depth-first search (dfs) function to search for words with wildcard characters.
        def dfs(node, index):
            # If we have reached the end of the search word, return whether the current node marks the end of a word.
            if index == len(word):
                return node.is_end_of_word
            # Get the character at the current index in the search word.
            char = word[index]
            # If the character is not a wildcard ('.'), check if it exists in the children of the current node.
            if char != '.':
                if char in node.children:
                    # Recursively search for the next character in the Trie.
                    return dfs(node.children[char], index + 1)
                else:
                    # If the character is not found, return False.
                    return False
            else:  # If the character is a wildcard ('.'), handle wildcard search.
                # Iterate through all children nodes of the current node.
                for child in node.children.values():
                    # Recursively search for the next character in the Trie.
                    if dfs(child, index + 1):
                        return True
                # If none of the children nodes match the next character, return False.
                return False

        # Start the search from the root node and the beginning of the search word.
        return dfs(self.root, 0)

"""
# Create a WordDictionary object
wordDictionary = WordDictionary()

# Add words to the dictionary
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")

# Search for "pad" in the dictionary
# The word "pad" is not in the dictionary, and it does not contain wildcard characters.
# Therefore, the result is False.
print(wordDictionary.search("pad"))  # Output: False

# Search for "bad" in the dictionary
# The word "bad" is in the dictionary, so the result is True.
print(wordDictionary.search("bad"))  # Output: True

# Search for ".ad" in the dictionary
# The "." in the search word acts as a wildcard and can match any character.
# "bad" and "dad" match the pattern ".ad," so the result is True.
print(wordDictionary.search(".ad"))  # Output: True

# Search for "b.." in the dictionary
# The "." in the search word acts as a wildcard and can match any character.
# "bad" matches the pattern "b..," so the result is True.
print(wordDictionary.search("b.."))  # Output: True

"""