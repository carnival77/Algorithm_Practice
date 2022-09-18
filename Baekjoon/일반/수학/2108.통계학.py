import sys
from collections import Counter
input=sys.stdin.readline

n = int(input())
nums=[]
for i in range(n):
    nums.append(int(input()))

a=int(round(sum(nums)/n,0))
nums.sort()
b=nums[n//2]
c=0
cnt=Counter(nums)
tmp=cnt.most_common()
k=tmp[0][1]
tmp2=[]
for t in tmp:
    if t[1]==k:
        tmp2.append(t[0])
# 최빈값이 1개
if len(tmp2)<=1:
    c=tmp2[0]
# 최빈값이 2개 이상
else:
    tmp2.sort()
    c = tmp2[1]
d=max(nums)-min(nums)
print(a)
print(b)
print(c)
print(d)