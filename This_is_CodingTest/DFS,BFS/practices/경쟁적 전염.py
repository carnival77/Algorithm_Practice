# 아이디어 1
# 1. board 하나만 존재
# 2. bfs(s,x,y)
# 2-1) bfs. while s loop.
# 2-1-1) 맵 채우기. for i in range(k)
# 2-1-2) board 전체를 탐색하며 i(해당 바이러스 번호) 번째 바이러스를 상하좌우로 확산
#     이 때, 조건 = 해당 칸에 다른 바이러스가 존재 X , 맵 바깥 X
# 2-1-3) return maps[x][y]

# -> 4중 for loop 가 되어서 제한 시간 1초 초과 예정

# 아이디어 2.
# 1. 큐에 (바이러스 종류, 시간, x좌표, y좌표) 삽입 <- 먼저 리스트에 바이러스 정보 담고, 바이러스 종류 순으로 정렬 후 큐에 삽입
# 2. bfs 수행 -> 칸에 바이러스 채우기
# 2_1) while q:
# 2-2) 상하좌우 중 아직 바이러스가 없는 칸(0)에 바이러스 삽입, 그리고 큐에 (바이러스 종류, 시간, x좌표, y좌표) 삽입
# 2-3) 만약 시간이 target_s에 도달하면 멈춤
#

#
from collections import deque

n,k = map(int,input().split())

board=[]
virus = []
for i in range(n):
    board.append(list(map(int,input().split())))
    for j in range(n):
        if board[i][j] != 0:
            virus.append((board[i][j],0,i,j))

q=deque(sorted(virus))

tg_s,tg_x,tg_y= map(int,input().split())

dy = [0,0,-1,1]
dx = [-1,1,0,0]

while q:
    virus,s,x,y = q.popleft()

    if s == tg_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >=0 and nx <= (n-1) and ny <= (n-1):
            if board[nx][ny] == 0:
                board[nx][ny] = virus
                q.append((board[nx][ny],(s+1),nx,ny))

print(board[tg_x-1][tg_y-1])