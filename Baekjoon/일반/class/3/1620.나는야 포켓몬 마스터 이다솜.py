import sys
input = sys.stdin.readline

n,m = map(int,input().split())

d=dict()
l=[]

for i in range(n):
    name=input().rstrip()
    d[name]=i+1
    l.append(name)

for i in range(m):
    data=input().rstrip()
    if data.isalpha():
        print(d[data])
    else:
        print(l[int(data)-1])