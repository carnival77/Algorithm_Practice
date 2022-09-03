n=int(input())
d=[0]*(n+1)
d[0]=1

for i in range(2,n+1,2):
    d[i]=3*d[i-2]
    k=2
    while i-2*k>=0:
        d[i]+=d[i-2*k]*2
        k+=1

print(d[n])