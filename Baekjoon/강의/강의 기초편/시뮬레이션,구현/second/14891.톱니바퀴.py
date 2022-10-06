from collections import deque
import math

n=4
d=[]
ans=0

for i in range(n):
    data=list(map(int,input()))
    d.append(deque(data))

k=int(input())

# 맞닿은 극이 달라서 반대방향 회전이 필요하면 True, 아니면 False 반환
def rcheck(num):
    if d[num][2]!=d[num+1][6]:
        return True
    else:
        return False

def lcheck(num):
    if d[num][6]!=d[num-1][2]:
        return True
    else:
        return False

for _ in range(k):
    num,dir=map(int,input().split())
    num-=1
    a=[0]*n # 각 톱니의 회전 여부. 0 = 회전 X. 1 = 시계방향, -1 = 반시계방향
    a[num]=dir
    # 왼쪽 톱니바퀴 연쇄적으로 구하기
    for i in range(num,0,-1):
        if lcheck(i):
            a[i-1]=-a[i]
        else:
            break
    # 오른쪽 톱니바퀴 연쇄적으로 구하기
    for i in range(num,n-1):
        if rcheck(i):
            a[i+1]=-a[i]
        else:
            break
    # 회전 적용
    for i in range(n):
        if a[i]==0:
            continue
        elif a[i]==1:
            d[i].rotate(1)
        elif a[i]==-1:
            d[i].rotate(-1)

for i in range(n):
    if d[i][0]==1:
        ans+=int(math.pow(2,i))

print(ans)