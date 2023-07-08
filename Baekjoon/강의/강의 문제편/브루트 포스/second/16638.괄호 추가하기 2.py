import sys
from itertools import combinations
input=sys.stdin.readline

n=int(input())
data=input()
a=[]
for i in range(n):
    a.append(data[i])
k=len(a)//2
cand=[2*i+1 for i in range(k)]
if len(a)==1:
    print(a[0])
    sys.exit(0)
ans=-sys.maxsize

def cal(a,op_inx):
    l=int(a[op_inx-1])
    r=int(a[op_inx+1])
    op=a[op_inx]
    if op=='+':
        return l+r
    elif op=='-':
        return l-r
    else:
        return l*r

def process(b,inx):
    result = str(cal(b, inx))
    b = b[:inx - 1] + [result] + b[inx + 2:]
    return b

def valid(a):
    for i in range(len(a)-1):
        if a[i+1]==a[i]+2:
            return False
    return True

for num in range(k):
    for comb in combinations(cand,num):
        if not valid(comb): continue
        b=a[:]
        comb=tuple(list(comb)[::-1])
        for op_inx in comb:
            b=process(b,op_inx)
        # inx=1
        # while len(b)!=1:
        #     b=process(b,inx)
        # res=int(b[0])
        ans=max(ans,eval(''.join(b)))

print(ans)