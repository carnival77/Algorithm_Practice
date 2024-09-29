import sys
from collections import Counter

input=sys.stdin.readline

r,c,K=map(int,input().split())
r-=1
c-=1
MAX=100
n=m=3
# ok=False

a=[list(map(int,input().split())) for _ in range(3)]

def R(a,l):

    max_len=0
    b=[]
    for row in a:
        c = list(Counter(row).items())
        c.sort(key=lambda x: (x[1], x[0]))
        if len(c)>50:
            c=c[:50]
        d = []
        for num, cnt in c:
            if num==0: continue
            d.append(num)
            d.append(cnt)
        b.append(d)
        max_len=max(max_len,len(d))

    for i in range(l):
        row=b[i]
        if len(row)<max_len:
            b[i]+=[0]*(max_len-len(row))
            if len(b[i]) > 50:
                b[i] = b[i][:50]

    return b

def transpose(a):
    return list(map(list,zip(*a)))

def C(a,m):
    return transpose(R(transpose(a),m))

def check(time):
    if r<=n-1 and c<=m-1:
        if a[r][c]==K:
            print(time)
            sys.exit(0)

check(0)
for time in range(1,MAX+1):

    if n>=m:
        a=R(a,n)
    else:
        a=C(a,m)

    n=len(a)
    m=len(a[0])

    check(time)

print(-1)