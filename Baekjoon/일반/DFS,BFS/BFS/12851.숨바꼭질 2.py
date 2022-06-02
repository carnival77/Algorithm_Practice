from collections import deque

MAX=200000

n,k=map(int,input().split())

check=[False]*(MAX+1)
dist=[-1]*(MAX+1)
cnt=0

dist[n]=0
check[n]=True

q=deque()
q.append(n)

while q:
    now=q.popleft()
    if now==k:
        cnt+=1
    for next in [now-1,now+1,now*2]:
        #  최소 시간이 dist에 이미 있더라도, 큐에 넣어 cnt가 증가할 수 있도록 한다.
        if 0<=next<MAX+1 and (not check[next] or dist[next] == dist[now] + 1):
                q.append(next)
                dist[next] = dist[now] + 1
                check[next] = True

print(dist[k])
print(cnt)