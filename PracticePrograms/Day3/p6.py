# Spiral Pattern

a = [
    [1,2,3,4],
    [12,13,14,5],
    [11,16,15,6],
    [10,9,8,7]
]

# How about we move in directions?
# dir = [0 for right, 1 for down, 2 for left, 3 for up]
# while travesing store the visited index in a list
# then if the next index to be visited is in the list then just change the dir
# for the problem the outer loop will run the same as normal 2d matrix loop
# 123 696 745
# inner loop will manage the directions

x = 0
y = 0
devmode = False
directions = {
    0:"Right",
    1:"Down",
    2:"Left",
    3:"Up"
}

visited = []
lenA = len(a)
dir = 0

def debug(x, y, visited):
    if not devmode:
        return
    global a
    try: 
        print(f"{a[x][y]} : {(x, y) in visited}")
    except:
        pass

def isVisited(x, y):
    global visited
    if (x,y) in visited:
        return True
    return False

for _ in range(lenA * lenA):
    visited.append((x,y))
    print(f"({x},{y}), dir = {directions[dir]}, value = {a[x][y]}")
    # Go right
    if dir == 0:
        print(a[x][y], end=" ")
        debug(x,y+1,visited)
        if y + 1 == lenA or isVisited(x, (y+1)):
            dir = 1
            x += 1
        else: y += 1

    # Go down
    elif dir == 1:
        print(a[x][y], end=" ")
        debug(x+1, y, visited)
        if x + 1 == lenA or isVisited((x+1), y):
            dir = 2
            y -= 1
        else: x += 1

    # Go left
    elif dir == 2:
        print(a[x][y], end=" ")
        debug(x, y-1, visited)
        if y - 1 == -1 or isVisited(x, (y-1)):
            dir = 3
            x -= 1
        else: y -= 1

    # Go up
    elif dir == 3:
        print(a[x][y], end=" ")
        debug(x-1, y, visited)
        if x - 1 == -1 or isVisited((x-1), y):
            dir = 0
            x += 1
        else: x -= 1

print(a[x][y])