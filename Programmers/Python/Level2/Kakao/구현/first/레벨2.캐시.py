def solution(cacheSize, cities):
    answer = 0
    cache=[]

    if cacheSize==0:
        answer=len(cities)*5
        return answer

    for city in cities:
        city=city.lower()
        # 참조하는 값이 캐시안에 없으면
        if city not in cache:
            # 캐시에 여유 공간이 있다면 넣어주고
            if len(cache)<cacheSize:
                cache.append(city)
            # 가장 오래 전에 참조한 값을 빼고 현재 값을 캐시에 넣어준다.
            else:
                cache.pop(0)
                cache.append(city)
            answer+=5
        # 참조하는 값이 캐시안에 있으면 해당 값을 캐시의 가장 최근 위치에 넣어준다.
        else:
            cache.pop(cache.index(city))
            cache.append(city)
            answer+=1

    return answer

# cacheSize=3
# cacheSize=2
# cacheSize=5
cacheSize=0
# cities=["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
# cities=	["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
# cities=	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
# cities=	["Jeju", "Pangyo", "NewYork", "newyork"]
cities=	["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize,cities))