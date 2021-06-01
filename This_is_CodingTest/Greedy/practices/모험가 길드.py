n = int(input())

arr = list(map(int,input().split()))

arr.sort()

cnt=0

for i in arr:
    if n>0 :
        n = n- i
        for a in range(i):
            arr.remove(min(arr))
        cnt+=1
    else:
        break

print(cnt)
