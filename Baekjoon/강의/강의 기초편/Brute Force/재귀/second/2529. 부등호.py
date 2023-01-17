from itertools import permutations

k = int(input())
arr = list(input().split())
used=[False]*10
ans=[]
a=[str(i) for i in range(10)]

def check(a):
    for i in range(k):
        if arr[i]=='<' and not (int(a[i])<int(a[i+1])):
            return False
        if arr[i]=='>' and not (int(a[i])>int(a[i+1])):
            return False

    return True

for p in permutations(a,k+1):
    p=list(p)
    if check(p):
        ans.append("".join(p))

ans.sort()
print(ans[-1])
print(ans[0])