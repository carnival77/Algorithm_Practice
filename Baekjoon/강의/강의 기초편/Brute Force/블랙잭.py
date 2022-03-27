def solution(n,m,arr):
    answer = 0

    length = n

    for i in range(length):
        for j in range(i+1,length):
            for k in range(j+1,length):
                if arr[i]+arr[j]+arr[k]> m:
                    continue
                else:
                    answer=max(answer,arr[i]+arr[j]+arr[k])

    return answer

##
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # n=5
    # m=21
    # arr=[5,6,7,8,9]

    n=10
    m=500
    arr=[93,181,245,214,315,36,185,138,216,295]

    print(solution(n,m,arr))


