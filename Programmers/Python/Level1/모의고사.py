def solution(answers):
    
    answer = []

    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    correct = [0] * 3

    for i, a in enumerate(answers):
        if a == supo1[i]:
            correct[0] = correct[0] + 1
        if a == supo2[i]:
            correct[1] = correct[2] + 1
        if a == supo3[i]:
            correct[2] = correct[2] + 1

    corrects = []

    for i, n in enumerate(correct):
        corrects.append((i, n))

    # print(corrects)

    corrects.sort(key=lambda x: x[1], reverse=True)

    for x in corrects:
        if corrects[0][1] <= x[1]:
            answer.append(x[0])

    return list(map(lambda x: x + 1, answer))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    answer=[1,3,2,4,2] # 0,1,3,3,5,6. 3

    # citations = [4,4,2,2,1] # 1,2,2,4,4. 2
    print(solution(answer))


