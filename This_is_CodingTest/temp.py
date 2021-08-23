# 풀이법
# 1. 드래곤 커브를 그릴 때, 시작점의 좌표와 방향을 활용하자.
# 2. k세대는, (K-1)세대의 순서를 반대로 하고, 반시계 방향으로 90도 회전한 것.

import sys

input = sys.stdin.readline

c=[[False]*101 for i in range(101)]
# dx=[1,0,-1,0]
# dy=[0,-1,0,1]
dx = [0,-1,0,1]
dy = [1,0,-1,0]
n=int(input())

# 이전 세대부터 다음 세대의 것까지 합쳐진 모든 방향 구하기
def curve(d,g):
    ans=[d]
    for _ in range(1,g+1):
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
    for d in dir:
        x += dx[d]
        y += dy[d]
        c[x][y] = True
ans = 0
for i in range(100):
    for j in range(100):
        if c[i][j] and c[i][j+1]  and c[i+1][j] and c[i+1][j+1]:
            ans += 1
print(ans)