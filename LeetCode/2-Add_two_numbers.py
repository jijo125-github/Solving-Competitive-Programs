""" You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]
"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
            
        num2 = ''
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
            
        answer = str(int(num1[::-1]) + int(num2[::-1]))[::-1]
        head = cur = ListNode(0)
        for digit in answer:
            cur.next = ListNode(digit)
            cur = cur.next
            
        return head.next