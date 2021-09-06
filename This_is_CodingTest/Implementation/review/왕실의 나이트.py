pos = input()

row = int(pos[1])
col = int(ord(pos[0]) - int(ord('a'))) + 1

move_type = [(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(-1,2),(-1,-2)]

x=row
y=col

ans=0

for move in move_type:
    nx = x + move[0]
    ny = y + move[1]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        ans+=1

print(ans)