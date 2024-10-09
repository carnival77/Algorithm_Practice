# 마이너스 기호를 만날 때 ( 괄호를 쳐 주고, 다음 마이너스가 나오면 이전에 ( 괄호가 있는 상태이면 )을 치고 또 (를 친다. 다음 마이너스가 없다면 끝까지 모든 수를 더해서 한 번에 빼 준다.
# solution 1. 직접 (,)를 넣어서 eval 함수로 처리

# import sys,re
# input=sys.stdin.readline
#
# data=list(input().rstrip())
# braket = False
# need=False
#
# for i,a in enumerate(data):
#     if a=='-':
#         if not braket:
#             data.insert(i+1,'(')
#             braket=True
#         else:
#             data.insert(i,')')
#             braket=False
#         need=True
#     else:
#         continue
# if need:
#     data+=[')']
# data="".join(data)
# expression=re.split('([-|+|)|(])',data)
# for i,e in enumerate(expression):
#     if e.isdigit():
#         expression[i]=int(e)
# for i,e in enumerate(expression):
#     if type(e)==int:
#         expression[i]=str(e)
# expression=''.join(expression).split()
#
# print(eval("".join(expression[0])))

# 마이너스 기호를 만날 때 다음 마이너스 까지, 다음 마이너스가 없다면 끝까지 모든 수를 더해서 한 번에 빼 준다.
# solution 2.
import sys
input=sys.stdin.readline

data=input().split('-')
s=0
for i in data[0].split('+'):
    s+=int(i)
for i in data[1:]:
    for j in i.split('+'):
        s-=int(j)
print(s)
