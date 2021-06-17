# <1> my solution
#
# @ 아이디어
# - 주어진 숫자들 중 2개를 고르는 조합을 수행한다.
# -
# - 큰 숫자로 이뤄진 조합에 최댓값, 최솟값 각각의 경우에 아래의 서로 다른 사칙연산 우선 순위대로 사칙 연산을 적용한다.
# - 사칙 연산 우선 순위 :
#     최댓값 : 곱셈, 덧셈, 뺄셈, 나눗셈
#     최솟값 :
# - 그 결과를 모두 더한다.
# - 중간에, 음수를 빼거나 곱하거나
#
# @ detailed process
# 1) combinations = combination 2 in N.
# 2) combinations.sort()
# 3) calculations = [1,1,1,1]. index[2] = x, index[0] = +, index[1] = -, index[3] = //
# 4)
#
# @ 아이디어 2
# - 점화식과 재귀함수를 이용한 완전 구현
# - 숫자 사이의 각 연산자 자리에 연산자를 하나씩 대입하여 앞에서부터 순차적으로 계산한다. 그리고 그 결괏값 중 최댓값과 최솟값을 반환한다.
#
# @ detailed process
# first_num = input_nums.pop(0)
# for order,input_num in enumerate(input_nums) :


n = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_val = 1e9
max_val = -1e9


def dfs(index, now):
    global min_val, max_val, n, add, sub, mul, div, temp
    global count

    if index == n:
        min_val = min(min_val, now)
        max_val = max(max_val, now)

    else:
        if add > 0:
            add -= 1
            dfs(index + 1, now + arr[index])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(index + 1, now - arr[index])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(index + 1, now * arr[index])
            mul += 1
        if div > 0:
            div -= 1
            dfs(index + 1, int(now / arr[index]))
            div += 1


dfs(1, arr[0])

print(max_val)
print(min_val)
