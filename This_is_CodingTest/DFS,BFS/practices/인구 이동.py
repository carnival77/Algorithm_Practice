from collections import deque

n,l,r = map(int,input().split())

board=[]

for _ in range(n):
    board.append(list(map(int,input().split())))

dy = [0,0,-1,1]
dx = [-1,1,0,0]

day_cnt=0

# bfs 로 인구 이동 가능한 국가들을 연합으로 그룹 짓고, 같은 union_num을 부여한 뒤, 연합 내 인구 이동 실행.
def process(x,y,union_num):
    # 연합된 국가들
    united=[]
    united.append((x,y))
    # 연합 국가들의 인구 수 합
    sum = board[x][y]
    # bfs 위한 연합 국가들 q
    q = deque()
    q.append((x,y))
    # 현재 연합 번호 할당
    union[x][y] = union_num

    while q:
        x,y = q.popleft()

        # 상하좌우
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]

            # 상하좌우 방향의 해당 칸이 맵 내에 있고 아직 union에 가입되지 않았다면
            if nx >=0 and ny >= 0 and nx < n and ny < n and union[nx][ny] == -1:
                # 인구 차이가 l 이상 r 이하라면
                if l <= abs(board[x][y] - board[nx][ny])  <= r:
                    # 같은 연합이므로
                    # q에 삽입
                    q.append((nx,ny))
                    # united에 삽입
                    united.append((nx,ny))
                    # 연합 번호 할당
                    union[nx][ny] = union_num

                    sum += board[nx][ny]

    # 연합 내 국가 간 인구 이동
    for x,y in united:
        board[x][y] = sum // len(united)

while True:
    # 매일마다 연합 갱신. 아직 연합이 정해지지 않은 곳은 -1
    union = [[-1] * n for _ in range(n)]
    # 연합 개수(번호). 이것이 n*n 과 같게 되어 연합이 전혀 없고 각 나라가 개인팀이 되어야 인구 이동 종료
    union_num=0
    # board 전체 체크
    for x in range(n):
        for y in range(n):
            # 만약 연합이 정해지지 않은 곳이면
            if union[x][y] == -1:
                # process 실행. bfs 로 인구 이동 가능한 국가들을 연합으로 그룹 짓고, 같은 union_num을 부여한 뒤, 연합 내 인구 이동 실행.
                process(x,y,union_num)
                # 연합 개수(번호) +1
                union_num += 1

    # 연합 개수(번호). 이것이 n*n 과 같게 되어 연합이 전혀 없고 각 나라가 개인팀이 되어야 인구 이동 종료
    if union_num == n*n:
        break
    # 한 번의 인구 이동이 종료되면 1일 +
    day_cnt += 1

print(day_cnt)