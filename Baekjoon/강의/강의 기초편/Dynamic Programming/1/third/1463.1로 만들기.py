n=int(input())
d=[-1]*(n+1) # n을 1로 만들기 위한 최소 연산 횟수
d[0]=0
d[1]=0
for i in range(2,n+1):
    d[i]=d[i-1]+1
    if i%2==0 and d[i]>d[i//2]:
        d[i]=d[i//2]+1
    if i%3==0 and d[i]>d[i//3]:
        d[i]=d[i//3]+1
print(d[n])