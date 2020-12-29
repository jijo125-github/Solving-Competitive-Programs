""" 
    Given an integer array and another integer element. The task is to find if the given element is present in array or not.
        Input:
        N = 4
        Arr[] = {1,2,3,4}
        X = 3
        Output: 2
"""


def search(arr, N, X):
    indx = 0
    for value in arr:
        if value == X:
            return indx
        indx += 1
    return -1
            

import math
def main():
        T=int(input())
        while(T>0):
            N=int(input())
            A=[int(x) for x in input().strip().split()]
            x=int(input())
            print(search(A,N,x))
            T-=1


if __name__ == "__main__":
    main()