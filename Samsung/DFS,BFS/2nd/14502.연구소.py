from collections import deque
from itertools import combinations
import copy

n,m= map(int,input().split())

a=[list(map(int,input().split())) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

answer=0

virus=[]
zeros=[]

# 바이러스 퍼뜨리기
def bfs(v,temp_a):

    # count=0

    q=deque()
    q.append(v)

    while q:
        x,y=q.popleft()
        temp_a[x][y]=2

        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]

            if 0<=nx<n and 0<=ny<m:
                if temp_a[nx][ny] != 0:
                    continue
                else:
                    q.append((nx,ny))

    return temp_a

# 바이러스 위치 파악
# 빈 칸 찾기
for i in range(n):
    for j in range(m):
        if a[i][j] == 2:
            virus.append([i,j])
        elif a[i][j] == 0:
            zeros.append([i,j])

# 벽 세우기
for targets in combinations(zeros,3):
    count=0
    temp_a = copy.deepcopy(a)
    for x,y in targets:
        temp_a[x][y] = 1

    for v in virus:
        temp_a = bfs(v,temp_a)

    for i in range(n):
        for j in range(m):
            if temp_a[i][j] == 0:
                count+=1

    answer = max(answer, count)

print(answer)