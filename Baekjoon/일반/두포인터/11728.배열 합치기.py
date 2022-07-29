n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

# print(*sorted(a+b))
a.sort()
b.sort()
left_index=0
right_index=0
ans=[]

while left_index<n and right_index<m:
    if a[left_index]<b[right_index]:
        ans.append(a[left_index])
        left_index+=1
    else:
        ans.append(b[right_index])
        right_index+=1
ans+=a[left_index:]
ans+=b[right_index:]

print(*ans)