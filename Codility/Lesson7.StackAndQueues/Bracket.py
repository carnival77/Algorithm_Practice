"""
아이디어: 스택으로 여는 괄호 푸시, 닫는 괄호 만나면 매칭 검사
시간: O(N), 공간: O(N)
"""

def solution(S):
    arr=list(S)
    N = len(arr)

    if N==0:
        return 1

    if N%2==1:
        return 0

    pair={')':'(',']':'[','}':'{'}

    stack=[]
    for char in arr:
        if char in pair.values():
            stack.append(char)
        else:
            if not stack or pair[char]!=stack[-1]:
                return 0
            else:
                stack.pop()

    return 1 if not stack else 0