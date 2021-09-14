#에라토테네스의 체 적용

def solution(n):
    primes = []

    a = [False] * 2 + [True] * (n - 1)

    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False

    answer = len(primes)
    return answer