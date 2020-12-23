""" Reverse words in a given string 

ex : i.like.this.program.very.much
ans: much.very.program.this.like.i """


def rever(sent):
    rev = [word for word in sent.split('.')[::-1]]
    return '.'.join(rev)
        
testcases = int(input())
for _ in range(testcases):
    sentence = '.'.join(input().split())
    print(rever(sentence))