#!/usr/bin/env Python
# coding=utf-8

#solution 1.
# def process(stack,st):
#     for s in st:
#         if s not in stack:
#             continue
#         else:
#             top = stack[-1]
#             if s == top:
#                 stack.pop()
#                 continue
#             else:
#                 return 0
#     return 1
#
# def solution(skill, skill_trees):
#     ans=0
#     for st in skill_trees:
#         stack = list(i for i in skill[::-1])
#         ans+=process(stack,st)
#     return ans

#solution 2.
def solution(skill, skill_trees):
    ans = 0
    for skill_tree in skill_trees:
        l=list(skill)
        for s in skill_tree:
            if s in l:
                if s!=l.pop(0):
                    break
        else:
            ans+=1
    return ans

skill="CBD"
skill_trees=["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill,skill_trees))