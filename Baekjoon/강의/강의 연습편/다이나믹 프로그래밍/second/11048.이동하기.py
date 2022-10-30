n,m=map(int,input().split())

d=[[0]*m for _ in range(n)]
a=[list(map(int,input().split())) for _ in range(n)]
d[0][0]=a[0][0]

for i in range(n):
    for j in range(m):
        if 0<=i+1<n:
            d[i+1][j]=max(d[i+1][j],d[i][j]+a[i+1][j])
        if 0<=j+1<m:
            d[i][j+1]=max(d[i][j+1],d[i][j]+a[i][j+1])
        if 0<=i+1<n and 0<=j+1<m:
            d[i+1][j+1]=max(d[i+1][j+1],d[i][j]+a[i+1][j+1])

print(d[n-1][m-1])