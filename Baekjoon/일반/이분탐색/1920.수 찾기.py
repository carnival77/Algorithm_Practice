import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

a=set(a)

for i in b:
    if i in a:
        print(1)
    else:
        print(0)