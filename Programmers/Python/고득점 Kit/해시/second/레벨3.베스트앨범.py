from collections import Counter


def solution(genres, plays):
    answer = []

    cnt = Counter(genres)

    genre_total_play = []

    for k in cnt.keys():
        total = 0
        for genre, play in zip(genres, plays):
            if genre == k:
                total += play
        genre_total_play.append([k, total])

    genre_total_play.sort(key=lambda x: x[1], reverse=True)

    for g, t in genre_total_play:
        genre = g
        inx_play = []
        for i, gp in enumerate(zip(genres, plays)):
            g = gp[0]
            p = gp[1]
            if g == genre:
                inx_play.append([i, p])
        inx_play.sort(key=lambda x: x[1], reverse=True)
        cnt = 0
        for ip in inx_play:
            if cnt >= 2:
                break
            i = ip[0]
            answer.append(i)
            cnt += 1

    return answer

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