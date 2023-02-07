n=int(input())
a=list(map(int,input().split()))
# d[i] = a[1]...a[i] 까지의 수열이 있을 때, a[i]를 마지막으로 하는 가장 긴 증가하는 부분수열의 길이
d=[1]*n

for i in range(n):
    for j in range(i):
        # 조건에 맞으려면, a[1] ... a[j],a[i] 수열이 있으면, j<i , a[j] < a[i]. 이어야 한다.
        # a[j]<a[i] 인 상태에서, d[j] 에 a[i] 1개를 추가한 길이가 d[i]보다 크면, d[i]는 d[j] 에 a[i] 1개를 더한 길이로 변경해준다.
        if a[i]>a[j]:
            d[i]=max(d[j]+1,d[i])

print(max(d))