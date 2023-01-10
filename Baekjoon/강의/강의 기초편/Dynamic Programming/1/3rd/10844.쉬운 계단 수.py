n=int(input())
mod=1000000000
d=[[0]*10 for _ in range(n+1)]
for i in range(1,10):
    d[1][i]=1

for i in range(2,n+1):
    for j in range(10):
        if j==0:
            d[i][j]=d[i-1][1]
        elif 1<=j<=8:
            d[i][j]=d[i-1][j-1]+d[i-1][j+1]
        else:
            d[i][j]=d[i-1][j-1]
        d[i][j]%=mod

print(sum(d[n])%mod)