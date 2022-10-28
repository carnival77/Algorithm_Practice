n=int(input())
d=[[0]*10 for _ in range(n+1)] # d[i][j]=i 자리가 j로 끝나는 오름차순 수의 개수
# d[i][j]=d[i][j-1]+d[i-1][j] (1<=i<=n, 1<=j<=9)
mod=10007
for i in range(10):
    d[1][i]=1
for i in range(1,n+1):
    d[i][0]=1

for i in range(1,n+1):
    for j in range(1,10):
        d[i][j]=d[i][j-1]+d[i-1][j]
        d[i][j]%=mod
print(sum(d[n])%mod)