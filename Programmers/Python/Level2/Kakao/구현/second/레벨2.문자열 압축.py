def solution(s):
    n=len(s)
    ans = n
    result=""

    for step in range(1,n//2+1):
        result=""
        prev=s[0:step]
        cnt=1
        for i in range(step,n,step):
            next=s[i:step+i]
            if prev==next:
                cnt+=1
            else:
                result+=str(cnt)+prev if cnt>=2 else prev
                cnt=1
                prev=next
        result += str(cnt) + prev if cnt >= 2 else prev
        ans=min(n,len(result))
    return ans
s="abcabcdede"
print(solution(s))