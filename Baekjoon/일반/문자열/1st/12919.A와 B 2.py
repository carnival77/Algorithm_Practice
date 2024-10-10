# [풀이 시간]
# 1회 : 약 55분. 풀이 참고 O.
# [접근 방식]
# 1. S에서 문자 2개 중 하나를 선택하여 T를 만드는 방식 : 시간복잡도 O(2^n).
# 2. T에서 두 가지 경우의 수로 문자 하나를 제거하여 S를 만드는 방식 : 불필요한 경우의 수 제거
# 1번의 경우, 가령 S=[A], T=임의의 20자리 문자 A*20 와 같은 경우의 수도 고려하게 된다.

a=list(input())
b=list(input())
ans=0

def dfs(b):
    global ans

    if ans==1:
        return

    n=len(a)
    m=len(b)

    if n>m:
        return
    if n==m and a!=b:
        return

    if a==b:
        ans=1
        return

    tmp = b[:]
    t=tmp[-1]
    if t=='A':
        tmp.pop()
        dfs(tmp)
    tmp = b[:]
    tmp.reverse()
    if tmp[-1]=='B':
        tmp.pop()
        dfs(tmp)

dfs(b[:])

print(ans)