import sys
input=sys.stdin.readline

n,r=map(int,input().split())
N=2**n
a=[list(map(int,input().split())) for _ in range(N)]

def up_down_inversion(a):
    return a[::-1]

def right_left_inversion(a):
    for i in range(len(a)):
        a[i]=a[i][::-1]
    return a

def rotate_90_clockwise(a):
    return list(map(list,zip(*a[::-1])))

def rotate_90_counter_clockwise(a):
    return list(map(list,zip(*a)))[::-1]

def op_one_to_four(k,cmd):
    global a

    b=[[0]*N for _ in range(N)]
    for x in range(0,N,k):
        for y in range(0,N,k):
            part=[[0]*k for _ in range(k)]
            for i in range(k):
                for j in range(k):
                    part[i][j]=a[x+i][y+j]
            if cmd==1:
                part=up_down_inversion(part)
            elif cmd==2:
                part=right_left_inversion(part)
            elif cmd==3:
                part=rotate_90_clockwise(part)
            else:
                part=rotate_90_counter_clockwise(part)
            for i in range(k):
                for j in range(k):
                    b[x+i][y+j]=part[i][j]
    a=b

def op_five_to_eight(k,cmd):
    global a

    b = [[0] * N for _ in range(N)]
    l=N//k
    all=[[0]*l for _ in range(l)]
    for rowInx,x in enumerate(range(0,N,k)):
        for colInx,y in enumerate(range(0,N,k)):
            part=[[0]*k for _ in range(k)]
            for i in range(k):
                for j in range(k):
                    part[i][j]=a[x+i][y+j]
            all[rowInx][colInx]=part
    if cmd==5:
        all=up_down_inversion(all)
    elif cmd==6:
        all=right_left_inversion(all)
    elif cmd==7:
        all=rotate_90_clockwise(all)
    else:
        all=rotate_90_counter_clockwise(all)
    for rowInx,x in enumerate(range(0,N,k)):
        for colInx,y in enumerate(range(0,N,k)):
            part=all[rowInx][colInx]
            for i in range(k):
                for j in range(k):
                    b[x+i][y+j] = part[i][j]
    a=b

for _ in range(r):
    cmd,L=map(int,input().split())
    k=2**L
    if 1<=cmd<=4:
        op_one_to_four(k,cmd)
    else:
        op_five_to_eight(k,cmd)

for i in range(len(a)):
    for j in range(len(a[0])):
        print(a[i][j], end = ' ')
    print()