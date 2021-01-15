""" Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
    
    Example 1:

    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
    Example 2:

    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]
"""


class Solution:
    def searchRange(self, nums, target):
        length = len(nums)
        if length == 1 and target == nums[0]:
            return [0,0]
        i, j = 0, length - 1
        first_pos, last_pos = True, True
        answer = [-1,-1]
        while i < length:
            if nums[i] == target and first_pos:
                answer[0] = i
                first_pos = False
            if nums[j] == target and last_pos:
                answer[-1] = j
                last_pos = False
            if first_pos is False and last_pos is False:
                return answer
            i += 1
            j -= 1
        return answer


obj = Solution()
numarr = [5,7,7,8,8,10]
target = 8
print(obj.searchRange(numarr,target))