import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=list(map(int,input().split()))

ans=0

a.insert(0,0)
b=[0]*(n+1)
c=[0]*m

for i in range(1,n+1):
    b[i]=b[i-1]+a[i]

for i in range(1,n+1):
    remainder=b[i]%m
    if remainder==0:
        ans+=1
    c[remainder]+=1

for i in range(m):
    if c[i]>0:
        ans+=(c[i]*(c[i]-1)//2)

print(ans)