n=int(input())
t,p=[0],[0]
for _ in range(n):
    a,b=map(int,input().split())
    t.append(a)
    p.append(b)
d=[-1]*(n+1)
def recur(day):
    if day==n+1:
        return 0
    if day>n+1:
        return -int(1e9)
    if d[day]!=-1:
        return d[day]

    t1=recur(day+t[day])+p[day]
    t2=recur(day+1)
    d[day]=max(t1,t2)
    return d[day]

print(recur(1))