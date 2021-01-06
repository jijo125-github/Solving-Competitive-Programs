""" Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space. 

    Example 1:

    Input: s = "the sky is blue"
    Output: "blue is sky the"

    Example 3:

    Input: s = "a good   example"
    Output: "example good a"
    Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.strip().split()[::-1])


obj = Solution()
sentence = "a good   example"
print(obj.reverseWords(sentence))