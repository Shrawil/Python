def get_and_check(msg: str):
    while True:
        try:
            choice = int(input(msg))
            return choice 
        except ValueError:
            print("Please enter a valid value.")


def take_attendance():
    # Will hold all roll numbers
    present = list()
    absent = list()
    
    total_students = get_and_check('Enter number of students : ')
    print("Type 1 if present. [Note: Any other number than 1 will mark the roll number as absent.]")

    for i in range(total_students):
        is_present = get_and_check(f'Roll number {i+1} : ')
        if is_present == 1: present.append(i+1)
        else: absent.append(i+1)

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