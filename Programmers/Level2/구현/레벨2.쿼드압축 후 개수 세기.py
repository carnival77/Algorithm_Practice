#!/usr/bin/env Python
# coding=utf-8
# 1st try. 정답 x, 비효율적 코딩
# a=[]
#
# def check(x,y,n,tmp):
#     global a
#     for i in range(x,x+n):
#         for j in range(y,y+n):
#             if a[i][j]!=tmp:
#                 return False
#     return True
#
# def convert(x,y,n,tmp):
#     global a
#     for i in range(x,x+n):
#         for j in range(y,y+n):
#             if i==x and j==y:
#                 continue
#             else:
#                 a[i][j]=-1
#
# def recur(x,y,n):
#     global a
#     if n==1:
#         return
#     if check(x,y,n,a[x][y]):
#         convert(x,y,n,a[x][y])
#         return
#     for i in range(x,n):
#         for j in range(y,n):
#             # if x<=i<n//2 and y<=j<n//2:
#             if i==x and j==y:
#                 recur(i,j,n//2)
#             # elif x<=i<n//2 and n//2<=j<n:
#             elif i==x and j==n//2:
#                 recur(i,j,n//2)
#             # elif n//2<=i<n and y<=j<n//2:
#             elif i==n//2 and j==y:
#                 recur(i,j,n//2)
#             elif i==n//2 and j==n//2:
#                 recur(i,j,n//2)
#
# def solution(arr):
#     global a
#     a=arr
#     n=len(a)
#     recur(0,0,n)
#     cnt1,cnt2=0,0
#     for i in range(n):
#         for j in range(n):
#             if a[i][j]==0:
#                 cnt1+=1
#             elif a[i][j]==1:
#                 cnt2+=1
#
#     for i in range(n):
#         print(a[i])
#
#     return [cnt1,cnt2]

def solution(arr):
    answer = [0,0]

    a=arr
    n=len(a)

    def compression(x,y,n):
        start=a[x][y]
        for i in range(x,x+n):
            for j in range(y,y+n):
                if start!=a[i][j]:
                    n//=2
                    compression(x,y,n)
                    compression(x,y+n,n)
                    compression(x+n,y,n)
                    compression(x+n,y+n,n)
                    return
        answer[start]+=1

    compression(0,0,n)

    return answer

# arr=[[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
arr=[[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
print(solution(arr))