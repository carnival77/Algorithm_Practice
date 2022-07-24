# solution.
# n은 최대 20인데, 0부터 20 미만까지의 20개의 수를 순열로 나열하는 것은, 20P20 = 20!이므로 시간 초과다.
# 관점을 바꿔, 0을 n/2개, 1을 n/2개 가진 수열을 순열로 나열한다면, 0과 1이라는 같은 수를 가지므로 최악의 경우의 경우의 수는 최대 20!/(10!*10!) 이고, 이것은 약 20만 이하다.
# but, next_permutation 이 아닌, 일반 permutation을 쓰면 시간 초과.

# from itertools import permutations, combinations
#
# n=int(input())
# k=n//2
# s=[list(map(int,input().split())) for _ in range(n)]
# ans=1e9
# arr=[0 if i<n/2 else 1 for i in range(n)]
#
# for perm in permutations(arr,n):
#     start,link=[],[]
#     a,b=0,0
#     for i in range(n):
#         if perm[i]==0:
#             start.append(i)
#         else:
#             link.append(i)
#     for i, j in combinations(start, 2):
#         a += s[i][j] + s[j][i]
#     for i, j in combinations(link, 2):
#         b += s[i][j] + s[j][i]
#     ans = min(ans, abs(a - b))
# print(ans)

def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1

    a[i-1],a[j] = a[j],a[i-1]

    j = len(a)-1
    while i < j:
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1

    return True

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
b = [0 if i < n/2 else 1 for i in range(n)]
ans = 2147483647
while True:
    first = []
    second = []
    for i in range(n):
        if b[i] == 0:
            first.append(i)
        else:
            second.append(i)
    one = 0
    two = 0
    for i in range(n//2):
        for j in range(n//2):
            if i == j:
                continue
            one += a[first[i]][first[j]]
            two += a[second[i]][second[j]]
    diff = abs(one-two)
    if ans > diff:
        ans = diff
    if not next_permutation(b):
        break
print(ans)