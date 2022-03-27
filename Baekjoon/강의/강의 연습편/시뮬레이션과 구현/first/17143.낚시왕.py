import sys
input=sys.stdin.readline

# 상어의 정보. 위치는 [x][y]로 표시하고, 해당 칸의 상어가 아래의 3개의 정보를 갖는다.
class Fish:
    def __init__(self, size=0, speed=0, direction=0):
        self.size = size
        self.speed = speed
        self.direction = direction
# up, down, right, left
dx = [-1,1,0,0]
dy = [0,0,1,-1]
n, m, mm = map(int,input().split())
# 두 개의 맵을 만든다. 두 번째 맵은 상어가 이동 완료 후 잡아먹히는 지 여부 반영하고, 첫 번째 맵에 다시 등록하기 위해 존재
fish = [[Fish() for j in range(m)] for i in range(n)]
nfish = [[Fish() for j in range(m)] for i in range(n)]
for _ in range(mm):
    x,y,s,d,z = map(int,input().split())
    x -= 1
    y -= 1
    d -= 1
    fish[x][y] = Fish(z,s,d)

# 상어의 다음 위치 계산
def get_next(x, y, speed, direction):
    for k in range(speed):
        if direction == 0: # up
            if x == 0:
                x = 1
                direction = 1
            else:
                x -= 1
        elif direction == 1: # down
            if x == n-1:
                x = n-2
                direction = 0
            else:
                x += 1
        elif direction == 2: # right
            if y == m-1:
                y = m-2
                direction = 3
            else:
                y += 1
        elif direction == 3: # left
            if y == 0:
                y = 1
                direction = 2
            else:
                y -= 1
    return (x,y,direction)

ans = 0

# 열의 수만큼 낚시꾼 1칸씩 우측 이동
for j in range(m):
    for i in range(n):
        if fish[i][j].size > 0:
            # 상어 잡으면 ans +
            ans += fish[i][j].size
            fish[i][j].size = 0
            break
    for l1 in range(n):
        for l2 in range(m):
            if fish[l1][l2].size == 0:
                continue
            f = fish[l1][l2]
            x, y, direction = get_next(l1, l2, f.speed, f.direction)
            # 만약 두 번째 맵의 해당 칸이 비어있거나, 칸에 있던 상어의 크기가 새로운 상어보다 작다면 대체
            if nfish[x][y].size == 0 or nfish[x][y].size < f.size:
                nfish[x][y] = Fish(f.size, f.speed, direction)
    # 두 번째 맵의 상어 정보들을 첫 번째 맵으로 되돌려넣기
    for l1 in range(n):
        for l2 in range(m):
            fish[l1][l2] = Fish(nfish[l1][l2].size, nfish[l1][l2].speed, nfish[l1][l2].direction)
            nfish[l1][l2].size = 0

print(ans)