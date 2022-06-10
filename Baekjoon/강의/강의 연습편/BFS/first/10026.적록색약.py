from collections import deque

n=int(input())
a=[list(list(input())) for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def can(blind,a,b):
    if a==b:
        return True
    if blind:
        if (a=='R' and b=='G') or (b=='R' and a=='G'):
            return True
    return False

def bfs(blind):
    ans=0
    check = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not check[i][j]:
                q=deque()
                q.append((i, j))
                check[i][j]=True
                c=a[i][j]
                while q:
                    x,y=q.popleft()
                    for k in range(4):
                        nx,ny=x+dx[k],y+dy[k]
                        if 0<=nx<n and 0<=ny<n and not check[nx][ny]:
                            if can(blind,a[i][j],a[nx][ny]):
                                q.append((nx,ny))
                                check[nx][ny]=True
                ans+=1
    return ans

ans1=bfs(False)
ans2=bfs(True)
ans=[ans1,ans2]
print(*ans)