def pos(n):
    if n == 0: 
        print('already Zero')
        exit()
    while n > 0:
        print(n-1, end=' ')
        n -= 1
        
def neg(n):
    if n == 0: 
        print('already Zero')
        exit()
    while n <= 0:
        print(n, end=' ')
        n += 1