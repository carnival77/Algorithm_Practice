t=int(input())
m=3
MAX=100000
nums=[1,2,3]
d=[0]*(MAX+1)
d[0]=1

for j in range(m):
    for i in range(1,MAX+1):
        if i-nums[j]>=0:
            d[i]+=d[i-nums[j]]

for _ in range(t):
    print(d[int(input())])