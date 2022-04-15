from collections import Counter

def solution2(genres, plays):
    genres_dict = {}
    genres_list = []
    for i in range(len(genres)):
        if genres[i] not in genres_dict:
            genres_dict[genres[i]] = []
        genres_dict[genres[i]].append([i, plays[i]])

    for g in genres_dict:
        genres_dict[g].sort(key=lambda x: x[1], reverse=True)
        genres_list.append([g, sum([play for _, play in genres_dict[g]])])

    genres_list.sort(key=lambda x: x[1], reverse=True)
    answer = []
    for g, _ in genres_list:
        answer.extend([x[0] for x in genres_dict[g][:2]])
    return answer

# 내 풀이 : dict에서 요소를 더 추가할 때 list로 key값을 설정한 뒤 append하면 된다. 그리고 lambda식과 sum을 활용하자
def solution(genres, plays):

    answer= []

    genre_cnt = Counter(genres)

    all=[]
    i=0
    for gen, play in zip(genres, plays):
        all.append([gen,i,play])
        i += 1

    all.sort(key=lambda x:x[2],reverse=True)
    # print(all)

    play_num=list()

    for genre  in genre_cnt.keys():
        play_num.append([genre,0])

    for genre in genre_cnt.keys():
        for gen,play in zip(genres,plays):
            if genre==gen:
                for i in range(len(play_num)):
                    if play_num[i][0] == gen:
                        play_num[i][1]+=play

    play_num.sort(key = lambda x:x[1],reverse=True)

    # print(play_num)

    for genre,plays in play_num:
        cnt=0
        for gen,i,play in all:
            if genre==gen:
                cnt+=1
                if cnt>2: break
                else: answer.append(i)

    return answer

def solution3(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres,plays))