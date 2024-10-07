from collections import deque

answer=[]
t=int(input())
for round in range(1,t+1):
    cmds=list(input())
    n=int(input())
    q=deque(input().strip('['']').split(','))
    ok=False
    rev=1 # 1이면 정방향, -1이면 역방향
    for cmd in cmds:
        if cmd=='R':
            rev=-rev
        else:
            if n<=0:
                answer.append("error")
                ok=True
                break
            else:
                if rev==1:
                    q.popleft()
                else:
                    q.pop()
                n-=1
    if ok:continue
    if rev==-1:
        q.reverse()
    ans='['
    for inx,e in enumerate(q):
        ans+=e
        if inx==len(q)-1:continue
        ans+=','
    ans+=']'
    answer.append(ans)

for e in answer:
    print(e)