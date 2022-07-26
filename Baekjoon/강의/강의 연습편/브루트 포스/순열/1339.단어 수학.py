# 문제의 시간 제한이 너무 작아 파이썬으로는 시간 초과가 날 수 밖에 없다.
from collections import Counter
from itertools import permutations

n=int(input())
words=[]
ans=0
all=''
for _ in range(n):
    word=input()
    words.append(word)
    all+=word

c=Counter(all)
used=list(c.keys())
k=len(used)
arr=list(i for i in range(10))
arr.sort(reverse=True)
arr=arr[:k]

for perm in permutations(arr,k):
    alp = []
    nums = []
    for num,p in zip(perm,used):
        alp.append(p)
        nums.append(num)
    tmp=0
    for word in words:
        trans=''
        for a in word:
            trans+=str(nums[alp.index(a)])
        tmp+=int(trans)
    ans=max(ans,tmp)
print(ans)