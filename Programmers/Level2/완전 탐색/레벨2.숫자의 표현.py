
## 70점. 정확성은 통과하나, 효율성에서 탈락
def solution2(n):
    answer = 0

    arr=[0]*n

    for i in range(1,n+1):
        arr[i-1]=i

    for step in range(n,0,-1):
        for inx in range(n-step+1):
            total = sum(arr[inx:inx+step])
            if total>n:
                break
            elif total == n:
                answer+=1

    return answer

# 위와 다르게 배열을 생성하고 그 배열에 값을 삽입할 필요가 없다.
def solution(n):
    answer=0

    for i in range(1,n+1):
        sum=0
        for j in range(i,n+1):
            sum+=j
            if sum==n:
                answer+=1
                break
            elif sum>n:
                break

    return answer

print(solution(15))