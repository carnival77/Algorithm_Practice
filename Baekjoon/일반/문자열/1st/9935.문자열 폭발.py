a=list(input())
b=list(input())
n,m=len(a),len(b)
i=0
stack=[]
while i<n:
    if a[i:i+m]==b:
        # a=a[:i]+a[i+m:] -> 원본 수열 a를 리스트 슬라이싱하여 b와 같은 부분만 제거하면, 리스트 슬라이싱은 O(n)이므로 시간 초과다.
        i=i+m
    else:
        stack.append(a[i])
        if stack[-m:]==b:
            for _ in range(m):
                stack.pop()
        i+=1
if len(stack)==0:
    print("FRULA")
else:
    print("".join(stack))