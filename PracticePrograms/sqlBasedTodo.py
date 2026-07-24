import sqlite3

conn = sqlite3.connect("todo.db")
cursor = conn.cursor()

try:
    cursor.execute("CREATE TABLE TODO (taskId INTEGER PRIMARY KEY AUTOINCREMENT, task VARCHAR(50))")
    conn.commit()
except:
    print("Working with existing TODO table!")
while True:
    print("[1] Create Task\n[2] Show Tasks\n[3] Delete All Tasks\n[4] Delete by Number\n[0] Exit")
    choice = int(input("Enter you choice : "))
    if choice == 1:
        task = input("Type task : ")
        cursor.execute("INSERT INTO TODO(task) VALUES(?)", (task,))
        conn.commit()
    elif choice == 2:
        cursor.execute("SELECT task FROM TODO")
        i = 1
        for tasks in cursor.fetchall():
            print(f"{i}: {tasks}")
            i += 1
    elif choice == 3:
        cursor.execute("DELETE FROM TODO")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='TODO'")
        conn.commit()
    elif choice == 4:
        num = int(input("Enter task number : "))
        cursor.execute("DELETE FROM TODO WHERE taskId=?", (num,))
        conn.commit()
    elif choice == 0:
        break