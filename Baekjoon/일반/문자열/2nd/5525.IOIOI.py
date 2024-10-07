# 약 1시간 풀이. 이전 풀이 참고 O

n=int(input())
m=int(input())
s=input()

cnt=0 # IOI의 개수
ans=0
i=0

while i<m:
    if s[i:i+3]=='IOI':
        i+=2
        cnt+=1
        if cnt==n:
            ans+=1
            cnt-=1
    else:
        i+=1
        cnt=0

print(ans)