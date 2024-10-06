# python 의 슬라이싱은 매번 새로운 객체를 만들어내는 O(n) 연산. 따라서 문자열 슬라이싱을 사용할 경우 전체 시간복잡도 = O(N^2)
# 반면, 스택을 사용할 경우, 전체 시간복잡도는 O(n*m) = O(n)
# 풀이 시간 : 약 1시간. 이전 풀이 참고 O

a=list(input())
b=list(input())
n=len(a)
m=len(b)
s=[]

i=0
while i<n:
    if a[i:i+m]==b:
        i+=m
    else:
        s.append(a[i])
        if s[-m:]==b:
            # s=s[:-m]
            for _ in range(m):
                s.pop()
        i+=1
if len(s)==0:
    print("FRULA")
else:
    print("".join(s))