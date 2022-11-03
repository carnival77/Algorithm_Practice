# solution
# 문제 유형 : 재귀 + DP + 해시
# 아래의 코드의 시간복잡도 : 최악의 경우(n=10^12, p=2, q=3) 436개
# 10^12 = 약 2^40, 3^25이므로 모든 경우의 수가 약 1000이라고 하고,
# 수식에서 n을 mod로 나눈 후 내림을 하므로 분자가 줄어 경우의 수가 감소하고,
# 공배수인 6의 경우를 제외하면 확실히 모든 경우의 수는 약 1000 이하.

from collections import defaultdict
import sys
input=sys.stdin.readline
n,p,q=map(int,input().split())
# n,p,q=int(1e12),2,3
# cnt=0
if n==0:
    print(1)
    sys.exit(0)

d=defaultdict(int) # 딕셔너리의 기본 value를 0으로
d[0]=1

def recur(x,mod):
    # global cnt
    k=int(x/mod)
    if d[k]!=0: # 이미 값이 구해졌을 때는 이미 구해진 값을 반환하여 경우의 수 줄이기
        return d[k]
    d[k]=recur(k,p)+recur(k,q)

    # cnt+=1

    return d[k]

ans=recur(n,p)+recur(n,q)
print(ans)
# print(cnt)