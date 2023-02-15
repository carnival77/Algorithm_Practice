t=int(input())

N=1000000
d=[0]*(N+1)
d[1]=1
d[2]=2
d[3]=4
mod = 1000000009

for i in range(4,N+1):
    d[i]=d[i-1]+d[i-2]+d[i-3]
    d[i]%=mod

for i in range(t):
    n=int(input())
    print(d[n])