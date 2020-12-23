""" to check if two strings are anagram of each other """

def anagram(str1,str2):
	l1 = len(str1)
	l2 = len(str2)
	for c in str1:
		if (l1 == l2 and c not in str2) or l1 != l2:
			return "no"
	return "yes"


testcases = int(input())
for _ in range(testcases):
	str1, str2 = map(str,input().split())
	print(anagram(str1,str2))