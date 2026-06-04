import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

def doSql(choice):
    #Creating table
    if choice == 0:
        tableName = input("Enter table name : ")
        try:
            cursor.execute(f"CREATE TABLE {tableName}(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(20), age INT, roll INT)")
            conn.commit()
            print("Table created successfully!")
        except:
            print("Table already exists!")
    #Inserting into table
    elif choice == 1:
        tableName = input("Enter table name : ")
        try:
            name = input("Enter your name : ")
            age = int(input("Enter your age : "))
            roll = int(input("Enter you roll number : "))
            cursor.execute(f"INSERT INTO {tableName}(name, age, roll) VALUES(?, ?, ?)", (name, age, roll,))
            conn.commit()
            print("Inserted 1 Row!")
        except: print("An error occured while trying to run this query!")
    #Deleting from table
    elif choice == 2:
        tableName = input("Enter table name : ")
        try:
            rowId = int(input("Enter row id to delete : "))
            cursor.execute(f"DELETE FROM {tableName} WHERE id = ?", (rowId,))
            conn.commit()
        except: print("An error occured while trying to run this query!")
    #Delete all from table
    elif choice == 3:
        tableName = input("Enter table name : ")
        try:
            cursor.execute(f"DELETE * FROM {tableName}")
            conn.commit()
            print("All rows deleted!")
        except: print("Table does not exist!")
    #Selecting from table
    elif choice == 4:
        tableName = input("Enter table name : ")
        try:
            rowId = int(input("Enter row id to search : "))
            cursor.execute(f"SELECT * FROM {tableName} WHERE id = ?", (rowId,))
            print(cursor.fetchone())
        except: print("Table does not exist!")
    elif choice == 5:
        tableName = input("Enter table name : ")
        try:
            cursor.execute(f"SELECT * FROM {tableName}")
            for row in cursor.fetchall():
                print(row)
        except: print("Table does not exist!")
    elif choice == 6:
        tableName = input("Enter table name : ")
        try: cursor.execute(f"DROP TABLE {tableName}")
        except: print("Table does not exist!")
        

while(True):
    print("[0] Create Table\n[1] Insert\n[2] Delete by ID\n[3] Delete All\n[4] Search by ID\n[5] Select all\n[6] Drop table\n[7] Exit")
    try: 
        choice = int(input("Enter your choice : "))
        if choice == 7: break
        elif choice < 0 or choice > 7: print("Invalid input recieved : Choose between 0 to 7!")
        else: doSql(choice)
    except:
        print("Something went wrong!")
print("Thank you for using this program!")