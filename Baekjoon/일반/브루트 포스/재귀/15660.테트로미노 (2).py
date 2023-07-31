import sys
input=sys.stdin.readline

n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
res=[]
ans=0
c=[[False]*m for _ in range(n)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<m:
        return True
    return False

def dfs(x,y,sum,cnt):
    global ans,res

    if not inBoard(x,y):
        return

    if c[x][y]:
        return

    if cnt==4:
        if sum>=ans:
            ans=sum
            tmp=set()
            for i in range(n):
                for j in range(m):
                    if c[i][j]:
                        tmp.add((i,j))
            res.append([ans,tmp])
        # ans=max(ans,sum)
        return

    c[x][y]=True

    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        dfs(nx,ny,sum+a[x][y],cnt+1)

    c[x][y]=False

def process(x,y):
    global ans,res

    dfs(x, y, 0, 0)
    if y + 2 <= m - 1:
        tmp = a[x][y] + a[x][y + 1] + a[x][y + 2]
        if x + 1 <= n - 1:
            if tmp+a[x + 1][y + 1]>=ans:
                res.append([ans, {(x, y), (x, y + 1), (x, y + 2), (x + 1, y + 1)}])
                ans=tmp+a[x + 1][y + 1]
            # ans = max(ans, tmp + a[x + 1][y + 1])
        if x - 1 >= 0:
            if tmp+a[x - 1][y + 1]>=ans:
                res.append([ans, {(x, y), (x, y + 1), (x, y + 2), (x - 1, y + 1)}])
                ans = tmp+a[x - 1][y + 1]
            # ans = max(ans, tmp + a[x - 1][y + 1])
    if x + 2 <= n - 1:
        tmp = a[x][y] + a[x + 1][y] + a[x + 2][y]
        if y + 1 <= m - 1:
            if tmp+a[x + 1][y + 1]>=ans:
                res.append([ans, {(x, y), (x+1, y), (x+2, y), (x + 1, y + 1)}])
                ans = tmp+a[x + 1][y + 1]
            # ans = max(ans, tmp + a[x + 1][y + 1])
        if y - 1 >= 0:
            if tmp+a[x + 1][y - 1]>=ans:
                res.append([ans, {(x, y), (x+1, y), (x+2, y), (x + 1, y - 1)}])
                ans = tmp+a[x + 1][y - 1]
            # ans = max(ans, tmp + a[x + 1][y - 1])
for x in range(n):
    for y in range(m):
        process(x,y)

res.sort(key=lambda x:-x[0])
ans=0
for i in range(len(res)-1):
    for j in range(i+1,len(res)):
        if res[i]==res[j]:
            continue
        v1,s1=res[i]
        v2,s2=res[j]
        tmp=s1&s2
        if len(tmp)!=0:
            continue
        else:
            ans=max(ans,v1+v2)
            # if ans==35:
            #     print(s1,s2)
            # ans=v1+v2
            # print(ans)
            # sys.exit(0)

print(ans)