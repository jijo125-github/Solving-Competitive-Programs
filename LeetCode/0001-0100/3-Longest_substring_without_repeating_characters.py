""" Given a string s, find the length of the longest substring without repeating characters.

    Example 1:

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
    Example 2:

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    Example 3:

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
    Example 4:

    Input: s = ""
    Output: 0
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        limit = len(s) - 1
        i, maxi, ct = 0, 1, 1
        while i < limit:
            temp = s[i]
            for ch in s[i+1:]:
                if ch not in temp:
                    temp += ch
                    ct += 1
                else:
                    if maxi < ct:
                        maxi = ct
                    break
            if len(s[i:]) == ct and maxi < ct:
                maxi = ct
            ct = 1      
            i += 1
        return maxi


obj = Solution()
word = "abcabcbb"
print(obj.lengthOfLongestSubstring(word))