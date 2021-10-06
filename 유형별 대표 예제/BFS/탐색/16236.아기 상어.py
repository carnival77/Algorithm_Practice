# 1. d를 통해 최단 거리를 지속적으로 업데이트한다.
# 2. ok, eat flag를 통해 각 조건들의 경우를 다룬다.
# 3. 요소 3개의 sort를 sort()를 사용해 dist, x, y 순으로 내림차순한다.
# 4. bfs로 물고기를 한마리씩 잡는다. bfs와 time을 세기 위한 while문을 잘 분리했다.

from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(a, x, y, size):
    n = len(a)
    ans = []
    d = [[-1]*n for _ in range(n)]
    q = deque()
    q.append((x,y))
    d[x][y] = 0
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if 0 <= nx < n and 0 <= ny < n and d[nx][ny] == -1:
                ok = False
                eat = False
                # 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다.
                if a[nx][ny] == 0:
                    ok = True
                elif a[nx][ny] < size: # 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다.
                    ok = True
                    eat = True
                elif a[nx][ny] == size: # 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
                    ok = True
                if ok:
                    q.append((nx,ny))
                    d[nx][ny] = d[x][y] + 1
                    if eat:
                        ans.append((d[nx][ny],nx,ny))
    if not ans:
        return None
    ans.sort()
    return ans[0]

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
x,y = 0,0
for i in range(n):
    for j in range(n):
        if a[i][j] == 9:
            x,y = i,j
            a[i][j] = 0
ans = 0
size = 2
exp = 0
while True:
    p = bfs(a, x, y, size)
    if p is None:
        break
    dist, nx, ny = p
    a[nx][ny] = 0
    ans += dist
    exp += 1
    if size == exp:
        size += 1
        exp = 0
    x,y = nx,ny
print(ans)

# from collections import deque
#
# n=int(input())
# board=[]
# for i in range(n):
#     board.append(list(map(int,input().split())))
# fish_q=deque() # 잡을 물고기들의 위치
# dx=[-1,0,1,0]
# dy=[0,-1,0,1]
# time=0
# size=(2,0) # (현 사이즈, 먹은 물고기 수)
# x,y=0,0 # 현재 위치.
#
#
#
# # 먹은 수만큼 size 증가
# def upgrade(size):
#     if size[1] == size[0]:
#         a,b = size
#         a+=1
#         b=0
#         size = (a,b)
#         # size[0] +=1
#         # size[1] = 0
#     return size
#
# # 물고기 1마리씩 타겟 삼아 잡기
# def bfs(fish_q,x,y):
#     global time,size
#     # 보드 내 칸까지의 거리. 초기값 0이고 0이면 아직 방문 X
#     dist=list([0] * n for _ in range(n))
#     tx,ty = fish_q.popleft()
#     q=deque()
#     q.append((x,y))
#     while q:
#         x,y=q.popleft()
#         for k in range(4):
#             nx=x+dx[k]
#             ny=y+dy[k]
#             # 범위 내라면
#             if 0<=nx<n and 0<=ny<n:
#                 # 아직 가보지 않은 곳이고 해당 칸의 물고기의 사이즈가 상어 현 사이즈보다 작거나 같다면
#                 if dist[nx][ny] == 0 and size[0] >= board[nx][ny]:
#                     dist[nx][ny] = dist[x][y] + 1
#                     q.append((nx,ny))
#     a,b = size
#     size = (a,b+1)
#     size=upgrade(size)
#     time+=dist[tx][ty]
#
#     board[tx][ty] = 0
#
#     return tx,ty
#
# def bfs_2(fish_q,x,y):
#     # 가장 위, 왼쪽에 있는 물고기 순으로 정렬. -> x,y 중 x 우선으로 내림차순 정렬
#     fishes=sorted(list(fish_q),key=lambda x:(-x[0],-x[1]))
#     for fish in fishes:
#         q=deque()
#         tx,ty = fish
#         q.append((tx,ty))
#         x,y = bfs(q,x,y)
#
#
# def process(fish_q,x,y):
#     # 대상 물고기 수
#     n=len(fish_q)
#     #먹을 수 있는 물고기가 1마리
#     if n==1:
#         x,y = bfs(fish_q,x,y)
#     elif n>1:
#         bfs_2(fish_q,x,y)
#
# while True:
#     # 맵 체크해서 현재 목표 물고기 장바구니
#     for i in range(n):
#         for j in range(n):
#             # 현재 사이즈보다 작은 물고기가 있는 칸이면
#             if 1<=board[i][j]<size[0]:
#                 # 목표로 설정하여 해당 칸 위치 큐에 담기
#                 fish_q.append((i,j))
#             # 현재 상어 위치 판별
#             elif board[i][j] == 9:
#                 x,y=i,j
#     # 더 이상 먹을 물고기 x
#     if len(fish_q) == 0:
#         break
#
#     # 먹을 물고기 있다면
#     else:
#         process(fish_q,x,y)
#
# print(time)
#
