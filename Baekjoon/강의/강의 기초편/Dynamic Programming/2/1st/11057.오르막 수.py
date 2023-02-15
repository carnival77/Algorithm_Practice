# 해설 : https://carnival.tistory.com/71

n=int(input())

d=[[0]*10 for _ in range(n+1)]

mod=10007

for i in range(1,n+1):
    for j in range(10):
        if i==1:
            d[i][j]=1
        else:
            for k in range(j+1):
                d[i][j] += d[i-1][k]
        d[i][j]%=mod

ans=0
for j in range(10):
    ans+=d[n][j]

print(ans%mod)