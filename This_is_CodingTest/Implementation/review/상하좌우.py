n = int(input())

cmds = list(map(str,input().split()))

board = [[False] * n for i in range(n)]

move_types = ['R','L','U','D']

dx = [0,0,-1,1]
dy = [1,-1,0,0]

board[0][0] = True

x,y=0,0

for cmd in cmds:
    for direction in range(4):
        if move_types[direction] == cmd:
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < n and 0 <= ny < n:
                x = nx
                y = ny
            else: continue

print(x+1,y+1)