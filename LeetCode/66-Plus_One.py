""" Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

    Input: digits = [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.

    Input: digits = [0]
    Output: [1]
"""


class Solution:
    def plusOne(self, digits):
        if digits[-1] == 9:
            tempstr = ''
            for digit in digits:
                tempstr += str(digit)
            tempstr = str(int(tempstr) + 1)
            digits = list(map(int,tempstr))
            return digits
        digits[-1] = digits[-1] + 1
        return digits


obj = Solution()
numarr = [1,2,3]
# numarr = [2,9,9]
print(obj.plusOne(numarr))
        