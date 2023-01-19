# 솔루션
# 1. w와 s의 각 알파벳을 총 알파벳 (a-z, A-Z) 52자리 배열에 실제 존재하면 +1, 그 외엔 0 로 담는다.
# 2. s를 담을 때, 슬라이딩 윈도우 기법을 적용한다.
# 3. 즉, s에 n개씩 담으면서, 담긴 문자열이 w와 같은 지 체크한다. 그리고 슬라이딩 윈도우 왼쪽 것은 빼고, 오른쪽 것은 새로 넣으면서 m까지 탐색한다.

import sys
input=sys.stdin.readline

n,m=map(int,input().split())
w=list(input())
s=list(input())

a=[0]*52
b=[0]*52

ans=0

for i in range(n):
    if w[i].islower():
        a[ord(w[i])-ord('a')]+=1
    else:
        a[ord(w[i])-ord('A')+26]+=1

for i in range(n):
    if s[i].islower():
        b[ord(s[i])-ord('a')]+=1
    else:
        b[ord(s[i])-ord('A')+26]+=1

if a==b:
    ans+=1

for i in range(n,m):
    j=i-n
    if s[i].islower():
        b[ord(s[i])-ord('a')]+=1
    else:
        b[ord(s[i])-ord('A')+26]+=1
    if s[j].islower():
        b[ord(s[j])-ord('a')]-=1
    else:
        b[ord(s[j])-ord('A')+26]-=1
    if a==b:
        ans+=1

print(ans)