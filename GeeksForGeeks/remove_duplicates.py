""" 
  Given a string without spaces, the task is to remove duplicates from it.
    Input: S = "geeksforGeeks"
    Output: geksfor
"""


def dup(sent):
  uniq = []
  for char in sent:
    if char not in uniq:
      uniq.append(char)
  return ''.join(uniq)

testcases = int(input())
for _ in range(testcases):
	sentence = input().lower()
	print(dup(sentence))