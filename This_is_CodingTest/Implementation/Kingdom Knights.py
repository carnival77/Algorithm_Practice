def myEnum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)


if __name__ == '__main__':

    position = input()
    row=int(position[1])
    col=int(ord(position[0])) - int(ord('a')) +1

    cols = myEnum('a','b','c','d','e','f','g','h')

    count = 0

    steps = [[-2,-1],[-2,1],[2,-1],[2,1],[1,2],[1,-2],[-1,2],[-1,-2]]

    for step in steps:
        if col + step[1] >= 1 and row + step[0] >= 1 and col+step[1] <= 8 and row+step[0] <=8:
            count  += 1

    print(count)
