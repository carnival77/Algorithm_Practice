import sys
input=sys.stdin.readline

INF=int(1e9)

n,m=map(int,input().split())
graph=[[INF] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

for _ in range(m):
    x,y=map(int,input().split())
    graph[x][y]=1
    graph[y][x]=1

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

res=[]
for i in range(1,n+1):
    row_sum=0
    for j in range(1,n+1):
        if graph[i][j]!=INF:
            row_sum+=graph[i][j]
    res.append([row_sum,i])
res.sort()
# print(res)
ans=res[0][1]
print(ans)