items = [
    'Apple',
    'Banana',
    'Mango',
    'Bottle',
    'Pen',
    'Notebook',
    'Keyboard',
] 

def get_choice(msg, choices):
    while True:
        try:
            choice = int(input(msg))
            if choice in choices:
                break
            else:
                print(f"Please choose between {choices[0]}-{choices[len(choices)-1]}.")
        except:
            print("Please enter a valid number!")
    return choice

def show_items():
    print("Items available : ")
    for i in range(len(items)):
        print(f"Item {i+1} : {items[i]}")

def add_to_cart(cart: list):
    itemNumber = get_choice("Enter item number to add to cart [-1 to show item list] : ", (-1,1,2,3,4,5,6,7))
    if itemNumber == -1:
        show_items()
    elif items[itemNumber-1] is not None:
        print(f"{items[itemNumber-1]} added to cart!")
        cart.append(items[itemNumber-1])

def main():
    cart = list()
    while True:
        option = get_choice("[1] Add to cart | [2] Show cart items | [3] Show item list | [4] Exit : ", (1,2,3,4))
        if option == 1:
            add_to_cart(cart)
        elif option == 2:
            print("Your cart items : ")
            for i in range(len(cart)):
                print(f"Item {i+1} : {cart[i]}")
        elif option == 3:
            show_items()
        else:
            break

        

if __name__ == '__main__':
    main()