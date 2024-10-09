n=int(input())
m=int(input())
s=str(input())
ans=0
cnt=0
i=0

while i<m:
    if s[i:i+3]=='IOI':
        cnt+=1
        i+=2
        if cnt==n:
            ans+=1
            cnt-=1
    else:
        cnt=0
        i+=1

print(ans)