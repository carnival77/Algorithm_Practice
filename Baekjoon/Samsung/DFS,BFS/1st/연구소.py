# # 아이디어
# #
# # 1. 3개의 벽을 설치하는 모든 경우의 수를 계산한다.
# # 2. 각각의 경우의 수에서의 맵에서 바이러스 확산 결과 남은 안전지역 개수를 구한다.
# # 3. 모든 경우의 수 중 안전지역 개수가 최대인 경우의 안전지역 개수를 반환한다.
# #
# #
# # 1-1) n * m 개의 칸에서 현재 존재하는 벽의 개수를 빼고, 나머지 칸에서 벽을 설치할 3개의 칸을 조합으로 고른다
# # 1-1-1) 조합에 들어갈 리스트는?: (x,y) 좌표값으로 지정한다.
# # 1-1-3) 전체 칸에서 0인 칸을 따로 저장한다.
# # 1-1-4) 이 0인 칸의 리스트가 조합에 쓰일 리스트이다.
# #
# # 2-1) 1의 루프 안에서, 각 경우의 수에 뽑힌 3개의 0인 칸에 1을 넣는다.
# # 2-2) 남아있는 0인 칸에서 각 2를 DFS를 돌린다.
# # 2-3) DFS는 2가 존재하면 나머지 칸들도 2로 만드는 것이다.
# # 2-4) 여기서, 범위 설정은
# # 2-4-1) 2의 상하좌우에 맵의 끝이 있거나, 1이 존재하면 DFS는 진행되지 못한다.
# # 2-5) 2의 DFS 가 모두 진행된 후, 맵에서 남은 0의 개수를 구한다.
# # 2-6) 이 것을 safe라고 하며, min(safe,this_safe)로 하여 모든 경우의 수를 고려할 때 safe의 최솟값을 구한다.
# from itertools import combinations
#
# def insert_wall(r,c,temp_board):
#     global n,m
#     for i in range(n):
#         for j in range(m):
#             if i == r and j == c:
#                 temp_board[i][j] = 1
#     return temp_board
#
#
# n,m = map(int,input().split())
#
# board = []
# zeros = []
# virus_list=[]
#
# dy = [0,0,-1,1]
# dx = [-1,1,0,0]
#
# def dfs(virus,board):
#     x,y=virus
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if nx>(n-1) or ny>(m-1) or nx<0 or ny<0:
#             continue
#         if board[x][y] == 0:
#             board[x][y] = 2
#             dfs([x-1,y])
#             dfs([x + 1, y])
#             dfs([x , y - 1])
#             dfs([x, y + 1])
#             return board
#     return board
#
#
# # 1-1) n * m 개의 칸에서 현재 존재하는 벽의 개수를 빼고, 나머지 칸에서 벽을 설치할 3개의 칸을 조합으로 고른다
# # 1-1-1) 조합에 들어갈 리스트는?: (x,y) 좌표값으로 지정한다.
# # 1-1-3) 전체 칸에서 0인 칸을 따로 저장한다.
# # 1-1-4) 이 0인 칸의 리스트가 조합에 쓰일 리스트이다.
#
# y=0
# for r in range(n):
#     line = list(map(int,input().split()))
#     board.append(line)
#     for c,ele in enumerate(line):
#         if ele == 0:
#             zeros.append([r,c])
#         elif ele == 2:
#             virus_list.append([r,c])
#         else:
#             continue
#
#
#
# insert_combinations = list(combinations(zeros,3))
#
# # 2-1) 1의 루프 안에서, 각 경우의 수에 뽑힌 3개의 0인 칸에 1을 넣는다.
# # 2-2) 남아있는 0인 칸에서 각 2를 DFS를 돌린다.
# # 2-3) DFS는 2가 존재하면 나머지 칸들도 2로 만드는 것이다.
# # 2-4) 여기서, 범위 설정은
# # 2-4-1) 2의 상하좌우에 맵의 끝이 있거나, 1이 존재하면 DFS는 진행되지 못한다.
# # 2-5) 2의 DFS 가 모두 진행된 후, 맵에서 남은 0의 개수를 구한다.
# # 2-6) 이 것을 safe라고 하며, min(safe,this_safe)로 하여 모든 경우의 수를 고려할 때 safe의 최솟값을 구한다.
#
# for case in insert_combinations:
#     temp_board = board
#     for wall in case:
#         zeros.remove(wall)
#         r,c = wall
#         temp_board = insert_wall(r,c,temp_board)
#
#
#
#
#

# solution

## idea
# 1. 실제 board와 임시 board인 temp_board를 만든다.
# 2. 벽을 3개 설치한다.
# 2-1) dfs(count)로 board에 벽을 하나씩 설치한다. 즉, count 로 벽의 개수를 늘려가다가, count = 3 일 때 board의 데이터를 temp에 옮겨 담고,
# 각 바이러스 위치에서 virus_dfs(x,y)를 수행한 뒤 안전 영역의 최댓값을 계산한 뒤 dfs를 return 으로 종료한다.
# 2-2) 이 때 안전영역을 구하는 함수 get_safe()를 수행한다.

n,m = map(int,input().split())

board = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

dy = [0,0,-1,1]
dx = [-1,1,0,0]

result=0

for _ in range(n):
    line = list(map(int,input().split()))
    board.append(line)

# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 temp 맵에서 사방으로 퍼지도록 하기
def virus_def(x,y):

    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx <= (n-1) and ny <= (m-1):
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus_def(nx,ny)

# 현재 temp 맵에서 안전 영역의 크기 계산하는 메서드
def get_safe():
    safe_area_num=0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                safe_area_num+=1
    return safe_area_num

# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매 번 안전 영역의 크기 계산
def dfs(count):
    global result

    if count==3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = board[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus_def(i,j)

        result = max(result, get_safe())
        return

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                count+=1
                board[i][j]=1
                dfs(count)
                count-=1
                board[i][j]=0

dfs(0)
print(result)

