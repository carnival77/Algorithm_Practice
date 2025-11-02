def solution(grid):
    n=len(grid)
    m=len(grid[0])

    ans=0

    for x in range((n+1)//2):
        for y in range((m+1)//2):
            points=set()
            points.add((x,y))
            points.add((x,m-1-y))
            points.add((n-1-x,y))
            points.add((n-1-x,m-1-y))
            B_cnt,W_cnt=0,0
            for i,j in points:
                if grid[i][j]=='B':B_cnt+=1
                if grid[i][j]=='W':W_cnt+=1
            ans+=min(B_cnt,W_cnt)
    return ans

# grid = [
#   "BBWBB",
#   "BWBBW",
#   "BBWWB"
# ] # 3
grid = [
  "BWB",
  "WBB",
  "WBW"
] # 4
print(solution(grid))