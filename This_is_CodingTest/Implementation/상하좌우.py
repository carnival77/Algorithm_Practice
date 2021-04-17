
if __name__ == '__main__':

    n = int(input())

    x,y=1,1

    plans = input().split()

    moves = ['R','L','U','D']
    mx=[0,0,-1,1]
    my=[1,-1,0,0]

    for plan in plans:
        for i in range(len(moves)):
            if plan == moves[i]:
                nx = x + mx[i]
                ny = y + my[i]
        if nx<1 or ny<1 or nx >n or ny >n:
            continue
        x=nx
        y=ny

    print(x,y)
