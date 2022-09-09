from itertools import combinations
from collections import deque

n = int(input())
nums = list(map(int, input().split()))
spot_inx = list(i for i in range(1, n + 1))
ans = int(1e9)

a = [[] for _ in range(n + 1)]
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(data[0]):
        a[i + 1].append(data[j + 1])

for i in range(1, n + 1):
    a[i].sort()

def process(s):
    need_check = [False] * (n + 1)
    for i in s:
        need_check[i] = True
    s = list(s)
    q = deque()
    start = s[0]
    q.append(start)
    need_check[start] = False
    while q:
        x = q.popleft()
        for y in a[x]:
            if need_check[y]:
                q.append(y)
                need_check[y] = False

    if True in need_check:
        return False
    else:
        return True

def process2(s1, s2,nums):
    return abs(sum(list(nums[i-1] for i in s1)) - sum(list(nums[i-1] for i in s2)))

for i in range(1, n):
    for comb in combinations(spot_inx, i):
        first = set(comb)
        second = set(spot_inx) - first
        first_chk=process(first)
        second_chk=process(second)
        if first_chk and second_chk:
            ans = min(ans, process2(first, second,nums))
if ans!=int(1e9):
    print(ans)
else:
    print(-1)
