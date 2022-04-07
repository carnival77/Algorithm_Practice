n,m=map(int,input().split())

ans=-1

a=[list(map(int,input().split())) for _ in range(n)]
c=[[False]*m for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,1,-1]

def dfs(x,y,total,cnt):
    global a,c,ans

    if not 0<=x<n or not 0<=y<m:
        return

    if c[x][y]:
        return

    if cnt==4:
        ans=max(total,ans)
        return

    c[x][y]=True

    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        dfs(nx,ny,total+a[x][y],cnt+1)

    c[x][y]=False

for i in range(n):
    for j in range(m):
        dfs(i,j,0,0)
        if i+2<=n-1:
            tmp=a[i][j]+a[i+1][j]+a[i+2][j]
            if j+1<=m-1:
                tmp2=tmp+a[i+1][j+1]
                ans=max(ans,tmp2)
            if j-1>=0:
                tmp2=tmp+a[i+1][j-1]
                ans=max(ans,tmp2)
        if j+2<=m-1:
            tmp=a[i][j]+a[i][j+1]+a[i][j+2]
            if i+1<=n-1:
                tmp2=tmp+a[i+1][j+1]
                ans=max(ans,tmp2)
            if i-1>=0:
                tmp2=tmp+a[i-1][j+1]
                ans=max(ans,tmp2)

print(ans)