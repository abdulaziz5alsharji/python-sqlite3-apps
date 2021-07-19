import sys

try:
    import os
    import sqlite3
    from platform import system
    from termcolor import colored
    from pyfiglet import figlet_format
    from prettytable import PrettyTable
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!!]Press Any Key To Exit...", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")

db = sqlite3.connect(r"C:\Users\Dell\Desktop\password_safe.db")

cr = db.cursor()
cr.execute("CREATE TABLE IF NOT EXISTS safe_password(id INTEGER PRIMARY KEY AUTOINCREMENT, website_name TEXT, "
           "username TEXT NOT NULL, "
           "password TEXT NOT NULL)")

db.commit()


def addData(website_name: str, username: str, password: str) -> None:
    cr.execute("INSERT INTO safe_password (website_name, username, password) VALUES (?, ?, ?)", (website_name, username,
                                                                                                 password))
    db.commit()


def showData() -> None:
    cr.execute("SELECT * FROM safe_password ORDER BY id")
    data = cr.fetchall()
    if len(data) == 0:
        print(colored("[!!]NO DATA", color="red"))
    else:
        table = PrettyTable(["ID", "Website", "Username", "Password"])
        print(colored(f"You Have {len(data)} Skill.", color="blue"))
        print("\n")
        for row in data:
            table.add_row(row)
        print(colored(table, color="blue"))


def search(website=None, username=None) -> None:
    if website is None and username is None:
        cr.execute("SELECT * FROM safe_password ORDER BY id")
        data = cr.fetchall()
        if len(data) == 0:
            print(colored("[!!]NO DATA", color="red"))
        else:
            table = PrettyTable(["ID", "Website", "Username", "Password"])
            print(colored(f"You Have {len(data)} Skill.", color="blue"))
            print("\n")
            for row in data:
                table.add_row(row)
            print(colored(table, color="blue"))
    elif website is None:
        cr.execute(f"SELECT * FROM safe_password WHERE username='{username}' ORDER BY id")
        data = cr.fetchall()
        if len(data) == 0:
            print(colored("[!!]NO DATA", color="red"))
        else:
            table = PrettyTable(["ID", "Website", "Username", "Password"])
            print(colored(f"You Have {len(data)} Skill.", color="blue"))
            print("\n")
            for row in data:
                table.add_row(row)
            print(colored(table, color="blue"))
    elif username is None:
        cr.execute(f"SELECT * FROM safe_password WHERE website_name='{website}' ORDER BY id")
        data = cr.fetchall()
        if len(data) == 0:
            print(colored("[!!]NO DATA", color="red"))
        else:
            table = PrettyTable(["ID", "Website", "Username", "Password"])
            print(colored(f"You Have {len(data)} Skill.", color="blue"))
            print("\n")
            for row in data:
                table.add_row(row)
            print(colored(table, color="blue"))
    else:
        cr.execute(f"SELECT * FROM safe_password WHERE website_name='{website}' AND username='{username}' ORDER BY id")
        data = cr.fetchall()
        if len(data) == 0:
            print(colored("[!!]NO DATA", color="red"))
        else:
            table = PrettyTable(["ID", "Website", "Username", "Password"])
            print(colored(f"You Have {len(data)} Skill.", color="blue"))
            print("\n")
            for row in data:
                table.add_row(row)
            print(colored(table, color="blue"))


def deleteData(id_: int) -> None:
    cr.execute(f"DELETE FROM safe_password WHERE id={id_}")
    db.commit()


def updateData(new_password: str, id_: int) -> None:
    cr.execute(f"UPDATE safe_password SET password='{new_password}' WHERE id={id_}")
    db.commit()


def Exit() -> None:
    db.commit()
    db.close()
    sys.exit()


def main() -> None:
    try:
        print(colored("""
What do you want to do?
[1]Show All Data
[2]Add Date
[3]Delete Data
[4]Update Data
[5]Search About Data
[0]Quit App
        """, color="blue"))
        while True:
            print("")
            option = int(input(colored("[++]Choose Option: ", color="blue")))
            print("\n")
            if option == 1:
                showData()
            elif option == 2:
                websiteName = str(input(colored("[+]WebSite Name: ", color="blue")))
                Username = str(input(colored("[+]Username: ", color="blue")))
                Password = str(input(colored("[+]Password: ", color="blue")))
                addData(website_name=websiteName, username=Username, password=Password)
                print("\n")
                print(colored(f"[++]===================== Add IS DONE =====================[++]", color="blue"))
            elif option == 3:
                ID = int(input(colored("[+]ID: ", color="blue")))
                deleteData(id_=ID)
                print("\n")
                print(colored(f"[++]===================== DELETE IS DONE =====================[++]", color="blue"))
            elif option == 4:
                ID = int(input(colored("[+]ID: ", color="blue")))
                newPassword = str(input(colored("[+]New Password: ", color="blue")))
                updateData(newPassword, id_=ID)
            elif option == 5:
                websiteName = str(input(colored("[+]WebSite Name: ", color="blue")))
                Username = str(input(colored("[+]Username: ", color="blue")))
                if websiteName == "" and Username == "":
                    search()
                elif websiteName == "":
                    search(username=Username)
                elif Username == "":
                    search(website=websiteName)
                else:
                    search(website=websiteName, username=Username)
            elif option == 0:
                Exit()
            else:
                print(colored(f"[!!]Invalid Option", color="red"))
    except Exception as er:
        print(colored(er, color="red"))


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("Safe Password App"), color="blue"))
    print("\n")
    main()
