# Tower of Hanoi

n = 3

def tower(n, a, b, c):
    if n == 1:
        print(f"{a} -> {c}")
        return
    tower(n-1, a, c, b)
    print(f"{a} -> {c}")
    tower(n-1, b, a, c)

tower(n, "A", "B", "C")