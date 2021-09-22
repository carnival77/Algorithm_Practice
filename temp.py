import sys
class Fish:
    def __init__(self, size=0, speed=0, direction=0):
        self.size = size
        self.speed = speed
        self.direction = direction
# up, down, right, left
dx = [-1,1,0,0]
dy = [0,0,1,-1]
n, m, mm = map(int,input().split())
fish = [[Fish() for j in range(m)] for i in range(n)]
nfish = [[Fish() for j in range(m)] for i in range(n)]
for _ in range(mm):
    x,y,s,d,z = map(int,input().split())
    x -= 1
    y -= 1
    d -= 1
    fish[x][y] = Fish(z,s,d)

def get_next(x, y, speed, direction):
    for k in range(speed):
        if direction == 0: # up
            if x == 0:
                x = 1
                direction = 1
            else:
                x -= 1
        elif direction == 1: # down
            if x == n-1:
                x = n-2
                direction = 0
            else:
                x += 1
        elif direction == 2: # right
            if y == m-1:
                y = m-2
                direction = 3
            else:
                y += 1
        elif direction == 3: # left
            if y == 0:
                y = 1
                direction = 2
            else:
                y -= 1
    return (x,y,direction)

ans = 0

for j in range(m):
    for i in range(n):
        if fish[i][j].size > 0:
            ans += fish[i][j].size
            print(ans)
            fish[i][j].size = 0
            break
    for l1 in range(n):
        for l2 in range(m):
            if fish[l1][l2].size == 0:
                continue
            f = fish[l1][l2]
            x, y, direction = get_next(l1, l2, f.speed, f.direction)
            if nfish[x][y].size == 0 or nfish[x][y].size < f.size:
                nfish[x][y] = Fish(f.size, f.speed, direction)
    for l1 in range(n):
        for l2 in range(m):
            fish[l1][l2] = Fish(nfish[l1][l2].size, nfish[l1][l2].speed, nfish[l1][l2].direction)
            nfish[l1][l2].size = 0

print(ans)