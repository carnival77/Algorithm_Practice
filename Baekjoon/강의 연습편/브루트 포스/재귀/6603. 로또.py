def recur(a,index,arr):
    # 종료 조건
    # 정답을 찾은 경우
    if len(arr) == 6:
        print(' '.join(map(str,arr)))
        return
    # 불가능한 경우
    if index == len(a):
        return
    recur(a,index+1,arr+[a[index]])
    recur(a,index+1,arr)


while(1):
    data = list(map(int,input().split()))

    if data[0] == 0:
        break

    k = data[0]
    a = data[1:]
    arr=[]

    recur(a,0,arr)
    print()