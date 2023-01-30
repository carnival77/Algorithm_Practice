import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n=int(input())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
ans=[0]*(n+1)

for _ in range(1,n):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(parent):
    visited[parent]=True
    for child in graph[parent]:
        if not visited[child]:
            ans[child]=parent
            dfs(child)

dfs(1)

for i in range(2,n+1):
    print(ans[i])