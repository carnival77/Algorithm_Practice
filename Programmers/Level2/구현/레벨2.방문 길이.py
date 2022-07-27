#!/usr/bin/env Python
# coding=utf-8

#solution 1. 비효율적
# used = []
# x, y = 0, 0
# ans = 0
#
# def process(nx, ny):
#     global x, y, used, ans
#     route1 = [(x, y), (nx, ny)]
#     route2 = [(nx, ny), (x, y)]
#     if 0 <= nx <= 10 and 0 <= ny <= 10:
#         if route1 not in used or route2 not in used:
#             used.append(route1)
#             used.append(route2)
#             ans += 1
#     else:
#         return
#     x, y = nx, ny
#     return
#
# def solution(dirs):
#     global x,y,used,ans
#     x, y = 5, 5
#     for dir in dirs:
#         if dir == 'U':
#             process(x - 1, y)
#         elif dir == 'D':
#             process(x + 1, y)
#         elif dir == 'R':
#             process(x, y + 1)
#         else:
#             process(x, y - 1)
#     return ans

#solution 2. set과 dictionary 사용
def solution(dirs):
    s=set()
    d= {'U':(1,0),'D':(-1,0),'L':(0,-1),'R':(0,1)}
    x,y=5,5
    for dir in dirs:
        nx,ny=x+d[dir][0],y+d[dir][1]
        if 0<=nx<=10 and 0<=ny<=10:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x,y=nx,ny
    return len(s)//2

dirs = "ULURRDLLU"
print(solution(dirs))