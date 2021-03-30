""" 
The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn. 

    nput: n = 4
    Output: 4

    Explanation:
    T_3 = 0 + 1 + 1 = 2
    T_4 = 1 + 1 + 2 = 4
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        a,b,c,i = 0,0,1,1
        while i < n:
            a,b,c = b,c,a+b+c
            i += 1
        return c


obj = Solution()
print(obj.tribonacci(4))