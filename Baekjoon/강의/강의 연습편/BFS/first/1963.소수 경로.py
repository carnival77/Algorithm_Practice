# solution 1.
# 에라토스테네스의 체 시간 복잡도 : O(NloglogN)
# 에라토스테네스의 체를 적용해서, 시작 소수와 목표 소수 사이의 모든 소수를 구해 a 배열에 넣는다.
# 이 모든 소수들이 BFS의 정점이다.
# BFS의 가중치는 한 자리만 바뀌는 것이다.
# dist 배열은 목표 소수까지의 변환에 필요한 최소 횟수를 저장한다.

from collections import deque

MAX=10000

# 에라토스테네스의 체
def get_primes(n):
    a=[True]*(MAX+1)
    for i in range(2, n + 1):
        if a[i]:
            for j in range(2 * i, n + 1, i):
                a[j] = False

    return a

t=int(input())
a=get_primes(MAX)
for _ in range(t):
    s,e=map(int,input().split())

    check=[False]*(MAX+1)

    q=deque()
    q.append((s,0))
    check[s]=True
    ok=False

    while q:
        now,cnt=q.popleft()
        # 빼낸 값이 end면 cnt 프린트
        if now==e:
            print(cnt)
            ok=True
            break
        # now를 숫자에서 문자로 변환
        str_now=str(now)
        # 각 자리에 0 ~ 9를 넣어가며 소수인지 확인
        for digit in range(4):
            for num in range(10):
                next = int(str(str_now[:digit])+str(num)+str(str_now[digit+1:]))
                # 방문 X, 소수 O, 1000이상인 숫자
                if next>=1000 and not check[next] and a[next]:
                    q.append((next,cnt+1))
                    check[now]=True

    if not ok:
        print("Impossible")

# 참고 https://cijbest.tistory.com/13