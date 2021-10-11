# 출처 : https://hongcoding.tistory.com/64

# 솔루션
# 1. w와 s의 각 알파벳을 총 알파벳 (a-z, A-Z) 52자리 배열에 실제 존재하면 +1, 그 외엔 0 로 담는다.
# 2. s를 담을 때, 슬라이딩 윈도우 기법을 적용한다.
# 3. 즉, s에 n개씩 담으면서, 담긴 문자열이 w와 같은 지 체크한다. 그리고 슬라이딩 윈도우 왼쪽 것은 빼고, 오른쪽 것은 새로 넣으면서 m까지 탐색한다.

import sys

input=sys.stdin.readline

n,m = map(int,input().split())

# w=input()
#
# s=input()

w = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()

# print(w)

ans=0

# 알파벳 문자열. 0~25 까지의 26자리는 소문자 알파벳(a-z), 26~51까지의 26자리는 대문자 알파벳(A-Z)
wl = [0] * 52
sl = [0] * 52

# 1. w 담기
for i in range(n):
    # a-z
    if 'a' <= w[i] <= 'z':
        wl[ord(w[i])-ord('a')]+=1
    # A-Z. 대문자 알파벳. 26을 더해 26번째부터 채워준다.
    else:
        wl[ord(w[i])-ord('A') + 26] +=1

length,left=0,0
# 2. s 담기. 슬라이딩 윈도우 기법 적용
for i in range(m):
    # a-z
    if 'a' <= s[i] <= 'z':
        sl[ord(s[i])-ord('a')]+=1
    # A-Z. 대문자 알파벳. 26을 더해 26번째부터 채워준다.
    else:
        sl[ord(s[i])-ord('A') + 26] +=1
    length+=1

    # 3. 즉, s에 n개씩 담으면서, 담긴 문자열이 w와 같은 지 체크한다. 그리고 슬라이딩 윈도우 왼쪽 것은 빼고, 오른쪽 것은 새로 넣으면서 m까지 탐색한다.
    if length==n:
        # 담긴 문자열 sl이 wl와 같은 지 체크한다.
        if sl==wl:
            ans+=1
        # 그리고 슬라이딩 윈도우 왼쪽 것은 빼고, 오른쪽 것은 새로 넣으면서 m까지 탐색한다.
        # a-z
        if 'a' <= s[left] <= 'z':
            sl[ord(s[left]) - ord('a')] -=1
        # A-Z. 대문자 알파벳. 26을 더해 26번째부터 채워준다.
        else:
            sl[ord(s[left]) - ord('A') + 26] -=1
        length-=1
        left+=1

print(ans)