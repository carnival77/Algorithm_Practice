def solution(n,m,k,arr):
    answer = 0

    arr.sort(reverse=True)
    first=arr[0]
    second=arr[1]
    sum=0


    # first solution

    # while m>0:
    #     for i in range(k):
    #         sum+=first
    #         m-=1
    #     sum+=second
    #     m-=1

    # second solution

    count = int(m/(k+1)) * k + m%(k+1)

    sum += count*first
    sum += (m-count) * second


    return sum

##
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    n=5
    m=8
    k=3
    arr=[2,4,5,4,6]

    print(solution(n,m,k,arr))


