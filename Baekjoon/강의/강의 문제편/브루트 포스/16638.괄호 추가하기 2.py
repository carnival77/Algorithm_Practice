# solution.
# 비트마스크, 브루트포스 문제
# 연산자의 개수 m=(n-1)/2 이고, n은 19 이하이므로, m의 최댓값은 9다.
# 시간복잡도 : 각 연산자가 괄호에 포함되는지 아닌지로 구분되기에, 모든 경우의 수는 최대 2^9=512 이다.
# 각 자리의 연산자가 포함되면 1로, 포함되지 않으면 0으로 생각하여, 비트마스크로 구분한다.
# 각 괄호는 연산자를 하나만 포함할 수 있으므로, 연산자 비트마스크의 모양은 010, 101, 100, 000 등 1이 연속되지 않을 때 가능하다.

import sys
input=sys.stdin.readline

n=int(input())
a=list(input().rstrip())
ans=int(-1e9)

m=(n-1)//2

for s in range(1<<m):
    ok=True
    for i in range(m-1):
        if s&(1<<i)>0 and s&(1<<(i+1))>0:
            ok=False
    if not ok:
        continue
    b=a[:]
    for i in range(m):
        if s&(1<<i)>0:
            k=2*i+1
            b[k-1]='('+b[k-1]
            b[k+1]=b[k+1]+')'
    res=eval("".join(map(str,b)))
    ans=max(ans,res)
print(ans)