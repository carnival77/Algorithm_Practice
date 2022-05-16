from collections import deque

MAX=200000

n,k=map(int,input().split())

check=[False]*(MAX+1)
dist=[-1]*(MAX+1)

dist[n]=0
check[n]=True

q=deque()
q.append(n)

while q:
    now=q.popleft()
    for next in [now-1,now+1,now*2]:
        if 0<=next<MAX+1 and not check[next]:
            q.append(next)
            dist[next]=dist[now]+1
            check[next]=True

print(dist[k])