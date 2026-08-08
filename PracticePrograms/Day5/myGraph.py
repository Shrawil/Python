def inPoints(r, c, points):
    for item in points.items():
        if item[0] == c and item[1] >= r:
            return True
    return False

def showGraph(row, col, points):
    print(points.items())
    for r in range(row,0,-1):
        print(r, end=' ')
        for c in range(1, col+1):
            #print(f'r:{r} | c:{c} | inPoints:{inPoints(r,c,points)}')
            if inPoints(r, c, points):
                print('[', end=']')
            else:
                print(' ', end=' ')
        print()
    for i in range(col+1):
        print(i, end=' ')

if __name__ == '__main__':
    points = {
        1:3,
        2:6,
        3:1,
        4:4,
        5:3,
        6:2,
        7:6,
    }
    showGraph(6, 7, points)