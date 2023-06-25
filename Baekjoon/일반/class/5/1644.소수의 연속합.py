import math
import sys
input=sys.stdin.readline

n=int(input())
ans=0

def getDecimal(n):
    arr=[0]*(n+1)
    for i in range(2,n+1):
        arr[i]=i

    for i in range(2,int(math.sqrt(n))+1):
        if arr[i]==0:
            continue
        for j in range(i+i,n+1,i):
            arr[j]=0

    return arr

a=getDecimal(n+1)
b=[]

for i in a:
    if i!=0:
        b.append(i)

k=len(b)
start_inx=0
end_inx=0
sum=b[0]

while end_inx!=k:
    if sum==n:
        ans+=1
        end_inx+=1
        if end_inx==k: break
        sum+=b[end_inx]
    elif sum>n:
        sum-=b[start_inx]
        start_inx+=1
    else:
        end_inx+=1
        if end_inx == k: break
        sum+=b[end_inx]

print(ans)