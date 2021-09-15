# 피드백
# 1.

n=int(input())
a=[[0] * (n+1) for _ in range(n+1)]
k=int(input())

for _ in range(k):
    x,y = map(int,input().split())
    a[x][y] = 1

l=int(input())

changes = []

for _ in range(l):
    x,c = input().split()
    changes.append((int(x),c))

# 오른쪽, 아래, 왼쪽, 위
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 처음엔 오른쪽
direction = 0

#뱀.
# 현재 머리 위치
x,y=1,1
a[x][y] =2
# 전체 위치
q=[(x,y)]
s=0

while True:
    s+=1
    # 다음 머리 위치
    nx = x+dx[direction]
    ny = y+dy[direction]
    # 종료 조건
    if nx > n or nx < 1 or ny > n or ny < 1:
        print(s)
        break
    if a[nx][ny] == 2:
        print(s)
        break
    else:
        # 규칙 1,2번
        if a[nx][ny] == 1:
            a[nx][ny]=2
            q.append((nx,ny))
        # 규칙 1,3번
        elif a[nx][ny] == 0:
            a[nx][ny] = 2
            q.append((nx, ny))
            px,py = q.pop(0)
            a[px][py] = 0
    #다음 머리 위치로 현재 머리위치 조정
    x,y = nx,ny
    # 방향 전환 체크
    for sec,c in changes:
        if sec==s:
            if c=='D':
                direction = (direction+1)%4
            elif c=='L':
                if direction == 0:
                    direction=4
                direction -= 1
