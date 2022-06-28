# solution 1. 투 포인터 사용

# people 오름차순 정렬
#
# left는 0, right는 len(people) - 1의 값을 초기값으로 가짐.
#
# 남은 사람들 중, 가장 무거운 사람과 가장 가벼운 사람 무게의 합이,
# 3-1 limit값 이하일 경우, left는 1 더하기, right는 1 빼기
# 3-2 limit보다 클 경우, right만 1 빼기
#
# 3번 과정을 left가 right보다 작을 때 까지 반복하고, 매 반복 때 마다 answer에 1 더하기
#
# 반복을 마친 뒤, left가 right가
# 5-1 같으면, 한 명이 남은 것이니 answer에 1 더하기
# 5-2 left > right면, 모두 보트를 타고 나간 뒤므로 answer 그대로


def solution(people, limit):
    answer = 0
    people.sort()
    left = 0
    right = len(people) - 1
    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        answer += 1
    if left == right:
        answer += 1

    return answer


def solution2(people,limit):
    people.sort()
    cnt=0
    i=0
    j=len(people)-1
    while i<=j:
        cnt+=1
        if people[j] + people[i] <=limit:
            i+=1
        j-=1

    return cnt

# solution 3. deque 사용한 투 포인터
from collections import deque

def solution(people, limit):
    result = 0
    deque_people = deque(sorted(people))

    while deque_people:
        left = deque_people.popleft()
        if not deque_people:
            return result + 1
        right = deque_people.pop()
        if left + right > limit:
            deque_people.appendleft(left)
        result += 1
    return result



# people=[70, 50, 80, 50]
# people=[70, 80, 50]
people = [30, 20, 10]
limit=100

print(solution(people,limit))