import sys
input=sys.stdin.readline

n=int(input())
a=list(input())
s=list(['' for _ in range(n)] for _ in range(n))
ans=[]
inx=0

for i in range(n):
    for j in range(i,n):
        s[i][j]=a[inx]
        inx+=1

def check(inx):
    sum=0
    for i in range(inx,-1,-1):
        # ans[inx] ~ ans[i] 의 합
        sum+=ans[i]

        # sum의 부호와 s[i][inx]가 일치
        if s[i][inx]=='+' and not sum>0: return False
        if s[i][inx]=='-' and not sum<0: return False
        if s[i][inx]=='0' and not sum==0: return False
    return True

def dfs(inx):
    # 모든 조건을 만족하는 경우
    if inx==n:
        print(*ans)
        sys.exit(0)
    # -10~10
    for i in range(-10,11):
        ans.append(i)
        # inx번째까지의 숫자가 모든 조건을 만족한다면 inx+1번째로 진행
        if check(inx):
            dfs(inx+1)
        ans.pop()

dfs(0)