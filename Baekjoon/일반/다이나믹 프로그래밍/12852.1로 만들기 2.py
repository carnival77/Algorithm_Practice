n=int(input())
d=[0]*(n+1)
d[1]=0
d2=[[] for _ in range(n+1)]
d2[1]=[1]
for i in range(2,n+1):
    d[i]=d[i-1]+1
    d2[i] = [i]+d2[i-1]
    if i%2==0 and d[i] > d[i//2] + 1:
        d[i] = d[i//2] + 1
        d2[i]=[i]+d2[i//2]
    if i%3==0 and d[i] > d[i//3] + 1:
        d[i] = d[i//3] + 1
        d2[i] = [i]+d2[i//3]
print(d[n])
print(" ".join(map(str,d2[n])))