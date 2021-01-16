""" Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

    Example 1:

    Input
    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]

    Output
    [null,null,null,null,-3,null,0,-2]

    Explanation
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin(); // return -3
    minStack.pop();
    minStack.top();    // return 0
    minStack.getMin(); // return -2
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        

    def push(self, x: int) -> None:
        if not self.items:
            self.items.append((x,x))
        else:
            self.items.append((x, min(x,self.items[-1][-1])))

    def pop(self) -> None:
        if self.items:
            self.items.pop()
        

    def top(self) -> int:
        if not self.items:
            return None
        return self.items[-1][0]
        

    def getMin(self) -> int:
        if not self.items:
            return None
        return self.items[-1][-1]
        

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())