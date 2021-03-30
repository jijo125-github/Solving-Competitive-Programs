""" Given a string s consists of some words separated by spaces, return the length of the last word in the string. 
If the last word does not exist, return 0.

    Input: s = "Hello World"
    Output: 5

    Input: s = " "
    Output: 0
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s.strip()) > 0:
            return len(s.split()[-1])
        return 0


obj = Solution()
word = "Hello World"
# word = " "
print(obj.lengthOfLastWord(word))