import sys
from collections import Counter
input=sys.stdin.readline

t=int(input())
l1=int(input())
a=list(map(int,input().split()))
l2=int(input())
b=list(map(int,input().split()))
ans=0

x,y=[],[]
for i in range(l1):
    sum=0
    for j in range(i,l1):
        sum+=a[j]
        x.append(sum)
for i in range(l2):
    sum=0
    for j in range(i,l2):
        sum+=b[j]
        y.append(sum)
x.sort()
y.sort()
c=Counter(y)
for i in x:
    ans+=c[t-i]
print(ans)