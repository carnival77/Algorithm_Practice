import sys
input=sys.stdin.readline

n=int(input())
t=[0]
p=[0]
for _ in range(n):
    a,b=map(int,input().split())
    t.append(a)
    p.append(b)
d=[-1]*(n+1)

def go(i):
    if i==n+1:
        return 0
    if i>n+1:
        return -int(1e9)
    if d[i]!=-1:
        return d[i]
    t1=go(i+1)
    t2=p[i]+go(i+t[i])
    d[i]=max(t1,t2)
    return d[i]

print(go(1))