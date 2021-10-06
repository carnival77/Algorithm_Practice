# solution 2. combinations 대신 dfs 사용하여 board의 2 지점들 중 m개를 선택
from collections import deque
import sys

n,m = map(int,input().split())
board=[]
for i in range(n):
    board.append(list(map(int,input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 바이러스가 퍼질 위치 후보
subs=[]
ans=-1

for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            board[i][j]=0
            subs.append((i,j))

def bfs():
    # m개가 선택된 후,
    q=deque()
    # 각 칸에 도달하기 위한 최단 거리를 업데이트한다.
    d=[[-1] * n for _ in range(n)]

    # m개 지점을 큐에 넣는다.
    for i in range(n):
        for j in range(n):
            if board[i][j] == 3:
                q.append((i,j))
                d[i][j]=0

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<n :
                # d로 해당 칸에 방문했는 지 아닌 지 판별
                if board[nx][ny] != 1 and d[nx][ny] == -1:
                    # 그러므로 여기서 board 의 숫자를 바꿀 필요 없다
                    q.append((nx,ny))
                    d[nx][ny] = d[x][y] + 1

    # 이번 bfs의 최소 시간을 cur로
    cur=0
    for i in range(n):
        for j in range(n):
            # 벽이 아닌데, 즉 빈 칸(0) 이거나 바이러스가 있는(3) 칸이면
            if board[i][j] != 1:
                # 그런데 방문하지 않은 칸이 있다면 ans를 -1로 유지하기 위해 return
                if d[i][j] == -1:
                    return
                # 이번 bfs의 최소 시간을 cur로
                if cur < d[i][j]:
                    cur = d[i][j]
    global ans
    # ans 는 모든 cur 중에 최솟값
    if ans == -1 or ans > cur:
        ans=cur


# dfs 로 후보들 중 m개를 고르고, 설치하고(3으로 바꿔서), 다시 부순다(0으로 바꾼다).
def go(index,cnt):
    # index가 모든 후보를 다 탐색했을 때,
    if index == len(subs):
        # 설치된 개수가 m 개일 때
        if cnt == m:
            # 바이러스를 퍼뜨린다
            bfs()
    else:
        x,y = subs[index]
        board[x][y] = 3
        cnt+=1
        go(index+1,cnt)
        board[x][y]=0
        cnt-=1
        go(index+1,cnt)

go(0,0)
print(ans)


# solution 1. combinations 사용 - 어떻게 하는 지 모르겠다. 다시 생각해보자.
# from itertools import combinations
# from collections import deque
# import sys
#
# n,m = map(int,input().split())
# board=[]
# for i in range(n):
#     board.append(list(map(int,input().split())))
#
# temp = [[0] * n for _ in range(n)]
#
# def make_temp(n):
#     for i in range(n):
#         for j in range(n):
#             temp[i][j] = board[i][j]
#
# dx=[-1,1,0,0]
# dy=[0,0,-1,1]
#
# # zeros=[]
# subs=[]
# # ans=[]
# ans=-1
#
# # for i in range(n):
# #     for j in range(m):
# #         if board[i][j] == 0:
# #             zeros.append((i,j))
# #         elif board[i][j] == 2:
# #             twos.append((i,j))
#
# d=[[-1] * n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if board[i][j] == 2:
#             # board[i][j]=0
#             subs.append((i,j))
#
# for sub in combinations(subs,m):
#     q = deque()
#     d = [[-1] * n for _ in range(n)]
#     make_temp(n)
#
#     for i in range(n):
#         for j in range(n):
#             if temp[i][j] == 2:
#                 temp[i][j]=0
#
#     for x,y in sub:
#         # board[x][y]=2
#         temp[x][y]=3
#         q.append((x,y))
#         d[x][y]=0
#
#     while q:
#         x,y = q.popleft()
#         for dir in range(4):
#             nx,ny = x+dx[dir], y+dy[dir]
#             if 0<=nx<n and 0<=ny<n:
#                 if temp[nx][ny]!=1 and d[nx][ny] == -1:
#                     # board[nx][ny] = 2
#                     temp[nx][ny]=2
#                     q.append((nx,ny))
#                     d[nx][ny] = d[x][y]+1
#     # ans.append(max([max(row) for row in d]))
#     cur = 0
#     for i in range(n):
#         for j in range(n):
#             if board[i][j] != 1:
#                 if d[i][j] == -1:
#                     # return
#                     continue
#                 if cur < d[i][j]:
#                     cur = d[i][j]
#     # global ans
#     if ans == -1 or ans > cur:
#         ans = cur
#
#     # for i in range(n):
#     #     for j in range(m):
#     #         if temp[i][j] == 0:
#     #             print(-1)
#     #             sys.exit(0)
#
# print(ans)
# # ans = max([max(row) for row in d])
# # print(min(ans))
#
#
#
# subs = combinations(zeros,3)
#
# ans=0
#
# def bfs(two):
#     q = deque()
#     x,y=two
#     q.append((x,y))
#     while q:
#         x,y = q.popleft()
#         for dir in range(4):
#             nx,ny = x+dx[dir],y+dy[dir]
#             if 0<=nx<n and 0<=ny<n:
#                 if temp[nx][ny] == 0:
#                     temp[nx][ny]=2
#                     q.append((nx,ny))
#
# def safe(n,m):
#     cnt=0
#     for x in range(n):
#         for y in range(m):
#             if temp[x][y] == 0:
#                 cnt+=1
#     return cnt
#
# for sub in subs:
#     make_temp(n,m)
#     point1,point2,point3 = sub
#     x1,y1,x2,y2,x3,y3=point1[0],point1[1],point2[0],point2[1],point3[0],point3[1]
#     temp[x1][y1] = 1
#     temp[x2][y2] = 1
#     temp[x3][y3] = 1
#     for two in twos:
#         bfs(two)
#     cnt = safe(n,m)
#     ans=max(ans,cnt)
#
# print(ans)

