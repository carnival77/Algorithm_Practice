n=int(input())
s=1
cnt=1
left=1
right=1

while right<n:
    if s==n:
        cnt+=1
        right+=1
        s+=right
    elif s<n:
        right+=1
        s+=right
    else:
        s-=left
        left+=1

print(cnt)