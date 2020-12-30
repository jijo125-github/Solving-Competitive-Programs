'''
	Your task is to check if given linkedlist
	is a palindrome or not.
	
	Function Arguments: head (reference to head of the linked list)
	Return Type: boolean , no need to print just return True or False.

    Input:
    N = 3
    value[] = {1,2,1}
    Output: 1
'''
def isPalindrome(head):
    cur = head
    string = ''
    while cur:
        string += str(cur.data)
        cur = cur.next
    if string == string[::-1]:
        return 1
    return 0
        
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3
#Contributed by : Nagendra Jha

import atexit
import io
import sys

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node 

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list

        if isPalindrome(a.head):
            print(1)
        else:
            print(0)
# } Driver Code Ends