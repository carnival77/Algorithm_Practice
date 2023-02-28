import sys
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

n,m=map(int,input().split())
a=[list(input().strip()) for _ in range(n)]
ans=0

def dfs(x,y,checked,res):
    global ans

    res+=1
    ans=max(ans,res)

    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        if 0<=nx<n and 0<=ny<m:
            nt=a[nx][ny]
            if not checked[ord(nt)-65]:
                checked[ord(nt) - 65] = True
                dfs(nx,ny,checked,res)
                checked[ord(nt) - 65] = False

checked=[False]*26
checked[ord(a[0][0])-65]=True
dfs(0,0,checked,0)

print(ans)