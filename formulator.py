import math

def formula(shape, operation, *args):
    # Shapes - [1] Circle | [2] Square | [3] Rectangle | [4] Triangle
    if shape == 1:
        # Operations - [1] Area | [2] Circumference
        if operation == 1:
            area = 2 * math.pi * args[0]
            print(f"Area of a circle with radius {args[0]} is {area:.2f}!")
        else:
            circumference = math.pi * pow(args[0], 2)
            print(f"Circumference of a circle with radius {args[0]} is {circumference:.2f}!")
    elif shape == 2:
        # Operations - [1] Area | [2] Perimeter
        if operation == 1:
            print(f"Area of square with side {args[0]} is {args[0] * args[0]}!")
        else:
            print(f"Permeter of square with side {args[0]} is {4 * args[0]}!")
    elif shape == 3:
        # Operations - [1] Area | [2] Perimeter
        if operation == 1:
            print(f"Area of rectangle with length {args[0]} and breadth {args[1]} is {args[0] * args[1]}!")
        else:
            print(f"Permeter of rectangle with length {args[0]} and breadth {args[1]} is {2 * (args[0] + args[1])}!")
    else:
        # Operations - [1] Area | [2] Permeter
        if operation == 1:
            print(f"Area of triangle with base {args[0]} and height {args[1]} is {(args[0] * args[1])/2}!")
        else:
            print(f"Permeter of triangle with sides {args[0]}, {args[1]}, {args[2]} is {args[0] + args[1] + args[2]}!")


def main():
    # Asking for the shape
    while True:
        print("[1] Circle | [2] Square | [3] Rectangle | [4] Triangle")
        try: 
            shape = int(input("Enter a number > "))
            if shape > 0 and shape < 5:
                break
        except ValueError:
            print("Please enter a valid integer.")

    # Showing options based on shape.

    # Circle
    if shape == 1:
        print("[1] Area | [2] Circumference")
        while True:
            try: 
                opr = int(input("Enter a number > "))
                if opr > 0 and opr < 3:
                    try:
                        radius = int(input("Enter radius : "))
                    except ValueError:
                        print("Please enter a valid radius value for cirle.")
                    formula(shape, opr, radius)
                    break
            except ValueError:
                print("Please enter a valid integer.")

    # Square
    elif shape == 2:
        print("[1] Area | [2] Permeter")
        while True:
            try: 
                opr = int(input("Enter a number > "))
                if opr > 2 or opr < 1:
                    print("Please choose between 1 and 2.")
                else:
                    try: 
                        side = int(input("Enter value for base : "))
                    except ValueError:
                        print("Please enter valid integers for side of square.")
                    formula(shape, opr, side)
            except ValueError:
                print("Please enter a valid integer.")

    # Rectangle
    elif shape == 3:
        print("[1] Area | [2] Permeter")
        while True:
            try: 
                opr = int(input("Enter a number > "))
                if opr > 2 or opr < 1:
                    print("Please choose between 1 and 2.")
                else:
                    try: 
                        length = int(input("Enter value for length : "))
                        breadth = int(input("Enter value for breadth : "))
                    except ValueError:
                        print("Please enter valid integers for sides of rectangle.")
                    formula(shape, opr, length, breadth)
            except ValueError:
                print("Please enter a valid integer.")

    # Triangle
    elif shape == 4:
        print("[1] Area | [2] Perimeter")
        while True:
            try: 
                opr = int(input("Enter a number > "))
                if opr == 1:
                    try: 
                        base = int(input("Enter value for base : "))
                        height = int(input("Enter value for height : "))
                    except ValueError:
                        print("Please enter valid integers for base and height of the triangle.")
                    formula(shape, opr, base, height)
                elif opr == 2:
                    try:
                        side1 = int(input("Enter value for side 1 : "))
                        side2 = int(input("Enter value for side 2 : "))
                        side3 = int(input("Enter value for side 3 : "))
                    except ValueError:
                        print("Please enter valid values for side of triangle.")
                    formula(shape, opr, side1, side2, side3)
                else:
                    print("Please choose between 1 and 2.")
            except ValueError:
                print("Please enter a valid integer.")

if __name__ == '__main__':
    main()