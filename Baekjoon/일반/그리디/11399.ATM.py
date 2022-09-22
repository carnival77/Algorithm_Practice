n=int(input())
p=list(map(int,input().split()))
arr=[]

for i in range(n):
    arr.append([i,p[i]])
arr.sort(key=lambda x:x[1])

ans=0
for i in range(n):
    ans+=(n-i)*arr[i][1]
print(ans)