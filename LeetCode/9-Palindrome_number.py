""" Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same backward as forward.

Example:
Input: x = 121
Output: true """

""" Solution below """


def is_palindrome(x):
    number = str(abs(x))
    return int(number[::-1]) == x


print(is_palindrome(121))