#!/usr/bin/env Python
# coding=utf-8

# solution 1. 코드 길이가 너무 길고 풀이에 오래 걸린다.
# import math
# num=1
# a=[]
# n=0
# def process(sx,sy):
#     global num,n,a
#     x,y=sx,sy
#     #1
#     while a[x][y]==0:
#         a[x][y]=num
#         num += 1
#         nx=x+1
#         if nx<n and a[nx][y]==0:
#             x=nx
#         else:
#             break
#     #2
#     y+=1
#     while a[x][y]==0:
#         a[x][y] = num
#         num += 1
#         ny=y+1
#         if ny<n and a[x][ny]==0:
#             y=ny
#         else:
#             break
#     #3
#     x-=1
#     y-=1
#     while a[x][y]==0:
#         a[x][y] = num
#         num += 1
#         x-=1
#         y-=1
#
# def solution(n):
#     global a
#     answer = []
#
#     a=[[0]*n for _ in range(n)]
#     i=0
#     while i<math.ceil(n/3):
#         sx=2*i
#         sy=i
#         process(sx,sy)
#         i+=1
#
#     # for i in range(n):
#     #     print(a[i])
#
#     for i in range(n):
#         for j in range(n):
#             if a[i][j]!=0:
#                 answer.append(a[i][j])
#
#     return answer

# solution 2.
def solution(n):
    answer = []
    a=[[0]*n for _ in range(n)]

    x,y=-1,0
    num=1

    for i in range(n):
        for _ in range(n-i):
            if i%3==0:
                x+=1
            elif i%3==1:
                y+=1
            else:
                x-=1
                y-=1
            a[x][y]=num
            num+=1

    for i in range(n):
        for j in range(n):
            if a[i][j]!=0:
                answer.append(a[i][j])

    return answer

n=4
print(solution(n))