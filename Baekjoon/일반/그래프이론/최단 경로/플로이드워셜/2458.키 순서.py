# 플로이드-와샬 알고리즘을 통해서 i j가 연결되어 있는지 여부를 조사하고
# 각 숫자마다 연결된 노드의 개수가 N - 1이라면 자신의 키가 몇 번째인지 알 수 있다.
import sys
input=sys.stdin.readline
INF=int(1e9)
ans=0

n,m=map(int,input().split())

graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if graph[a][k]==1 and graph[k][b]==1:
                graph[a][b]=1

for i in range(1,n+1):
    check=0
    for j in range(1,n+1):
        if graph[i][j]==1:
            check+=1
        if graph[j][i]==1:
            check+=1
    if check==n-1:
        ans+=1
print(ans)