import sys
input=sys.stdin.readline

n=int(input())
INF=int(1e9)

graph=[[INF]*n for _ in range(n)]

for i in range(n):
    row=list(map(int,input().split()))
    for j in range(len(row)):
        if row[j]==1:
            graph[i][j]=1
        if i==j:
            graph[i][j]=INF
# print(graph)

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
# print(graph)
for i in range(n):
    for j in range(n):
        if graph[i][j]==INF:
            graph[i][j]=0
        else:
            graph[i][j]=1

for row in graph:
    print(*row)