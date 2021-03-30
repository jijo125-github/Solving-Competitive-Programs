""" Given an integer array nums where every element appears three times except for one, which appears exactly once.
Find the single element and return it.
    Example 1:

    Input: nums = [2,2,3,2]
    Output: 3
    Example 2:

    Input: nums = [0,1,0,1,0,1,99]
    Output: 99
"""


class Solution:
    def singleNumber(self, nums) -> int:
        number_dict = dict()
        for num in nums:
            number_dict[num] = number_dict.get(num,0) + 1
        for key, value in number_dict.items():
            if value == 1:
                return key


obj = Solution()
numarr = [0,1,0,1,0,1,99]
print(obj.singleNumber(numarr))