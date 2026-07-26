# Rotate the list left by one position.

# import time

# Pseudocode 
# 1. Store first element in temp.
# 2. ls[i] = ls[i+1]
# 3. Last element = temp

def rotate(ls):
    temp = ls[0]
    for i in range(len(ls)):
        if i == len(ls)-1:
            ls[i] = temp
        else:
            ls[i] = ls[i+1]
    return ls 

def main():
    ls = [1,2,3,4,5,6,7]
    print(ls)
    print(rotate(ls))
    '''
    for i in range(1000):
        print(rotate(ls), end="\r", flush=True)
        time.sleep(0.1)
    '''

if __name__ == '__main__':
    main()