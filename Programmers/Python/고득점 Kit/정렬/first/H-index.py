def solution(citations):

    citations.sort()

    # n= len(array)

    # for i,e in enumerate(citations):
    #     # n = len(citations[i:])
    #     if e>=len(citations[i:]):
    #         return len(citations[i:])

    n = len(citations)

    for i in range(n):
        if citations[i] >= n-i:
            return n-i



    # return answer


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    citations=[3,0,6,1,5,3] # 0,1,3,3,5,6. 3

    # citations = [4,4,2,2,1] # 1,2,2,4,4. 2
    print(solution(citations))


