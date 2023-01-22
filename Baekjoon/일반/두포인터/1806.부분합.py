import sys
input=sys.stdin.readline
n,s=map(int,input().split())
a=list(map(int,input().split()))

ans=int(1e9)
# 투포인터 풀이
# i,j=0,0
# sum=a[0]
# while j!=n:
#     if sum>=s:
#         ans=min(ans,j-i+1)
#         sum -= a[i]
#         i+=1
#     else:
#         j+=1
#         if j==n:
#             break
#         else:
#             sum+=a[j]
# if ans==int(1e9):
#     print(0)
# else:
#     print(ans)

# 구간합 풀이
a.insert(0,0)
b=[0]*(n+1)
for i in range(1,n+1):
    b[i]=b[i-1]+a[i]
i,j=0,1

while i<n:
    if b[j]-b[i]>=s:
        ans=min(ans,j-i)
        i+=1
    else:
        if j<n:
            j+=1
        else:
            i+=1
if ans==int(1e9):
    print(0)
else:
    print(ans)