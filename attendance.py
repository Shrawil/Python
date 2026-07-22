def get_and_check(msg: str, *args):
    while True:
        try:
            choice = int(input(msg))
            if choice in args:
                return choice 
            else:
                print(f"Please choose between {args[0]} - {args[len(args)-1]}.")
        except ValueError:
            print("Please enter a valid value.")


def take_attendance():
    absent = 0
    present = 0
    return present, absent

def main():
    while True:
        choice = get_and_check('[1] Take Attendance | [2] Exit > ', 1, 2)
        if choice == 1:
            present, absent = take_attendance()
        elif choice == 2:
            break
    

if __name__ == '__main__':
    main()