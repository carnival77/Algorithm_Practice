import sys
from itertools import combinations
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
b=set()

for num in range(1,n+1):
    for comb in combinations(a,num):
        b.add(sum(list(comb)))

no=1
while True:
    if no not in b:
        print(no)
        break
    no+=1