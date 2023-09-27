"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods (such as eval).

 

Example 1:

Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
Example 2:

Input: dummy_input = [""]
Output: [""]
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] contains any possible characters out of 256 valid ASCII characters.
 

Follow up: Could you write a generalized algorithm to work on any possible set of characters?
"""

class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string."""
        encoded_string = ""
        for s in strs:
            # To handle empty strings, we prepend the length of each string before the actual string.
            encoded_string += str(len(s)) + '/' + s
        return encoded_string

    def decode(self, s):
        """Decodes a single string to a list of strings."""
        decoded_strings = []
        i = 0
        while i < len(s):
            # Find the position of the delimiter '/' to determine the length of the next string.
            delimiter_pos = s.find('/', i)
            if delimiter_pos == -1:
                # If no delimiter is found, break the loop.
                break
            # Get the length of the string.
            length = int(s[i:delimiter_pos])
            # Update the starting position to the character after the delimiter.
            i = delimiter_pos + 1
            # Extract the string based on the length.
            decoded_strings.append(s[i:i + length])
            # Update the starting position for the next iteration.
            i += length
        return decoded_strings

# Example usage:
encoder = Codec()
decoder = Codec()

# Encoding a list of strings
strs = ["Hello", "World"]
encoded_string = encoder.encode(strs)
print(encoded_string)  # Output: "5/Hello5/World"

# Decoding the encoded string
decoded_strings = decoder.decode(encoded_string)
print(decoded_strings)  # Output: ["Hello", "World"]

"""
In the encode method:

We iterate through each string in the input list strs.
For each string, we prepend its length followed by a delimiter ('/') to the encoded_string.
This way, we can later extract the length and string during decoding.
In the decode method:

We initialize an empty list decoded_strings to store the decoded strings.
We iterate through the encoded string s and use the delimiter ('/') to separate the length and string.
We extract the length and convert it to an integer to determine the length of the next string.
We extract the string of the specified length and add it to the decoded_strings list.
We continue this process until we have processed the entire encoded string.
"""