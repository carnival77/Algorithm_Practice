n=int(input())
m=int(input())

ans=abs(n-100)

b=[False]*10  #  고장난 버튼은 True
if m > 0:
    a = list(map(int,input().split()))
else:
    a = []
for x in a:
    b[x]=True

def nums_possible(c):
    if c==0:
        if b[c]:
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