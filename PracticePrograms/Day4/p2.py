class Square:
    def area(self, l):
        print(f"Area of Square with length : {l} = {l ** 2}.")
    
    def perimeter(self, l):
        print(f"Perimeter of Square with length : {l} = {4 * l}.")

class Rectangle:
    def area(self, l, b):
        print(f"Area of Rectangle with length : {l} and breadth : {b} = {l * b}.")

    def perimeter(self, l, b):
        print(f"Perimeter of Rectangle with length : {l} and breadth : {b} = {2 * (l + b)}.")

shape1 = Square()
shape1.area(10)
shape1.perimeter(10)

shape2 = Rectangle()
shape2.area(10, 20)
shape2.perimeter(10, 20)