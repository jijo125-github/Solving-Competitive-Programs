""" 
Given an expression string x. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.

Input: {([])}
Output: true

Input: ([]
Output: false
"""

class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        return self.items.append(item)
        
    def pop(self):
        if not len(self.items) == 0:
            return self.items.pop()
        return -1

def is_check_open_closed_correct(ch1, ch2):
    if ch1 == '{' and ch2 == '}':
        return True
    elif ch1 == '(' and ch2 == ')':
        return True
    elif ch1 == '[' and ch2 == ']':
        return True
    return False
    
def parenthesis_checker(string):
    balanced = True
    stack = Stack()
    valid_open_characters = ['{', '(', '[']
    valid_close_characters = ['}', ')', ']']
    for character in string:
        if character in valid_open_characters:
            stack.push(character)
        elif character in valid_close_characters:
            last_stack_character = stack.pop()
            if not is_check_open_closed_correct(last_stack_character, character):
                return "not balanced"
    if balanced and len(stack.items) == 0:
        return "balanced"
    return "not balanced"
                
        
testcases = int(input())
for testcase in range(testcases):
    string_of_expression = input()
    print(parenthesis_checker(string_of_expression))