import sys
input=sys.stdin.readline

n,k=map(int,input().split())
ans=0
coins=[]
for i in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

for coin in coins:
    a=k//coin
    if a>=1:
        ans+=a
        k-=a*coin

print(ans)