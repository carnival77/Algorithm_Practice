# python 의 슬라이싱으로 특정 문자열을 생성하는 것은 매번 새로운 객체를 만들어내는 O(n) 연산. 따라서 문자열 슬라이싱을 사용할 경우 전체 시간복잡도 = O(N^2)
# 반면, 스택을 사용할 경우, 전체 시간복잡도는 O(n*m) = O(n)
# [풀이 시간]
# 1회 : 약 1시간 20분.

a=list(input())
s=[]
n=len(a)

for inx in range(n):
    s.append(a[inx])
    if a[inx]=='P' and len(s)>=4 and s[-4:]==list('PPAP'):
        for _ in range(3):
            s.pop()

if s==['P']:
    print('PPAP')
else:
    print('NP')