import sys
input=sys.stdin.readline

n,k=map(int,input().split())
a=[]
for i in range(n):
    a.append(len(input().strip()))
m=k+1
b=[0]*21
ans=0

for i in range(m):
    ans+=b[a[i]]
    b[a[i]]+=1

for end in range(m,n):
    start=end-m
    b[a[start]]-=1
    ans+=b[a[end]]
    b[a[end]]+=1

print(ans)