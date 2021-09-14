cnt = 0

def go(start, n, student,k):
    global cnt
    arr = []
    k_num=0
    for i in range(start, n):
        for j in range(start, i + 1):
            arr.append(student[j])
        for ele in arr:
            if ele == 1:
                k_num+=1
        if k_num == k:
            cnt+=1
        arr = []
        k_num = 0


def solution(student, k):
    global cnt
    n = len(student)

    for i in range(n):
        go(i, n, student,k)

    answer = cnt
    return answer

# input_data = input()
# k = int(input())

print(solution([0,1,0,0],1))