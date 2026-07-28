from myLib.easyInput import get_and_check

options = {
    1:'Add',
    2:'Remove',
    3:'List',
    4:'Update',
    5:'Exit'
}

def add_contact(contacts: dict):
    name = input("Enter contact name to add : ")
    if name in contacts:
        print("Contact already exists.")
    else:
        c_no = get_and_check("Enter contact number : ", int)
        contacts[name] = c_no
    return contacts

def remove_contact(contacts: dict):
    name = input("Enter contact name to delete : ")
    if name not in contacts:
        print("Contact not found.")
    else:
        contacts.pop(name)
        print("Contact removed.")
    return contacts

def list_contact(contacts: dict):
    for name, contact in contacts.items():
        print(f"{name} - {contact}")

def update_contact(contacts: dict):
    name = input("Enter contact name to update : ")
    if name not in contacts:
        print("Contact not found.")
    else:
        c_no = get_and_check("Enter contact number : ", int)            
        contacts[name] = c_no
    return contacts

def main() -> None:

    # Dictionary where all the contact will be store, name as key and number as value.
    contacts = {
        'Emergency':911,
    }

    # Only exit when use input 5 as choice.
    while True:
        print("| Options \t|")
        for k, v in options.items():
            print(f"| [{k}] {v} \t|")
        choice = get_and_check(f"Choose : ", int)

        if choice == 1:
            contacts = add_contact(contacts)

        elif choice == 2:
            contacts = remove_contact(contacts)

        elif choice == 3:
            list_contact(contacts)

        elif choice == 4:
            contacts = update_contact(contacts)

        elif choice == 5:
            print("Program executed successfully!")
            break

        else:
            print(f"Choose between {options}.")


if __name__ == '__main__':
    main()