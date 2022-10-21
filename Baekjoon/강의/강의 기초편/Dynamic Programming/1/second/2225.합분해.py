n,k=map(int,input().split())
mod = 1000000000
d = [[0]*(n+1) for _ in range(k+1)] # 0부터 n까지의 정수 k개를 써서 n을 만드는 경우의 수
# d[n][k]=시그마(d[n-i][k-1]) (0<=i<=n)
d[0][0]=1

for i in range(1, k+1):
    for j in range(0, n+1):
        for l in range(0, j+1):
            d[i][j] += d[i-1][j-l]
        d[i][j] %= mod

print(d[k][n])