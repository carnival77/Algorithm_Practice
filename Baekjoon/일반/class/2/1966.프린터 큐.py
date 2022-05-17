from collections import deque

t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    q=deque()
    for i,a in enumerate(arr):
        q.append((a,i))
    cnt = 0
    while True:
        max_v=max(q)[0]
        f=q.popleft()
        if f[0]==max_v:
            cnt+=1
            if f[1]==m:
                print(cnt)
                break
        else:
            q.append(f)