n,m = map(int,input().split())

board=[]

for _ in range(n):
    board.append(list(map(int,input().split())))

temp=0
ans=0

def get_sum(x1,y1,x2,y2,x3,y3,x4,y4):
    return board[x1][y1] + board[x2][y2] + board[x3][y3] + board[x4][y4]

for x in range(n):
    for y in range(m):
        #1
        if y+3 < m:
            temp = get_sum(x,y,x,y+1,x,y+2,x,y+3)
            if ans < temp: ans = temp
        #2
        if x + 3 < n:
            temp = get_sum(x, y, x+1, y, x+2, y, x+3, y)
            if ans < temp: ans = temp
        #3
        if y+1 < m and x+1 < n:
            temp = get_sum(x,y,x+1,y,x,y+1,x+1,y+1)
            if ans < temp: ans = temp
        #4
        if y+1 < m and x+2 < n:
            temp = get_sum(x,y,x+1,y,x+2,y,x+2,y+1)
            if ans < temp: ans = temp
        #5
        if y+1 < m and x-2 >= 0:
            temp = get_sum(x,y,x,y+1,x-1,y+1,x-2,y+1)
            if ans < temp: ans = temp
        #6
        if y+2 < m and x+1 < n:
            temp = get_sum(x,y,x+1,y,x,y+1,x,y+2)
            if ans < temp: ans = temp
        #7
        if y+2 < m and x+1 < n:
            temp = get_sum(x,y,x,y+1,x,y+2,x+1,y+2)
            if ans < temp: ans = temp
        #8
        if y+2 < m and x-1 >= 0:
            temp = get_sum(x,y,x,y+1,x,y+2,x-1,y+2)
            if ans < temp: ans = temp
        #9
        if y+2 < m and x-1 >= 0:
            temp = get_sum(x,y,x,y+1,x,y+2,x-1,y)
            if ans < temp: ans = temp
        #10
        if y+1 < m and x+2 < n:
            temp = get_sum(x,y,x,y+1,x+1,y+1,x+2,y+1)
            if ans < temp: ans = temp
        #11
        if y+1 < m and x+2 < n:
            temp = get_sum(x,y,x,y+1,x+1,y,x+2,y)
            if ans < temp: ans = temp
        #12
        if y+1 < m and x+2 < n:
            temp = get_sum(x,y,x+1,y,x+1,y+1,x+2,y+1)
            if ans < temp: ans = temp
        #13
        if y+1 < m and x-2 >= 0:
            temp = get_sum(x,y,x-1,y,x-1,y+1,x-2,y+1)
            if ans < temp: ans = temp
        #14
        if y+2 < m and x+1 < n:
            temp = get_sum(x,y,x,y+1,x+1,y+1,x+1,y+2)
            if ans < temp: ans = temp
        #15
        if y+2 < m and x-1 >= 0:
            temp = get_sum(x,y,x,y+1,x-1,y+1,x-1,y+2)
            if ans < temp: ans = temp
        #16
        if y+1 < m and x+2 < n:
            temp = get_sum(x,y,x+1,y,x+2,y,x+1,y+1)
            if ans < temp: ans = temp
        #17
        if y+2 < m and x-1 >= 0:
            temp = get_sum(x,y,x,y+1,x-1,y+1,x,y+2)
            if ans < temp: ans = temp
        #18
        if y-1 >= 0 and x+2 < n:
            temp = get_sum(x,y,x+1,y,x+2,y,x+1,y-1)
            if ans < temp: ans = temp
        #19
        if y+1 < m and x+2 < n:
            temp = get_sum(x,y,x+1,y,x+2,y,x,y+1)
            if ans < temp: ans = temp

print(ans)