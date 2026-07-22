def get_and_check(msg: str):
    while True:
        try:
            choice = int(input(msg))
            return choice 
        except ValueError:
            print("Please enter a valid value.")


def take_attendance(present: list, absent: list):


    total_students = get_and_check('Enter number of students : ')
    print("Type 1 if present. [Note: Any other number than 1 will mark the roll number as absent.]")

    for i in range(total_students):
        is_present = get_and_check(f'Roll number {i+1} : ')
        if is_present == 1: present.append(i+1)
        else: absent.append(i+1)

    return present, absent

def main():
    # Will hold all roll numbers.
    present = list()
    absent = list()
    
    while True:
        choice = get_and_check('[1] Take Attendance | [2] Show Presentees | [3] Show Absentees | [4] Exit > ')
        
        # Call take_attendance function.
        if choice == 1:
            present, absent = take_attendance(present, absent)
            print(f"Total number of presentees : {len(present)}.\nTotal number of absentees : {len(absent)}.")

        # Print all present roll numbers.
        elif choice == 2:
            if present is None or absent is None:
                print("Take attendance first.")
            else:
                print("Present students roll numbers : ", end="")
                for roll in present:
                    print(roll, end=" ")
                print()

        # Print all absent roll numbers.
        elif choice == 3:
            if present is None or absent is None:
                print("Take attendance first.")
            else:
                print("Absent students roll numbers : ", end="")
                for roll in absent:
                    print(roll, end=" ")
                print()

        # Exit program.
        elif choice == 4:
            print("Thanks for using this program!")
            break

        # Invalid input recieved.
        else:
            print("Please choose between 1, 2, 3, 4.")

if __name__ == '__main__':
    main()