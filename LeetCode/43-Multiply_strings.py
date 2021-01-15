""" Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

    Example 1:

    Input: num1 = "2", num2 = "3"
    Output: "6"
    Example 2:

    Input: num1 = "123", num2 = "456"
    Output: "56088"
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        li, lj = len(num1), len(num2)
        i, j = 0, 0
        n1, n2 = 0, 0
        while i < li:
            n1 += (ord(num1[i]) - 48) * (10 ** (li-i-1))
            i += 1
        while j < lj:
            n2 += (ord(num2[j]) - 48) * (10 ** (lj-j-1))
            j += 1
        return str(n1*n2)


obj = Solution()
num1, num2 = "123", "456"
print(obj.multiply(num1,num2))