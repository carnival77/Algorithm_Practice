# solution 1. 미리 조합 경우의 수를 다 뽑기
# import sys
# from itertools import combinations
#
# n,m,h=map(int,input().split())
# H=h+2
# N=n+2
# a=[[0]*N for _ in range(H)]
# ans=int(1e9)
#
# for x in range(H):
#     a[x][0]=-1
#     a[x][N-1]=-1
#
# # 초기 메모리 유실선 표시
# for _ in range(m):
#     x,y=map(int,input().split())
#     a[x][y]=1
#
# cand=[] # 가로선 설치 위치 후보
# for x in range(1,H-1):
#     for y in range(1,N-2):
#         if a[x][y]==0:
#             if a[x][y-1]==1 or a[x][y+1]==1:
#                 continue
#             else:
#                 cand.append([x,y])
#
# # 가로선 설치 후보 중 3개를 선택하여 만드는 모든 조합의 경우의 수
# comb=[]
# for event in combinations(cand,3):
#     comb.append(event)
#
# def copyBoard(a):
#     return [row[:] for row in a]
#
# # 열 번호 그대로 내려오는지 확인
# def process(b):
#     for sy in range(1, N - 1):
#         x = 0
#         y = sy
#         while x < H:
#             if b[x][y] == 1:
#                 y += 1
#             elif b[x][y - 1] == 1:
#                 y -= 1
#             x += 1
#         if y != sy:
#             return False
#     return True
#
# # 초기에 유실선 없으면 그대로
# if process(a):
#     print(0)
#     sys.exit(0)
#
# # 가로선 설치 후보 중 3개를 선택하여 만들어진 각 조합의 경우의 수에서
# for event in comb:
#     b=copyBoard(a)
#     # 1,2,3개 각 설치 시
#     cnt = 1
#     for px,py in event:
#         b[px][py]=1
#         ok=process(b)
#         if ok:
#             ans=min(ans,cnt)
#             break
#         cnt+=1
# if ans>3:
#     print(-1)
# else:
#     print(ans)

# solution 2. 조합의 경우의 수를 조건에 맞게 순서대로 찾음 -> 시간복잡도 훨씬 작다
import sys
from itertools import combinations

n,m,h=map(int,input().split())
H=h+2
N=n+2
a=[[0]*N for _ in range(H)]
ans=int(1e9)

for x in range(H):
    a[x][0]=-1
    a[x][N-1]=-1

# 초기 메모리 유실선 표시
for _ in range(m):
    x,y=map(int,input().split())
    a[x][y]=1

cand=[] # 가로선 설치 위치 후보
for x in range(1,H-1):
    for y in range(1,N-2):
        if a[x][y]==0:
            if a[x][y-1]==1 or a[x][y+1]==1:
                continue
            else:
                cand.append([x,y])

def copyBoard(a):
    return [row[:] for row in a]

# 열 번호 그대로 내려오는지 확인
def process(b):
    for sy in range(1, N - 1):
        x = 0
        y = sy
        while x < H:
            if b[x][y] == 1:
                y += 1
            elif b[x][y - 1] == 1:
                y -= 1
            x += 1
        if y != sy:
            return False
    return True

# 초기에 유실선 없으면 그대로
if process(a):
    print(0)
    sys.exit(0)

# 가로선 설치 후보 중 3개를 선택하여 만들어진 각 조합의 경우의 수에서
for num in range(1,4):
    for event in combinations(cand,num):
        b=copyBoard(a)
        # 1,2,3개 각 설치 시
        for px,py in event:
            b[px][py]=1
            ok=process(b)
            if ok:
                print(num)
                sys.exit(0)
print(-1)
