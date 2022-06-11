from collections import deque
import sys

f,s,g,u,d=map(int,input().split())

q=deque()
q.append((s,0))
check=[False]*(f+1)
check[s]=True

while q:
    now,cnt=q.popleft()
    if now==g:
        print(cnt)
        sys.exit(0)
    for next in [now+u,now-d]:
        if 1<=next<=f and not check[next]:
            q.append((next,cnt+1))
            check[next]=True

print("use the stairs")