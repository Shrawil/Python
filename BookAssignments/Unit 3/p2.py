m = '11'

# 11(base b) = b^1 + b^0
#            = b + 1

print(int(m, 2)) # 2 + 1
print(int(m, 8)) # 8 + 1
print(int(m, 10)) # 10 + 1
print(int(m, 16)) # 16 + 1

m = '111'

# 111(base b) = b^2 + b^1 + b^0
#             = b^2 + b + 1

print(int(m, 2)) # 4 + 2 + 1 = 7
print(int(m, 8)) # 64 + 8 + 1 = 73
print(int(m, 10)) # 100 + 10 + 1 = 111
print(int(m, 16)) # 256 + 16 + 1 = 273