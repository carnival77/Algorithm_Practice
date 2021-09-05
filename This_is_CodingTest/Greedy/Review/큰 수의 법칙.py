n,m,k = map(int,input().split())

arr = list(map(int,input().split()))

arr.sort(reverse=True)

first = arr[0]
second = arr[1]
answer=0


while(m>0):
    for _ in range(k):
        answer += first
        m -= 1
    answer+=second
    m -= 1

print(answer)