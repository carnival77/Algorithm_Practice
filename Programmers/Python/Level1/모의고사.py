def solution(answers):

    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    correct = [0,0,0]

    for i, a in enumerate(answers):
        if a == supo1[i%len(supo1)]:
            correct[0] = correct[0] + 1
        if a == supo2[i%len(supo2)]:
            correct[1] = correct[1] + 1
        if a == supo3[i%len(supo3)]:
            correct[2] = correct[2] + 1

    answer=[]

    for person,score in enumerate(correct):
        if max(correct)== score:
            answer.append(person+1)

    return answer

##
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    answer=[1,3,2,4,2] # 0,1,3,3,5,6. 3

    # citations = [4,4,2,2,1] # 1,2,2,4,4. 2
    print(solution(answer))


