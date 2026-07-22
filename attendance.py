def get_and_check(msg: str):
    pass 

def take_attendance():
    absent = 0
    present = 0
    return present, absent

def main():
    while True:
        choice = get_and_check('[1] Take Attendance | [2] Exit > ')
        if choice == 1:
            present, absent = take_attendance()
        elif choice == 2:
            break
    

if __name__ == '__main__':
    main()