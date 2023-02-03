n=int(input())
p=[0]+list(map(int,input().split()))
d=[0]*(n+1) # N장의 카드를 구매하는 모든 방법의 수

for i in range(1,n+1):
    for j in range(1,i+1):
        d[i]=max(d[i],d[i-j]+p[j])

print(d[n])