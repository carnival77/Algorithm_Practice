from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]
t=int(input())
for _ in range(t):
    m,n,k=map(int,input().split())
    a=[[0]*(m) for _ in range(n)]
    ans=0

    for _ in range(k):
        x,y=map(int,input().split())
        a[y][x]=1

    for i in range(n):
        for j in range(m):
            if a[i][j]==1:
                ans+=1
                a[i][j]=2
                q=deque()
                q.append((i,j))
                while q:
                    x,y=q.popleft()
                    for k in range(4):
                        nx,ny=x+dx[k],y+dy[k]
                        if 0<=nx<n and 0<=ny<m and a[nx][ny]==1:
                            q.append((nx,ny))
                            a[nx][ny]=2

    print(ans)