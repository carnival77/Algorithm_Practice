# 탐색 범위를 + - 를 고려해서 주어진 것의 두 배를 하는 것
# 탐색 범위에서 1씩 올려가며 클릭 가능한 숫자를 파악하여 가장 답에 근접한 숫자를 먼저 찾는 것
# pmpress = + - 를 누르는 횟수를 주어진 숫자 - c를 하고 위에서 구한 숫자를 누르는 횟수를 더한 것의 최솟값을 찾는 것

n = int(input())

m = int(input())

broken=[False] * 10

broken_numbers = list(map(int,input().split()))

for i in broken_numbers:
    broken[i] = True

ans=abs(n-100)

# C에 포함되어 있는 숫자 중 고장난 버튼이 있는지 확인한다.
# 수를 10으로 계속해서 나누면서 각 자릿수의 수를 검사한다.
def nums_possible(c):
    if c==0:
        if broken[c]==True:
            return 0
        else:
            return 1
    cnt=0
    while c>0:
        if broken[int(c%10)] == True:
            return 0
        else:
            c//=10
            cnt+=1
    return cnt

# 숫자 버튼을 눌러 이동할 채널 C를 정한다.
for i in range(1000001):
    c=i
    pmpress=0
    # C에 포함되어 있는 숫자 중 고장난 버튼이 있는지 확인한다.
    # 고장난 버튼이 있으면, 해당 채널로는 숫자를 입력해서 이동할 수 없으므로 0을 반환한다.
    # 고장난 버튼이 없다면, 해당 채널로 가기 위해 입력해야 하는 숫자의 횟수를 반환한다.
    nums_cnt = nums_possible(c)
    # 고장난 버튼이 포함되어 있지 않다면 |C-N|을 계산해 +나 - 버튼을 몇 번 눌러야 하는지 구한다.
    if nums_cnt > 0:
        pmpress = abs(n-c)
        if ans > (nums_cnt + pmpress):
            ans = nums_cnt + pmpress

print(ans)

# n = int(input())
# m = int(input())
# broken = [False] * 10
# if m > 0:
#     a = list(map(int,input().split()))
# else:
#     a = []
# for x in a:
#     broken[x] = True
# def possible(c):
#     if c == 0:
#         if broken[0]:
#             return 0
#         else:
#             return 1
#     l = 0
#     while c > 0:
#         if broken[c%10]:
#             return 0
#         l += 1
#         c //= 10
#     return l
# ans = abs(n-100)
# for i in range(0, 1000000+1):
#     c = i
#     l = possible(c)
#     if l > 0:
#         press = abs(c-n)
#         if ans > l + press:
#             ans = l + press
# print(ans)