from helper import *
from resClasses import *

ROLES = [
    'manager',
    'waiter',
    'cleaner',
    'chef'
]

while True:
    print('[1] Employee List | [2] Apply | [3] Resign | [4] Exit')
    choice = get_and_check('int', '> ', [1,2,3,4])

    if choice == 1:
        # Waiter, Clearner, Chef, Manager

        print("Managers - ")
        for manager in Manager.managers:
            print(manager)

        print("Chefs - ")
        for chef in Chef.chefs:
            print(chef)

        print("Waiters - ")
        for waiter in Waiter.waiters:
            print(waiter)

        print("Cleaners - ")
        for cleaner in Cleaner.cleaners:
            print(cleaner)

    elif choice == 2:
        role = get_and_check('str', 'Enter a job role : ', ROLES)

        if role == 'manager':
            name, age, gender = get_person()

            isMarried = input("Are you married [Yes/No] : ")
            if isMarried.lower() == 'yes': isMarried = True
            else: isMarried = False

            newRole = Manager(name, age, gender, isMarried)

        elif role == 'chef':
            name, age, gender = get_person()

            newRole = Chef(name, age, gender)

        elif role == 'waiter':
            name, age, gender = get_person()

            newRole = Waiter(name, age, gender)

        elif role == 'cleaner':
            name, age, gender = get_person()

            newRole = Cleaner(name, age, gender)

    elif choice == 3:
        print("You can't resign.")

    else: 
        print("Exiting program!")
        break 