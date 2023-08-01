import sys
from collections import deque
input=sys.stdin.readline

n,k=map(int,input().split())
a=deque(list(map(int,input().split())))
r=deque([0]*n)
ans=0

def check1():
    global r

    if r[n-1]==1:
        r[n-1]=0

def move():
    global r

    for i in range(n-2,0,-1):
        if r[i]==1 and r[i+1]==0 and a[i+1]>0:
            r[i+1],r[i]=r[i],r[i+1]
            a[i+1]-=1

def check2():
    cnt=0
    for i in range(2*n):
        if a[i]==0:
            cnt+=1
    if cnt>=k:
        return True
    return False

while True:
    ans += 1
    a.rotate(1)
    r.rotate(1)
    check1()
    move()
    check1()
    if a[0]>0:
        r[0]=1
        a[0]-=1
    if check2():
        break

print(ans)