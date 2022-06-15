n=int(input())
data=list(map(int,input().split()))
ans=0

for num in data:
    check=True
    for i in range(2,num):
        if num%i==0:
            check=False
            break
    if check and num!=1:
        ans+=1
print(ans)