def get_and_check(msg: str):
    while True:
        try:
            choice = int(input(msg))
            return choice 
        except ValueError:
            print("Please enter a valid value.")


def take_attendance():
    absent = 0
    present = 0
    total_students = get_and_check('Enter number of students : ')
    return present, absent

def main():
    while True:
        choice = get_and_check('[1] Take Attendance | [2] Exit > ')
        if choice == 1:
            present, absent = take_attendance()
            print(f"Total number of presentees : {present}.\nTotal number of absentees : {absent}.")
        elif choice == 2:
            print("Thanks for using this program!")
            break
        else:
            print("Please choose between 1 and 2.")
            choice = get_and_check('[1] Take Attendance | [2] Exit > ')
    

if __name__ == '__main__':
    main()