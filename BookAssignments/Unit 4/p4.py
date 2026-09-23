import random

n = 100

CHOICES = ['HEADS', 'TAILS']


headCount = 0
tailCount = 0
for i in range(n):
    flip = random.choice(CHOICES)
    if flip == 'HEADS':
        headCount += 1
    else:
        tailCount += 1
print(headCount)
print(tailCount)
print("Probabily is ", headCount/tailCount)