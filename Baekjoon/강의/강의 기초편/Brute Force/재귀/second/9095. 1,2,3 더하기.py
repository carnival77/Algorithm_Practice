from itertools import product

t = int(input())

arr=[1,2,3]
for _ in range(t):
    n=int(input())
    ans=0
    for i in range(1,n+1):
        for pd in product(arr,repeat=i):
            if sum(pd)==n:
                ans+=1
    print(ans)