import sys

try:
    import os
    import sqlite3
    from termcolor import colored
    from pyfiglet import figlet_format
    from platform import system
    from prettytable import PrettyTable
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!!]Press Any Key To Exit..", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")

db = sqlite3.connect("task.db")
cr = db.cursor()
cr.execute("CREATE TABLE IF NOT EXISTS tasks(task_id INTEGER PRIMARY KEY, task_name VARCHAR(250) NOT NULL)")
db.commit()


def addTask(task_id: int, task_name: str) -> None:
    try:
        cr.execute("INSERT INTO tasks VALUES (?, ?)", (task_id, task_name))
        db.commit()
        print(colored("[++]~ DONE ADD ~[++]", color="blue"))
    except sqlite3.IntegrityError:
        print(colored("[!!]ID Already Exists", color="red"))


def deleteTask(task_id: int) -> None:
    cr.execute(f"DELETE FROM tasks WHERE task_id={task_id}")
    db.commit()
    print(colored("[++]~ DONE DELETE ~[++]", color="blue"))


def showTasks() -> None:
    cr.execute("SELECT * FROM tasks ORDER BY task_id")
    ALL_DATA = cr.fetchall()
    if len(ALL_DATA) == 0:
        print(colored("[!!]NO DATA", color="red"))
    TABLE = PrettyTable(["ID", "TASKS"])
    for row in ALL_DATA:
        TABLE.add_row(row)
    print(colored(TABLE, color="blue"))


def updateTask(task_id: int, value: str) -> None:
    cr.execute(f"UPDATE tasks SET task_name='{value}' WHERE task_id={task_id}")
    db.commit()
    print(colored("[++]~ DONE UPDATE ~[++]", color="blue"))


def Exit() -> None:
    db.commit()
    db.close()
    sys.exit()


def main() -> None:
    try:
        print(colored("""
What do you want to do?
[1]Show All Tasks
[2]Add Task
[3]Delete Task
[4]Update Task
[0]Quit App
        """, color="blue"))
        while True:
            print("")
            option = int(input(colored("[++]Choose Option: ", color="blue")))
            print("\n")
            if option == 1:
                showTasks()
            elif option == 2:
                ID = int(input(colored("[+]ID: ", color="blue")))
                TASK = str(input(colored("[+]Task: ", color="blue")))
                print("\n")
                addTask(task_id=ID, task_name=TASK)
            elif option == 3:
                ID = int(input(colored("[+]ID: ", color="blue")))
                print("\n")
                deleteTask(task_id=ID)
            elif option == 4:
                ID = int(input(colored("[+]ID: ", color="blue")))
                NEW_TASK = str(input(colored("[+]New Task: ", color="blue")))
                print("\n")
                updateTask(task_id=ID, value=NEW_TASK)
            elif option == 0:
                Exit()
            else:
                print(colored(f"[!!]Invalid Option", color="red"))
    except Exception as er:
        print(colored(er, color="red"))


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("TASK MANAGER APP"), color="blue"))
    print("\n")
    main()

