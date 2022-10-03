# n=int(input())
# a=[list(map(int,input().split())) for _ in range(n)]
# x,y=0,1
# ans=0
#
# def dfs(x,y,direction):
#     global a,n,ans
#
#     if (x,y)==(n-1,n-1):
#         ans+=1
#         return
#
#     # 가로
#     if direction==0:
#         # 가로
#         if 0<=y+1<n and a[x][y+1]!=1:
#             dfs(x,y+1,0)
#         # 대각선
#         if 0<=x+1<n and 0<=y+1<n and a[x+1][y+1]!= 1 and a[x][y+1]!=1 and a[x+1][y]!=1:
#             dfs(x+1,y+1,2)
#     # 세로
#     elif direction==1:
#         # 세로
#         if 0 <= x+1 < n and a[x+1][y]!=1:
#             dfs(x+1, y,1)
#         # 대각선
#         if 0 <= x + 1 < n and 0 <= y + 1 < n and a[x+1][y+1]!= 1 and a[x][y+1]!=1 and a[x+1][y]!=1:
#             dfs(x + 1, y + 1,2)
#     # 대각선
#     elif direction==2:
#         # 가로
#         if 0<=y+1<n and a[x][y+1]!=1:
#             dfs(x,y+1,0)
#         # 세로
#         if 0 <= x+1 < n and a[x+1][y]!=1:
#             dfs(x+1, y,1)
#         # 대각선
#         if 0 <= x + 1 < n and 0 <= y + 1 < n and a[x+1][y+1]!= 1 and a[x][y+1]!=1 and a[x+1][y]!=1:
#             dfs(x + 1, y + 1,2)
# dfs(x,y,0)
# print(ans)

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
x,y=0,1

def dfs(x,y,direction):
    global a,n
    if (x,y)==(n-1,n-1):
        return 1
    ans = 0
    # 가로
    if direction==0:
        # 가로
        if 0<=y+1<n and a[x][y+1]!=1:
            ans+=dfs(x,y+1,0)
        # 대각선
        if 0<=x+1<n and 0<=y+1<n and a[x+1][y+1]!= 1 and a[x][y+1]!=1 and a[x+1][y]!=1:
            ans+=dfs(x+1,y+1,2)
    # 세로
    elif direction==1:
        # 세로
        if 0 <= x+1 < n and a[x+1][y]!=1:
            ans+=dfs(x+1, y,1)
        # 대각선
        if 0 <= x + 1 < n and 0 <= y + 1 < n and a[x+1][y+1]!= 1 and a[x][y+1]!=1 and a[x+1][y]!=1:
            ans+=dfs(x + 1, y + 1,2)
    # 대각선
    elif direction==2:
        # 가로
        if 0<=y+1<n and a[x][y+1]!=1:
            ans+=dfs(x,y+1,0)
        # 세로
        if 0 <= x+1 < n and a[x+1][y]!=1:
            ans+=dfs(x+1, y,1)
        # 대각선
        if 0 <= x + 1 < n and 0 <= y + 1 < n and a[x+1][y+1]!= 1 and a[x][y+1]!=1 and a[x+1][y]!=1:
            ans+=dfs(x + 1, y + 1,2)
    return ans
print(dfs(x,y,0))