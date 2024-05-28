import sqlite3

sqliteConnection = sqlite3.connect('employee.db')
print("Database connected")

cursor = sqliteConnection.cursor()
print("Database initialized")

create_table_query = """
CREATE TABLE IF NOT EXISTS employee(id integer primary key AUTOINCREMENT, name text, age int, department text);
"""
cursor.execute(create_table_query)

def add_employee():
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    department = input("Enter employee department: ")
    
    sqliteConnection = sqlite3.connect('employee.db')
    cursor = sqliteConnection.cursor()
    cursor.execute('INSERT INTO employee (name, age, department) VALUES (?, ?, ?)', (name, age, department))
    
    sqliteConnection.commit()
    sqliteConnection.close()
 
    print("Employee add successfully.")

def list_employees():
    sqliteConnection = sqlite3.connect('employee.db')
    cursor = sqliteConnection.cursor()
    cursor.execute('SELECT * FROM employee')
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Department: {row[3]}")

    else:
        print("No employess found.")
    
    sqliteConnection.commit()
    sqliteConnection.close()
    
def delete_employee():
    emp_id = int(input("Enter employee ID to delete: "))

    sqliteConnection = sqlite3.connect('employee.db')
    cursor = sqliteConnection.cursor()
    cursor.execute('DELETE FROM employee WHERE id = ?', (emp_id),)

    if cursor.rowcount > 0:
        print("employee deleted successfully")
    else:
        print("employee not found.")

    sqliteConnection.commit()
    sqliteConnection.close()

def menu():
    while True:
        print("\nMenu:")
        print("1. Add Employee")
        print("2. List Employees")
        print("3. Delete Employee")
        print("4. Exit")

        choice = input("enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            list_employees()
        elif choice == '3':
            delete_employee()
        elif choice == '4':
            print("exiting the program")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ ==  "__main__":
    menu()