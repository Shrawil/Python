def main():
    while(True):
        print("[1] Add task\n[2] Show task\n[3] Delete all tasks\n[4] Delete by number\n[0] Exit")
        choice = input("Enter your choice : ")
        if choice == '1':
            with open("todo.txt", "a") as file:
                task = input("Enter a task : ")
                file.write(f"{task}\n")

        elif choice == '2':
            print("Todo list")
            print("=========")
            with open("todo.txt", "r") as file:
                i = 1
                for line in file:
                    print(f"{i}: {line.strip()}")
                    i += 1

        elif choice == '3':
            with open("todo.txt", "w") as file:
                file.write("")
            print("Delete all task in todo list!")

        elif choice == '4':
            content = ""
            num = int(input("Enter task number : "))
            with open("todo.txt", "r") as file:
                for i, line in enumerate(file, start=1):
                    if i != num:
                        content += line
            with open("todo.txt", "w") as file:
                file.write(content)

        elif choice == '0':
            break

if __name__ == '__main__':
    main()