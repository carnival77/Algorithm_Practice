# 풀이 시간 : 약 1시간 30분

# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

dx=[-1,0,1,0]
dy=[0,-1,0,1]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

def bfs(sx,sy,a):
    global ans

    q=deque()
    q.append((sx,sy))
    dist=[[-1]*n for _ in range(n)]
    dist[sx][sy]=0
    longest=0

    while q:
        i,j=q.popleft()
        for k in range(4):
            nx,ny=i+dx[k],j+dy[k]
            # if inBoard(nx,ny) and dist[nx][ny]==-1 and a[nx][ny]<a[i][j]:
            if inBoard(nx,ny) and a[nx][ny]<a[i][j]:
                q.append((nx,ny))
                dist[nx][ny]=dist[i][j]+1
                longest=max(longest,dist[nx][ny])

    # for i in range(n):
    #     for j in range(n):
    #         longest=max(longest,dist[i][j])

    return longest

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for t in range(1, T + 1):
    n,m=map(int,input().split())
    a=[list(map(int,input().split())) for _ in range(n)]

    ans=0

    # 가장 높은 봉우리 찾기
    high = []
    highest = 0
    for i in range(n):
        for j in range(n):
            highest = max(highest, a[i][j])
    for i in range(n):
        for j in range(n):
            if a[i][j] == highest:
                high.append([i, j])
    # 2차원 맵 탐색하며
    for x in range(n):
        for y in range(n):
            # 한 곳씩 1~m만큼 깎아보기
            for z in range(m+1):
                if a[x][y]-z<0:continue
                a[x][y]-=z
                # flag1=0
                # 가장 높은 봉우리에서
                for sx,sy in high:
                    # 최대 길이 등산로 찾기
                    res=bfs(sx,sy,a)+1
                    ans=max(ans,res)
                # 깎은 것 원복
                a[x][y]+=z

    print("#"+str(t),ans)