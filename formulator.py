import math

def formula(shape, operation, *args):
    print(shape, operation)
    for arguments in args:
        print(arguments)

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
                if shape > 0 and shape < 3:
                    try:
                        radius = int(input("Enter radius : "))
                    except ValueError:
                        print("Please enter a valid radius value for cirle.")
                    formula(shape, opr, radius)
                    break
            except ValueError:
                print("Please enter a valid integer.")

    # Triangle
    elif shape == 4:
        print("[1] Area | [2] Perimeter")
        while True:
            try: 
                opr = int(input("Enter a number > "))
                if shape > 0 and shape < 3:
                    try: 
                        base = int(input("Enter value for base : "))
                        height = int(input("Enter value for height : "))
                    except ValueError:
                        print("Please enter valid integers for base and height of the triangle.")
            except ValueError:
                print("Please enter a valid integer.")

    # Square and Rectangle
    else:
        print("[1] Area | [2] Perimeter")
        while True:
            try: 
                opr = int(input("Enter a number > "))
                if shape > 0 and shape < 3:
                    try: 
                        length = int(input("Enter value for length : "))
                        breadth = int(input("Enter value for breadth : "))
                    except ValueError:
                        print(f"Please enter valid integers for length and breadth of the {shape}.")
            except ValueError:
                print("Please enter a valid integer.")

if __name__ == '__main__':
    main()