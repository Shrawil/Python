import math

OPERATIONS = {
    1: "Area",
    2: "Perimeter",
    3: "Circumference"
}

SHAPES = {
    1: "Circle",
    2: "Square",
    3: "Rectangle",
    4: "Triangle"
}

def get_and_check_valid(word):
    while True:
        try:
            res = float(input(f"Enter value for {word} : "))
            break 
        except ValueError:
            print(f"Please enter a valid value for {word}!")
    return res

def get_values(shape, operation):
    print(shape, operation)
    if shape == 'Circle':
        return get_and_check_valid('radius')
    elif shape == 'Square':
        return get_and_check_valid('length')
    elif shape == 'Rectangle':
        return get_and_check_valid('length'), get_and_check_valid('breadth')
    elif shape == 'Triangle':
        if operation == 1:
            return get_and_check_valid('base'), get_and_check_valid('height')
        elif operation == 2:
            return get_and_check_valid('side a'), get_and_check_valid('side b'), get_and_check_valid('side c')

def get_operation():
    print("[1] Area | [2] Perimeter | [3] Circumference")
    while True:
        operation = get_and_check_valid('operation')
        if operation in OPERATIONS:
            break
        else:
            print("Please choose and opertion between 1-3!")
    return operation

def get_shape():
    print("[1] Circle | [2] Square | [3] Rectangle | [4] Triangle")
    while True:
        shape = get_and_check_valid('shape')
        if shape in SHAPES:
            break
        else:
            print("Please choose a shape between 1-4.")
    return shape

def formula(shape, operation):
    # Circle
    if shape == 1: 
        # Since we are working with circle only thing we will need is radius.
        radius = get_values(SHAPES[shape], OPERATIONS[operation])
        if operation == 1:
            res = ((math.pi * radius) ** 2)
        else:
            res = 2 * math.pi * radius
    # Square
    elif shape == 2:
        side = get_values(SHAPES[shape], OPERATIONS[operation])
        if operation == 1:
            res = side ** 2
        else:
            res = 4 * side
    # Rectangle
    elif shape == 3:
        length, breadth = get_values(SHAPES[shape], OPERATIONS[operation])
        if operation == 1:
            res = length * breadth
        else:
            res = 2 * (length + breadth)
    # Triangle
    else:
        if operation == 1:
            base, height = get_values(SHAPES[shape], OPERATIONS[operation])
            res = (base * height)/2
        else:
            a,b,c = get_values(SHAPES[shape], OPERATIONS[operation])
            res = a + b + c
    return res

def main():
    shape = get_shape()
    operation = get_operation()

    if shape == 1 and operation == 2: print("Cannot find perimeter of a circle!")
    if shape != 1 and operation == 3: print(f"Cannot find circumference of {SHAPES[shape]}!")

    print(f"{operation} of {shape} is {formula(shape, operation):.2f}")

    
if __name__ == '__main__':
    main()