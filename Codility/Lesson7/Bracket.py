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