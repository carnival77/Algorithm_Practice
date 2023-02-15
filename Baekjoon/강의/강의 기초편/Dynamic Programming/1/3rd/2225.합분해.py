n,k= map(int,input().split())

# d=[[0] * (n+1) for _ in range(k+1)]
d=[[0] * (k+1) for _ in range(n+1)]

d[0][0]=1

mod=1000000000

# for i in range(1,k+1):
#     for j in range(0,n+1):
#         for l in range(0,j+1):
#             d[i][j]+=d[i-1][j-l]
#         d[i][i]%=mod
#
# print(d[k][n])

for j in range(1,k+1):
    for i in range(n+1):
        for x in range(i+1):
            d[i][j]+=d[x][j-1]
        d[i][j]%=mod

print(d[n][k])