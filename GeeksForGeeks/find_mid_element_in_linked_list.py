""" Given a singly linked list of N nodes. The task is to find the middle of the linked list. 
For example, if given linked list is 1->2->3->4->5 then the output should be 3. """


def findMid(head):
    cur_node = head
    total = 0
    while cur_node:
        cur_node = cur_node.next
        total += 1
        
    cur_node = head
    mid = (total // 2) + 1
    key = 1
    while key != mid:
        cur_node = cur_node.next
        key += 1
    return cur_node.data
    
  
class node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
            self.tail = self.head
        else:
            new_node = node(val)
            self.tail.next = new_node
            self.tail = self.tail.next


def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head = createList(arr, n)
        print(findMid(head))