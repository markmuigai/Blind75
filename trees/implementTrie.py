"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 

Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
"""


class TrieNode:
    def __init__(self):
        # Initialize a TrieNode with an empty dictionary to store children nodes.
        self.children = {}
        # Initialize a boolean flag to mark the end of a word.
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        # Initialize a Trie object with an empty root node, which is a TrieNode.
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Start at the root node.
        node = self.root
        for char in word:
            # Check if the current character is not in the children of the current node.
            if char not in node.children:
                # Create a new TrieNode for the character and add it to the children dictionary.
                node.children[char] = TrieNode()
            # Move to the next node (character).
            node = node.children[char]
        # Mark the last node as the end of a word.
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        # Start at the root node.
        node = self.root
        for char in word:
            # Check if the current character is not in the children of the current node.
            if char not in node.children:
                # The word does not exist in the Trie.
                return False
            # Move to the next node (character).
            node = node.children[char]
        # Check if the last node is marked as the end of a word.
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        # Start at the root node.
        node = self.root
        for char in prefix:
            # Check if the current character is not in the children of the current node.
            if char not in node.children:
                # The prefix does not exist in the Trie.
                return False
            # Move to the next node (character).
            node = node.children[char]
        # The prefix exists in the Trie.
        return True

"""
Certainly! Let's walk through how the Trie data structure works using an example:

Example:

Suppose we want to insert the words "apple," "app," and "bat" into the Trie and perform some operations on it.

Initialize an empty Trie:

We create an empty root node.
Insert "apple" into the Trie:

Start at the root node.
For each character in "apple," create a new TrieNode if it doesn't exist in the children dictionary.
Mark the last node as the end of a word.
Trie Structure
 root
  |
  a
  |
  p
  |
  p
  |
  l
  |
  e (End of Word)
Search for "apple" in the Trie:

Start at the root node.
For each character in "apple," follow the path in the Trie.
Check if the last node is marked as the end of a word.
Result: "apple" is found, so return True.
Search for "app" in the Trie:

Start at the root node.
For each character in "app," follow the path in the Trie.
Check if the last node is marked as the end of a word.
Result: "app" is not found, so return False.
Check if a word with the prefix "app" exists in the Trie:

Start at the root node.
For each character in the prefix "app," follow the path in the Trie.
Result: A word with the prefix "app" exists (i.e., "apple" is a word in the Trie), so return True.
Insert "bat" into the Trie:

Start at the root node.
For each character in "bat," create a new TrieNode if it doesn't exist in the children dictionary.
Mark the last node as the end of a word.
Trie Structure:

css
Copy code
  root
  |
  a
  |
  p
  |
  p
  |
  l
  |
  e (End of Word)
  |
  b
  |
  a
  |
  t (End of Word)
Search for "bat" in the Trie:

Start at the root node.
For each character in "bat," follow the path in the Trie.
Check if the last node is marked as the end of a word.
Result: "bat" is found, so return True.
Check if a word with the prefix "ba" exists in the Trie:

Start at the root node.
For each character in the prefix "ba," follow the path in the Trie.
Result: A word with the prefix "ba" exists (i.e., "bat" is a word in the Trie), so return True.
This walk-through demonstrates how the Trie data structure efficiently stores and retrieves words and prefixes, making it useful for applications like autocomplete and spellchecking.
"""