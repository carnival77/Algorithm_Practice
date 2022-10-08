t=int(input())

d=[0]*12 # 1,2,3으로 정수 N을 만드는 모든 방법의 수
d[1]=1
d[2]=2
d[3]=4

def dp(n):
    for i in range(4,n+1):
        d[i] = d[i-1]+d[i-2]+d[i-3]

    return d[n]

for i in range(t):
    n=int(input())
    print(dp(n))