from myLib.easyInput import eval_list 

def get_grades(names: list):
    res = {}
    for name in names:
        grade = input(f"Enter grade for {name} [A,B,C,D,E,F] : ")
        res[name] = grade
    return res

def main():
    names = eval_list("Enter name of students : ")
    grade_dict = get_grades(names)

    for item in grade_dict:
        print(f'{item} : {grade_dict.get(item)}')

if __name__ == '__main__':
    main()