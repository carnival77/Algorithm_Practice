import sys
input=sys.stdin.readline

k=int(input().rstrip())
stack=[]
for _ in range(k):
    data=int(input().rstrip())
    if data>0:
        stack.append(data)
    else:
        stack.pop()
print(sum(stack))