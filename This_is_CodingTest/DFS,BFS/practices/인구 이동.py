from collections import deque

N,L,R = map(int,input().split())

board=[]

for _ in range(N):
    board.append(list(map(int,input().split())))

visi

union = deque()

# 차이값 sub이 L,R 범위 내인 지 체크. 범위 내이면 True
def between(sub):
    if sub >= L and sub <= R:
        return True
    else:
        return False

# board 전체를 완전 탐색
for x in range(N):
    for y in range(N):

        # board 각 칸마다 상, 하, 좌, 우 살핀다
        for direction in range(4):

            # 상
            if direction == 0:
                # 해당 방향의 칸이 맵을 벗어나 존재하지 않고, 아직 방문하지 않았을 때
                if x-1 <= 0 and visited[]:
                    # 해당 방향의 인접칸과 this 칸의 value 차이값을 계산하고, L <= 차이값 <= R 이라면, queue에 담아 연합을 이룬다.
                    sub = board[x-1][y] - board[x][y]
                    if between(sub):

                        union.append()
