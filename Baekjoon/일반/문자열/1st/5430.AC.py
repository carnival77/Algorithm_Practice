import sys
from collections import deque
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    ok=False
    p=list(input().strip())
    n=int(input())
    data=input().strip()[1:-1].split(',')
    a=deque(data)
    if n==0:
        a=deque()
    cnt=0
    for cmd in p:
        if cmd=='R':
            cnt+=1
        else:
            if len(a)<=0:
                print("error")
                ok=True
                if ok:
                    break
            if cnt%2==1:
                a.pop()
            else:
                a.popleft()
    if not ok:
        if cnt%2==1:
            a.reverse()
        print('['+",".join(map(str,a))+']')