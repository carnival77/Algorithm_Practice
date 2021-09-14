def solution(s):
    result = ''

    temp = ''

    result_arr = []

    arr = s.split(" ")

    for part in arr:
        for inx, ele in enumerate(part):
            if inx % 2 == 0:
                temp += ele.upper()
            elif inx % 2 == 1:
                temp += ele.lower()
        result_arr.append(temp)
        temp = ''

    result = " ".join(result_arr)

    return result