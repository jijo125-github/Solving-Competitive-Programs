""" Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
    Example 1:

    Input: nums = [1,3,5,6], target = 5
    Output: 2
    Example 2:

    Input: nums = [1,3,5,6], target = 2
    Output: 1
    Example 3:

    Input: nums = [1,3,5,6], target = 7
    Output: 4
    Example 4:

    Input: nums = [1,3,5,6], target = 0
    Output: 0
"""


class Solution:
    def searchInsert(self, nums, target) -> int:
        limit = len(nums)
        if nums[limit-1] < target:
            return limit
        elif nums[0] > target:
            return 0
        i = 0
        while i < limit:
            if nums[i] == target or nums[i] > target:
                return i
            i += 1


obj = Solution()
nums = [1,3,5,6]
target = 5
print(obj.searchInsert(nums, target))