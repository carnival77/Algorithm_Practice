import sys

n=int(input())

stack=[]
top=0
ans=[]

for _ in range(n):
    num=int(input())
    if top<num:
        for i in range(top+1,num+1):
            stack.append(i)
            ans.append('+')
        top=num
        stack.pop()
        ans.append('-')
    else:
        if num==stack[-1]:
            stack.pop()
            ans.append('-')
        else:
            print('NO')
            sys.exit(0)

for a in ans:
    print(a)