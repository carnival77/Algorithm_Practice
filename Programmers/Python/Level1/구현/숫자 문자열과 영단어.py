def solution(s):
    #         answer = ''

    #     tdict = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}

    #     i=0

    #     n=len(s)

    #     while i<n:
    #         if s[i].isdigit():
    #             answer+=str(s[i])
    #             i+=1
    #         else:
    #             for step in range(3,6):
    #                 tg = s[i:i+step]
    #                 if tg in tdict:
    #                     answer += str(tdict[tg])
    #                     i+=step
    #                     break

    #     return int(answer)

    tdict = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
             "eight": "8", "nine": "9"}

    answer = s
    for key, values in tdict.items():
        answer = answer.replace(key, values)

    return int(answer)