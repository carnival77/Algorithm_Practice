import sys
from itertools import combinations
from collections import deque

input=sys.stdin.readline
MAX=int(1e9)
ans=MAX

n=int(input())
value=[0]+list(map(int,input().split()))
vertex=[i for i in range(1,n+1)]

graph=[[] for _ in range(n+1)]

for i in range(1,n+1):
    row=list(map(int,input().split()))
    for j in row[1:]:
        graph[i].append(j)

def bfs(start,arr):
    res=[start]
    q=deque()
    q.append(start)
    while q:
        v=q.popleft()
        for next_v in graph[v]:
            if next_v not in res and next_v in arr:
                res.append(next_v)
                q.append(next_v)
    return res

def check(a):
    if set(a)==set(bfs(a[0],a)):
        return True
    return False

def process(first,second):
    if check(first) and check(second):
        return abs(sum(value[i] for i in first) - sum(value[i] for i in second))
    else:
        return MAX

for no in range(1,n):
    for comb in combinations(vertex,no):
        first=set(comb)
        second=set(vertex)-first
        ans=min(ans,process(list(first),list(second)))

if ans==MAX:
    print(-1)
else:
    print(ans)