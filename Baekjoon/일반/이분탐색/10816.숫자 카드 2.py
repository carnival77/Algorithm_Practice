from collections import defaultdict

n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
d=defaultdict(int)

ans=[]
a.sort()

for target in b:
    start=0
    end=len(a)-1
    while start<=end:
        mid = (start + end) // 2
        if target==a[mid]:
            if d[target] == 0:
                d[target] += 1
                i=1
                while mid-i>=start:
                    if a[mid-i]==target:
                        d[target] += 1
                        i += 1
                    else:
                        break
                i=1
                while mid+i<=end:
                    if a[mid+i]==target:
                        d[target]+=1
                        i += 1
                    else:
                        break
            break
        elif target>a[mid]:
            start=mid+1
        else:
            end=mid-1

for i in b:
    ans.append(d[i])

print(" ".join(map(str,ans)))