from collections import deque

# solution 1. 큐 사용
def solution(prices):
    answer = []

    q=deque(prices)

    while q:
        p=q.popleft()
        sec=0
        for next_p in q:
            sec+=1
            if next_p < p:
                break
        answer.append(sec)

    return answer

# solution 2. 이중 for문 사용
def solution2(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

# solution 3. stack 사용
# 참고 : https://velog.io/@soo5717/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A3%BC%EC%8B%9D%EA%B0%80%EA%B2%A9-Python
def solution3(prices):

    length = len(prices)

    # answer을 모든 시점에서 각각의 최댓값으로 설정
    answer = [i for i in range(length-1,-1,-1)]

    # 주식 가격이 떨어질 경우 찾기
    stack=[0]
    for i in range(1,length):
        while stack and prices[stack[-1]] > prices[i]:
            j=stack.pop()
            answer[j]=i-j
        stack.append(i)

    return answer