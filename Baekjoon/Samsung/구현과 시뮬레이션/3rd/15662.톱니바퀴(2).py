import sys
from collections import deque
input=sys.stdin.readline

t=int(input())
a=[]
for _ in range(t):
    q=deque()
    data=input().strip()
    for i in range(8):
        q.append(int(data[i]))
    a.append(q)
ans=0

def check(no,kind):
    if kind==0 and a[no][2]!=a[no+1][6]:
        return True
    if kind==1 and a[no][6]!=a[no-1][2]:
        return True
    return False

def process(no,d):
    global a

    dir=[0]*t
    dir[no]=d

    # 우측
    for i in range(no,t-1):
        if check(i,0):
            dir[i+1]=-dir[i]

    # 좌측
    for i in range(no,0,-1):
        if check(i,1):
            dir[i-1]=-dir[i]

    for i in range(t):
        if dir[i]==1:
            a[i].rotate(1)
        elif dir[i]==-1:
            a[i].rotate(-1)

for step in range(int(input())):
    no,d=map(int,input().split())
    process(no-1,d)

for i in range(t):
    if a[i][0]==1:
        ans+=1
print(ans)