""" Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

    Input: nums = [2,2,1,1,1,2,2]
    Output: 2
"""


class Solution:
    def majorityElement(self, nums) -> int:
        n = len(nums) / 2
        numdict = dict()
        for num in nums:
            numdict[num] = numdict.get(num,0) + 1
        for key,value in numdict.items():
            if value > n:
                return key


obj = Solution()
numarr = [2,2,1,1,1,2,2]
print(obj.majorityElement(numarr))