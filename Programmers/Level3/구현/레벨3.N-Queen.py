# solution 1. N^2 개의 칸 중 n개를 조합으로 뽑고, (상/하/좌/우/왼쪽 대각선 위/왼쪽 대각선 아래/오른쪽 대각선 위/오른쪽 대각선 아래) 8가지 방향을 모두 검사
# -> 시간 초과. 왜냐하면 1<=n<=15 이므로, n=15일 경우, 225C15는 10초 제한(약 100억) 을 넘는다.

# from itertools import combinations
#
# board=[]
# spaces=[]
# qs=[]
# n=0
#
# def watch(x,y,direction):
#     global board
#     # 왼쪽
#     if direction == 0:
#         while True:
#             y-=1
#             if not y>=0:
#                 break
#             if board[x][y] == 2:
#                 return True
#
#     # 오른쪽
#     if direction == 1:
#         while True:
#             y += 1
#             if not y<n:
#                 break
#             if board[x][y] == 2:
#                 return True
#
#     # 위쪽
#     if direction == 2:
#         while True:
#             x -= 1
#             if not x>=0:
#                 break
#             if board[x][y] == 2:
#                 return True
#
#     # 아래쪽
#     if direction == 3:
#         while True:
#             x += 1
#             if not x<n:
#                 break
#             if board[x][y] == 2:
#                 return True
#
#     # 대각선 오른쪽 아래
#     if direction == 4:
#         while True:
#             x+=1
#             y+=1
#             if not y<n or not x<n:
#                 break
#             if board[x][y] == 2:
#                 return True
#
#     # 대각선 오른쪽 위
#     if direction == 5:
#         while True:
#             y+=1
#             x-=1
#             if not y<n or not x>=0:
#                 break
#             if board[x][y] == 2:
#                 return True
#
#     # 대각선 왼쪽 위
#     if direction == 6:
#         while True:
#             x-=1
#             y-=1
#             if not x>=0 or not y>=0:
#                 break
#             if board[x][y] == 2:
#                 return True
#
#     # 대각선 왼쪽 아래
#     if direction == 7:
#         while True:
#             y-=1
#             x+=1
#             if not y>=0 or not x<n:
#                 break
#             if board[x][y] == 2:
#                 return True
#
#     return False
#
# def process():
#     global qs
#
#     # print(qs)
#     for x,y in qs:
#         # print((x,y))
#         for i in range(8):
#             if watch(x,y,i):
#                 return False
#
#     return True
#
# def solution(input):
#     global board,spaces,qs,n
#     answer = 0
#
#     n=input
#
#     board=[[0] * n for _ in range(n)]
#
#     for i in range(n):
#         for j in range(n):
#             spaces.append((i,j))
#
#     for comb in combinations(spaces,n):
#
#         # Q 설치
#         for x,y in comb:
#             # Q를 설치했으면 2, 아니면 0
#             board[x][y] = 2
#             qs.append((x,y))
#
#         if process():
#             answer+=1
#
#         # Q 제거
#         for x,y in comb:
#             board[x][y] = 0
#             qs.remove((x,y))
#
#     return answer
#
# input=4
#
# print(solution(input))

# solution 2. n개의 각 줄에서 1개씩 Q을 놓는다고 생각하자.
# 0번째 행부터 시작하는 재귀함수 내의 for문으로 각 줄을 탐색하며, Q가 놓일 수 있는 열인지 체크하여, 놓을 수 있으면 놓고, 다른 경우의 수를 위해 놓은 것을 치우면 된다.
# Q를 놓을 때, 놓을 수 있는 지 체크해야 하는데, 체크할 때 열, 왼쪽에서 오른쪽으로 내려오는 대각선, 오른쪽에서 왼쪽으로 내려오는 대각선 이 3개의 boolean 배열을 체크한다.
# 또한 Q를 놓을 때, 열, 왼쪽에서 오른쪽으로 내려오는 대각선, 오른쪽에서 왼쪽으로 내려오는 대각선 이 3개의 boolean 배열에서 해당 위치와 연관된 요소를 True로 설정한다.
# 열, 왼쪽에서 오른쪽으로 내려오는 대각선, 오른쪽에서 왼쪽으로 내려오는 대각선 이 3개의 boolean 배열의 개수는 각각 n,2*n-1,2*n-1 개이며, 가리키는 위치는 n,row+col,n+row-col-1이다.

n=int(input())

def check(row,col):
    if check_col[col]:
        return False
    if check_dig1[row+col]:
        return False
    if check_dig2[n+row-col-1]:
        return False
    return True

def recur(row):
    # 백트랙킹. 모든 행을 탐색했다면, Q를 각 행에 한 개씩 놓을 수 있는 경우의 수이므로, 1을 리턴
    if row==n:
        return 1
    ans=0 # Q를 각 행에 한 개씩 놓을 수 있는 모든 경우의 수의 합
    # 0번째 행부터 시작하는 재귀함수 내의 for문으로 각 줄을 탐색하며, Q가 놓일 수 있는 열인지 체크하여, 놓을 수 있으면 놓고, 다른 경우의 수를 위해 놓은 것을 치우면 된다.
    for col in range(n):
        # Q를 놓을 때, 놓을 수 있는 지 체크해야 하는데, 체크할 때 열, 왼쪽에서 오른쪽으로 내려오는 대각선, 오른쪽에서 왼쪽으로 내려오는 대각선 이 3개의 boolean 배열을 체크한다.
        if check(row,col):
            # 또한 Q를 놓을 때, 열, 왼쪽에서 오른쪽으로 내려오는 대각선, 오른쪽에서 왼쪽으로 내려오는 대각선 이 3개의 boolean 배열에서 해당 위치와 연관된 요소를 True로 설정한다.
            check_col[col]=True
            check_dig1[row+col]=True
            check_dig2[n+row-col-1]=True
            a[row][col]=True
            ans+=recur(row+1)
            check_col[col]=False
            check_dig1[row+col]=False
            check_dig2[n+row-col-1]=False
            a[row][col]=False
    return ans

a=[[False]*n for _ in range(n)] # True: 이미 Q가 놓여져 있거나 연관된 방향이므로 놓을 수 없다. False : 놓을 수 있다.
# 열, 왼쪽에서 오른쪽으로 내려오는 대각선, 오른쪽에서 왼쪽으로 내려오는 대각선 이 3개의 boolean 배열의 개수는 각각 n,2*n-1,2*n-1 개이며, 가리키는 위치는 n,row+col,n+row-col-1이다.
check_col=[False]*n
check_dig1=[False]*(2*n-1)
check_dig2=[False]*(2*n-1)

print(recur(0))