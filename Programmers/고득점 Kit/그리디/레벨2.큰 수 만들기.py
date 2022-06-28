## 시도 1. 조합과 순열. 역시 시간 초과. 왜냐하면 number는 1백만 이하의 숫자이므로.

# from itertools import combinations
#
# def solution(number, k):
#     answer = 0
#
#     for num in combinations(number,len(number) - k):
#         answer = max(int("".join(num)),answer)
#
#     return str(answer)

## 시도 2. i번째와 i+1번째를 비교하기. 테스트케이스는 모두 통과하나, 뭔가 논리상의 문제가 있는 듯하다.

# def solution(number, k):
#     need=len(number)-k
#
#     # print(need)
#
#     # answer=[0]*need
#
#     answer=[]
#
#     # print(answer)
#
#     i=0
#     ans_inx=0
#
#     while True:
#         if i+need == len(number):
#             answer ="".join(map(str,answer)) + "".join(number[i:])
#             break
#         elif i+need < len(number):
#             if i+1 <= len(number) -1:
#                 if number[i]>=number[i+1]:
#                     if ans_inx>0:
#                         if answer[ans_inx-1] >= number[i]:
#                             # answer[ans_inx] = number[i]
#                             answer.append(number[i])
#                             ans_inx+=1
#                             need-=1
#                         else:
#                             answer[ans_inx-1] = number[i]
#                     else:
#                         # answer[ans_inx] = number[i]
#                         answer.append(number[i])
#                         ans_inx+=1
#                         need-=1
#         i+=1
#
#     print(answer)
#
#     return answer
#
# number = "4177252841"
# k = 4
#
# print(solution(number,k))

## 시도 3. stack을 활용하여, stack 맨 위의 값이 넣을 값보다 작다면 넣을 값 중 크거나 같은 값이 나올 때까지 pop.
# pop할 때마다 k - 1. 왜냐하면 해당 숫자를 제거하는 것이기 때문

def solution(number, k):
    answer=[] #stack

    for num in number:
        while k>0 and answer and answer[-1] < num:
            answer.pop()
            k-=1
        answer.append(num)

    return "".join(answer[:len(answer)-k]) # 제거 횟수를 다 사용하지 않았을때 남은 횟수만큼 리스트 뒷부분을 자름