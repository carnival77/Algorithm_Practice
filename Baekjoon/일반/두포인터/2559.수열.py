import sys
n,k=map(int,input().split())
a=list(map(int,input().split()))

left_index=0
right_index=k-1
ans=-sys.maxsize
s=sum(a[left_index:right_index+1])

while True:
    if s>ans:
        ans=s
    s-=a[left_index]
    left_index+=1
    right_index += 1
    if right_index>=n:
        break
    s+=a[right_index]

print(ans)