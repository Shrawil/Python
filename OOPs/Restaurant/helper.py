def get_and_check(choiceType: str, msg: str, choices: list) -> str:  

    if choiceType not in ['int', 'str', 'bool', 'float']:
        return 'You must provide a valid datatype.'    
    
    while True:
        try:
            choice = input(msg)

            choice = choice.lower()

            if choiceType == 'int':
                choice = int(choice)

            elif choiceType == 'bool':
                if choice == 'True': choice = True
                else: choice = False 

            elif choiceType == 'float':
                choice = float(choice)

            if choice in choices:
                break
            else:
                print(f'Choose between {choices}.')

        except ValueError:
            print('Please enter a valid value.')

    return choice

def upCap(*args):
    result = []

    for arg in args:
        result.append(arg.lower().capitalize())

    return tuple(result)

GENDERS = ['male', 'female']

def get_person():
    name = input("Enter your name : ")

    while True:
        try:
            age = int(input("Enter your age : "))
            break
        except ValueError:
            print("Enter a valid value for age : ")

    while True:
        gender = input("Enter your gender : ")
        if gender.lower() not in GENDERS:
            print(f"Please choose between {GENDERS}.")
        else:
            break

    return name, age, gender

if __name__ == '__main__':
    print("This file is supposed to be used as imported module.")
    exit()