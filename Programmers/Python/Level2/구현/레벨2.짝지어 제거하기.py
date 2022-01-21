# def solution(s):
#     answer = -1
#
#     flag=0
#
#     s=list(s)
#
#     while True:
#         ok=False
#
#         if s==[]:
#             answer=1
#             break
#         elif len(s)==1:
#             answer=0
#             break
#
#         for i in range(flag,len(s)-1):
#             if s[i]==s[i+1]:
#                 ok=True
#
#                 s.pop(i+1)
#                 s.pop(i)
#                 flag=0
#
#                 break
#
#         if ok==False:
#             return 0
#
#     return answer

def solution(s):
    answer = -1

    stack=[]

    for a in s:
        if len(stack) == 0: stack.append(a)
        elif stack[-1] == a: stack.pop()
        else: stack.append(a)

    if len(stack)==0: return 1
    else: return 0

s="baabaa"
# s="cdcd"

print(solution(s))