""" 
Given an array of size N-1 such that it can only contain distinct integers in the range of 1 to N. 
Find the missing element. 
    Input:
    N = 5
    A[] = {1,2,3,5}
    Output: 4
"""

def missing(number,number_list):
    total = (number*(number+1)/2)
    for n in number_list:
        total=int(total-n)
    return total

test_cases = int(input())
for i in range(test_cases):
    noe = int(input())   
    num_list = list(map(int, input().split()))
    print(missing(noe,num_list))