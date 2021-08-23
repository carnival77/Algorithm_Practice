# 풀이법
# 1. 드래곤 커브를 그릴 때, 시작점의 좌표와 방향을 활용하자.
# 2. k세대는, (K-1)세대의 순서를 반대로 하고, 반시계 방향으로 90도 회전한 것.

# 주의
# 문제에서의 x,y 좌표는 일반적인 좌표계에서의 x,y 좌표처럼 기능한다.
# 하지만, 시스템 입력 상의 좌표는 행 = x, 열 = y 이므로, 위와 반대임을 유의하자

import sys

input = sys.stdin.readline

c=[[False]*101 for i in range(101)]

# 방향 0,1,2,3 은 문제에 나와있는 대로의 순서와 같다.
dx = [0,-1,0,1]
dy = [1,0,-1,0]

n=int(input())

# 이전 세대부터 다음 세대의 것까지 합쳐진 모든 방향 구하기
def curve(d,g):
    ans=[d]
    for _ in range(g):
        # ng = next generation. 다음 세대
        # 2. k세대는, (K-1)세대의 순서를 반대로 하고, 반시계 방향으로 90도 회전한 것.
        # 먼저 이전 세대의 방향을 모두 얻고
        ng = ans[:]
        # 순서 반대로
        ng = ng[::-1]
        # 모두 반시계 90도 회전
        for i in range(len(ng)):
            ng[i] = (ng[i]+1)%4
        # 기존 세대에 다음 세대 합치기
        ans+=ng
    return ans


for _ in range(n):
    y,x,d,g = map(int,input().split())
    # 이전 세대부터 다음 세대의 것까지 합쳐진 모든 방향 구하기
    dir = curve(d,g)
    c[x][y] = True
    # 방향대로 1줄씩 선 그리기
    for d in dir:
        x += dx[d]
        y += dy[d]
        c[x][y] = True

ans =0
for i in range(100):
    for j in range(100):
        if c[i][j]==True and c[i+1][j] == True and c[i][j+1] == True and c[i+1][j+1] == True:
            ans+=1

print(ans)