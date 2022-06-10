# solution 1.
# 모든 경우의 수를 전부 찾는 완전탐색이면서 BFS를 사용한 문제이다.
#
# 우선 네 자리 수인 9999까지의 모든 수를 완전탐색을 통해서 소수인지 판별을 한다.
#
# 그 다음은 각 자리수마다 숫자(0 ~ 9)를 바꾸어 가며 소수인 수는 큐에 넣어서 또 다시 자릿수를 바꾸어 가며 바꾸어야 하는 숫자가 나올 때 판별한다.
#
# 이 때 다음과 같은 조건을 생각해야 한다.
#
# 큐에 넣은 숫자는 방문 처리를 한다. (visited) - 카운트 중복 방지
# 과정 중에는 네 자리 숫자를 유지해야 하므로 바꾼 숫자가 1000이상인지 확인한다.

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