n=int(input())
m=int(input())

ans=abs(n-100)

b=[False]*10  #  고장난 버튼은 True
for x in list(map(int,input().split())):
    b[x]=True

def nums_possible(c):
    if c==0:
        if b[0]:
            return 0
        else:
            return 1
    cnt=0
    while c>0:
        if b[int(c%10)]:
            return 0
        else:
            cnt+=1
            c//=10
    return cnt

for c in range(1000001):
    press=nums_possible(c)
    if press>0:
        ans=min(ans,press+abs(n-c))

print(ans)