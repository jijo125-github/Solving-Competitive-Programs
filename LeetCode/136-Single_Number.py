""" Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

    Input: nums = [2,2,1]
    Output: 1

    Input: nums = [1]
    Output: 1
"""


class Solution:
    def singleNumber(self, nums) -> int:
        numdict = dict()
        for num in nums:
            numdict[num] = numdict.get(num,0) + 1
        for key,value in numdict.items():
            if value == 1:
                return key


obj = Solution()
numarr = [2,2,1]
print(obj.singleNumber(numarr))