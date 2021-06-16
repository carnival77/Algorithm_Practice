# # 1. my solution
#
# def balance_check(p):
#     balance = 0
#
#     for index, ele in enumerate(p):
#         if ele == '(':
#             balance += 1
#         elif ele == ')':
#             balance -= 1
#         if balance == 0:
#             return index
#
#
# def right_check(u):
#     count=0
#
#     for ele in u:
#         if ele == '(':
#             count+=1
#         else:
#             count-=1
#             if count < 0 :
#                 return False
#     return True
#
#
# def solution(p):
#     answer = ''
#     index = 0
#
#     # 1
#     if p == '':
#         return answer
#
#     # 2
#     index = balance_check(p)
#
#     u = p[:index + 1]
#     v = p[index + 1:]
#
#     # print(" u 1 : "+u)
#     # print(" v : " + v)
#
#     # 3
#     if right_check(u) == True:
#         answer = u + solution(v)
#
#     # 4
#     else:
#         # 4-1
#         answer = '('
#         # print("answer 1 : " + answer)
#         # 4-2
#         answer += solution(v)
#         # print("answer 2 : " + answer)
#         # 4-3
#         answer += ')'
#         # print("answer 3 : " + answer)
#         # 4-4
#         # print("u : "+u)
#         temp = u[1:-1]
#         # print("temp : "+temp)
#         for ele in temp:
#             if ele == ')':
#                 answer += '('
#             elif ele == '(':
#                 answer += ')'
#
#         # 4-5
#         return answer
#
#     return answer
#
# print(solution("(()())()"))

# print(right_check("(()())()"))
#
# print(balance_check("(()())()"))
#
# print(balance_check("))(("))

# 2. book solution

# # "균형잡힌 괄호 문자열"의 인덱스 반환
# def balanced_index(p):
#     count = 0 # 왼쪽 괄호의 개수
#     for i in range(len(p)):
#         if p[i] == '(':
#             count += 1
#         else:
#             count -= 1
#         if count == 0:
#             return i
#
# # "올바른 괄호 문자열"인지 판단
# def check_proper(p):
#     count = 0 # 왼쪽 괄호의 개수
#     for i in p:
#         if i == '(':
#             count += 1
#         else:
#             if count == 0: # 쌍이 맞지 않는 경우에 False 반환
#                 return False
#             count -= 1
#     return True # 쌍이 맞는 경우에 True 반환
#
# def solution(p):
#     answer = ''
#     if p == '':
#         return answer
#     index = balanced_index(p)
#     u = p[:index + 1]
#     v = p[index + 1:]
#
#     print("u 1 : "+u)
#     print("v : " + v)
#
#     # "올바른 괄호 문자열"이면, v에 대해 함수를 수행한 결과를 붙여 반환
#     if check_proper(u):
#         answer = u + solution(v)
#     # "올바른 괄호 문자열"이 아니라면 아래의 과정을 수행
#     else:
#         answer = '('
#         answer += solution(v)
#         answer += ')'
#
#         print("u : "+u)
#
#         u = list(u[1:-1]) # 첫 번째와 마지막 문자를 제거
#         print("u : ",u)
#         for i in range(len(u)):
#             if u[i] == '(':
#                 u[i] = ')'
#             else:
#                 u[i] = '('
#         answer += "".join(u)
#     return answer
#
# print(solution("(()())()"))

# 3. other solution 1

def solution(p):
    if p=='':
        return ''
    right=True
    cnt=0

    # 2
    for index in range(len(p)):
        if p[index] == '(': cnt -=1
        else: cnt += 1
        if cnt > 0 : right=False
        if cnt == 0:
            if right:
                return p[:index+1] + solution(p[index+1:])
            else:
                return '('+solution(p[index+1:])+')'+''.join(list(map(lambda x: '(' if x==')' else ')', p[1:index])))

print(solution("(()())()"))