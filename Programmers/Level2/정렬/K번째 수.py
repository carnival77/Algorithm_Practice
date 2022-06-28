def solution(array, commands):
    answer = []

    # for command in commands:
    #     first=command[0]
    #     last=command[1]
    #     index=command[2]
    #     arr = array[first-1:last]
    #     arr.sort()
    #     answer.append(arr[index-1])

    # for com in commands:
    #     answer.append(list(sorted(array[com[0]-1:com[1]]))[com[2]-1])

    # for com in commands:
    #     i,k,j = com
    #     answer.append(list(sorted(array[i-1:k]))[j-1])

    answer = list(map(lambda x: sorted(array[x[0] - 1:x[1]])[x[2] - 1], commands))

    return answer


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    array=[1, 5, 2, 6, 3, 7, 4]
    commands  = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    solution(array,commands)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
