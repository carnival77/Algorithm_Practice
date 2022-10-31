import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
m=int(input())

d=[[0]*(n) for _ in range(n)]

# length=수열의 길이
# length = 1,2 # 길이가 1인 수열과 같은 두 개의 수로 이루어진 수열은 팰린드롬
for i in range(n):
    d[i][i]=1
for i in range(n-1):
    if a[i]==a[i+1]:
        d[i][i+1] = 1

# length >= 3 # 양쪽 맨 끝의 수가 같고 안쪽 수열이 팰린드롬이면 팰린드롬
for k in range(3,n+1):
    for i in range(n-k+1):
        j=k+i-1
        if a[i]==a[j] and d[i+1][j-1]==1:
            d[i][j]=1

for _ in range(m):
    s,e=map(int,input().split())
    print(d[s-1][e-1])