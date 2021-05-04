

if __name__ == '__main__':

    n, m = map(int, input().split())

    visit = [[0] * m for _ in range(n)]

    x,y,direction = map(int, input().split())
    visit[x][y]=1

    map_arr = []
    for i in range(n):
        map_arr.append(list(map(int, input().split())))

    dx=[-1,0,1,0]
    dy=[0,1,0,-1]

    def turn_left():
        global direction
        direction -= 1
        if direction == -1:
            direction = 3

    count=1
    turn_time=0
    while True:
        turn_left()
        nx = x + dx[direction]
        ny = y + dy[direction]

        if map_arr[nx][ny] == 0 and visit[nx][ny] ==0:
            x=nx
            y=ny
            count+=1
            turn_time=0
            continue
        else:
            turn_time+=1

        if turn_time==4:
            nx = x - dx[direction]
            ny = y - dy[direction]

            if map_arr[nx][ny] == 0:
                x=nx
                y=ny
            else:
                break
            turn_time=0

    print(count)
###