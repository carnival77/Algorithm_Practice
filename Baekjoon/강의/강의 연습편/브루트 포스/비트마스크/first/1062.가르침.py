import sys
from itertools import combinations
input=sys.stdin.readline

n,k=map(int,input().split())
ans=0
if k<5:
    print(ans)
    sys.exit(0)
elif k==26:
    print(n)
    sys.exit(0)
allSet=set()
b={'a','n','c','t','i'}
wordSets=[]
for _ in range(n):
    wordSet=set(input().strip())
    wordSets.append(wordSet)
    allSet |= wordSet

otherSet=allSet-b
if len(otherSet)<=k-5:
    print(n)
    sys.exit(0)

for comb in combinations(otherSet,k-5):
    tmpSet=b | set(comb)
    cnt=0
    for wordSet in wordSets:
        if wordSet <= tmpSet:
            cnt += 1
    ans=max(ans,cnt)
print(ans)