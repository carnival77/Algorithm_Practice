# n = 9
# a = [list(map(int, input().split())) for _ in range(n)]
#
# dx = [0, 0, 1, -1, 1, -1, 1, -1, 0]
# dy = [1, -1, 0, 0, 1, 1, -1, -1, 0]
#
# s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# zeros = []
# cnt = 0
# for i in range(n):
#     for j in range(n):
#         if a[i][j] == 0:
#             zeros.append((i, j))
#             cnt += 1
# # print(zeros)
# while cnt > 0:
#     for x, y in zeros:
#         col = set()
#         for i in range(n):
#             if i != x:
#                 col.add(a[i][y])
#         result = s - col
#         if len(result) == 1:
#             a[x][y] = list(result)[0]
#             cnt -= 1
#         row = set()
#         for j in range(n):
#             if j != y:
#                 row.add(a[x][j])
#         result = s - row
#         if len(result) == 1:
#             a[x][y] = list(result)[0]
#             cnt -= 1
#     for x in range(1, 8, 3):
#         for y in range(1, 8, 3):
#             group = set()
#             tx,ty=0,0
#             for k in range(9):
#                 nx, ny = x + dx[k], y + dy[k]
#                 if a[nx][ny] != 0:
#                     group.add(a[nx][ny])
#                 else:
#                     tx,ty=nx,ny
#             result = s - group
#             if len(result) == 1:
#                 a[tx][ty] = list(result)[0]
#                 cnt -= 1
#
# for i in range(n):
#     print(a[i])

# solution.
# 빈 칸에 넣을 숫자를 판별하기 위해서는 해당 칸이 속한 행, 열, 3x3 크기의 정사각형 이 3개에 존재하는 숫자를 살펴야 한다.
# 이 3개를 row, col, sqaure 배열로 설정하여, 각 숫자를 포함하고 있는지를 Boolean형으로 나타내게 한다.
# 가령 row[i][j] = True 는 i번째 행은 j라는 숫자를 포함하고 있다는 뜻이다.
# 작은 정사각형은 총 9개가 있으며, make_square 함수는 (x,y)를 받고 해당 칸이 속한 작은 정사각형의 번호를 반환한다.
# recur 함수는 z==81이 되어 마지막 칸까지 탐색을 마치는 경우 답을 출력한다.

# 작은 정사각형은 총 9개가 있으며, make_square 함수는 (x,y)를 받고 해당 칸이 속한 작은 정사각형의 번호를 반환한다.
def make_square(x,y):
    return (x//3)*3 + y//3

def recur(z):
    # recur 함수는 z==81이 되어 마지막 칸까지 탐색을 마치는 경우 답을 출력하고 True를 리턴한다.
    if z==81:
        for r in a:
            print(' '.join(map(str,r)))
        return True
    x,y=z//n,z%n
    # 0이 아닌 경우 다음 칸을 탐색한다.
    if a[x][y]!=0:
        return recur(z+1)
    # 해당 칸에서 1~9의 숫자 중 행, 열, 작은 정사각형 모두에 없는 수를 넣어본다.
    for i in range(1,10):
        if not row[x][i] and not col[y][i] and not square[make_square(x,y)][i]:
            row[x][i] = col[y][i] = square[make_square(x,y)][i]=True
            a[x][y]=i
            # 경우의 수들 중 마지막 칸까지 탐색을 성공한 경우 True가 반환되므로, 아래의 제거 과정을 다시 밟지 않고 recur 함수가 종료되도록 True를 반환한다.
            if recur(z+1): return True
            # 다른 경우의 수를 위해 해당 칸에서 수를 다시 제거한다.
            row[x][i] = col[y][i] = square[make_square(x,y)][i]=False
            a[x][y]=0
    # 마지막 칸까지 탐색을 마치지도, 이번 칸이 0인 경우도 아닌 경우, 실패한 탐색이다.
    return False

n=9
a=[list(map(int,input().split())) for _ in range(n)]
# 빈 칸에 넣을 숫자를 판별하기 위해서는 해당 칸이 속한 행, 열, 3x3 크기의 정사각형 이 3개에 존재하는 숫자를 살펴야 한다.
# 이 3개를 row, col, sqaure 배열로 설정하여, 각 숫자를 포함하고 있는지를 Boolean형으로 나타내게 한다.
# 가령 row[i][j] = True 는 i번째 행은 j라는 숫자를 포함하고 있다는 뜻이다.
col=[[False]*10 for _ in range(n)]
row=[[False]*10 for _ in range(n)]
square=[[False]*10 for _ in range(n)]
for i in range(n):
    for j in range(n):
        if a[i][j]!=0:
            row[i][a[i][j]]=True
            col[j][a[i][j]]=True
            square[make_square(i,j)][a[i][j]]=True

recur(0)