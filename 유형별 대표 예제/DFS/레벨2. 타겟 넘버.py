# 조합 문제. N개 중 M개를 선택하여 중복 허용 X, 순서 상관하며 사용. 즉, 순서가 달라도 같은 요소로 구성되어 있으면 같은 집합
#
from itertools import combinations

answer=0

def dfs(numbers,index,sum,n):
    global answer
    # 종료 조건
    if index == n and sum == target:
        answer+=1
        return
    if index==n:
        return

    dfs(numbers,index+1,sum+numbers[index],n)
    dfs(numbers, index + 1, sum - numbers[index], n)

def solution(numbers, target):
    n=len(numbers)
    dfs(numbers,0,0,len(numbers))
    return answer

numbers=[1, 1, 1, 1, 1]
target=3

print(solution(numbers,target))