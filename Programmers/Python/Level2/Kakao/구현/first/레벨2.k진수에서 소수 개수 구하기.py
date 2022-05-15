def change(n,k):
    tmp=''

    while n>0:
        n,mod=divmod(n,k)
        tmp+=str(mod)

    return tmp[::-1]

def is_prime(num):
    if num == 1: return False

    for i in range(2, int(num**0.5)+1):
        if num % i == 0: return False
    return True

def solution(n, k):
    answer = 0
    n=change(n,k)
    l=n.split('0')
    for e in l:
        if e.isdigit():
            if is_prime(int(e)):
                answer+=1

    return answer