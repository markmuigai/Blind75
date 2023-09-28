"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word. Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
"""

class TrieNode:
    def __init__(self):
        # Initialize a TrieNode with an empty dictionary to store children nodes.
        self.children = {}
        # Initialize a flag to mark the end of a word.
        self.is_end_of_word = False

class Solution:
    def findWords(self, board, words):
        # Define a Trie data structure for efficient word lookup.
        trie = TrieNode()
        
        # Build the Trie by inserting each word from the given list.
        for word in words:
            node = trie
            for char in word:
                if char not in node.children:
                    # If the character is not in the children of the current node, create a new node for it.
                    node.children[char] = TrieNode()
                # Move to the next node (character).
                node = node.children[char]
            # Mark the last node as the end of the word.
            node.is_end_of_word = True
        
        # Define a set to store the found words.
        found_words = set()
        
        def backtrack(node, r, c, path):
            char = board[r][c]
            curr_node = node.children.get(char)
            word = path + char

            if curr_node and curr_node.is_end_of_word:
                # If the current node marks the end of a word, add it to the found words set.
                found_words.add(word)

            # Mark the current cell as visited by changing the character to '#'.
            board[r][c] = '#'

            # Define directions for exploring adjacent cells (up, down, left, right).
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] != '#':
                    # Check if the adjacent cell is within bounds and hasn't been visited.
                    # Also, ensure that the character exists in the Trie to continue the word.
                    backtrack(curr_node, nr, nc, word)

            # After exploring all paths from the current cell, backtrack by marking it as unvisited.
            board[r][c] = char

        # Iterate through all cells on the board and call the backtrack function for each cell.
        for r in range(len(board)):
            for c in range(len(board[0])):
                start_char = board[r][c]
                if start_char in trie.children:
                    # If the starting character exists in the Trie, begin exploring words from this cell.
                    backtrack(trie, r, c, "")

        # Convert the set of found words to a list and return it as the result.
        return list(found_words)

"""
Certainly! Let's walk through how the algorithm works step by step using the example input:

Input:

python
Copy code
board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"]
]
words = ["oath", "pea", "eat", "rain"]
Build the Trie:

Create an empty Trie data structure.
Insert each word from the words list into the Trie.
Trie Structure:

root
|
o - a - t - h (End of Word)
|   |
|   t - h (End of Word)
|   |
|   h (End of Word)
|
p - e - a (End of Word)
|
e - a - t (End of Word)
|     |
|     h (End of Word)
|     |
|     e - a - t (End of Word)
|
r - a - i - n (End of Word)
Initialize an empty set to store found words (found_words).

Iterate through each cell on the board:

Start from each cell as the beginning of a word.
Check if the starting character exists in the Trie.
Perform backtracking:

Explore adjacent cells (up, down, left, right) to form words.
Mark visited cells with "#" to prevent reusing characters in the same word.
If a valid word is formed during backtracking and exists in the Trie, add it to the found_words set.

Continue backtracking and exploration for all possible words on the board.

After exploring all cells and backtracking, convert the found_words set to a list and return it as the result.

Result:
The words "eat" and "oath" are found on the board, and they are returned as the output.

Output:

css
Copy code
["eat", "oath"]
In summary, the algorithm builds a Trie to efficiently search for words on the board. It explores the board using backtracking and marks visited cells to ensure each character is used at most once in a word. Found words are added to the found_words set, and the final list of found words is returned as the result.
"""