# 배낭 문제
# d[i][j] : i번째 물건까지 고려했고 배낭의 무게(=허용 무게)가 j일 때 최대 가치.
# 점화식 및 논리 :
# [점화식]
# (전제) weight=w[i], value=v[i]
# 1) if j<weight : d[i][j] = d[i-1][j]
# 2) if j>=weight : max( d[i-1][ j-weight ]+value ), d[i-1][j] )
# [논리]
# i번째 물건까지 고려했고 배낭의 무게(=허용 무게)가 j일 때 최대 가치를 만드려고 한다.
# i번째 물건을 배낭에 담기를 고려할 때,
# 1) 현재 배낭의 허용 무게보다 물건의 무게가 더 크면 넣지 않는다.
#     이때 최대 가치는 현재 가방의 허용 무게 j로
#     그 전(i-1번째 물건을 고려할 때)까지 가져올 수 있었던 최대 가치다.
# 2) 그렇지 않다면, 다음 중 더 나은 선택지를 고른다.
# 2-1) 현재 물건을 배낭에 넣는다.
#     그 전(i-1번째 물건을 고려할 때)까지 현재 배낭의 허용 무게에서 물건의 무게만큼 뺀 허용 무게로
#     가져올 수 있었던 최대 가치에 물건의 가치를 더한다.
# 2-2) 현재 물건을 넣지 않고 이전 배낭 그대로 가지고 간다.
#     이때 최대 가치는 현재 가방의 허용 무게 j로
#     그 전(i-1번째 물건을 고려할 때)까지 가져올 수 있었던 최대 가치다.
# 참고 :
# 1. https://velog.io/@imacoolgirlyo/12865%EB%B2%88-%ED%8F%89%EB%B2%94%ED%95%9C-%EB%B0%B0%EB%82%AD-86k4cgn35m
# 2. https://hongcoding.tistory.com/50

n,k=map(int,input().split())
w,v=[0],[0]
for _ in range(n):
    a,b=map(int,input().split())
    w.append(a)
    v.append(b)

d=[[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        weight=w[i]
        value=v[i]

        if  j<weight:
            d[i][j]=d[i-1][j]
        else:
            d[i][j]=max(d[i-1][j-weight]+value,d[i-1][j])

print(d[n][k])