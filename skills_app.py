import sys

try:
    import os
    import sqlite3
    from pyfiglet import figlet_format
    from termcolor import colored
    from platform import system
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit ..", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")

db = sqlite3.connect(r"C:\Users\Dell\Desktop\python\app2.db")
cr = db.cursor()


# cr.execute("CREATE TABLE skills(user_id integer, skill text, progress integer)")


def showAllSkills() -> None:
    cr.execute("select * from skills")
    data = cr.fetchall()
    if len(data) == 0:
        print(colored("[!!]NO DATA", color="red"))
    else:
        print(colored(f"You Have {len(data)} Skill.", color="blue"))
        for uid, skill, progress in data:
            print(colored(f"[{uid}]{skill} => {progress}%", color="blue"))
    db.commit()


def addNewSkill(uid: int, skill: str, progress: int) -> None:
    cr.execute("select skill from skills")
    data = cr.fetchall()
    if (skill, ) in data:
        print(colored(f"[!]This Skill Is Already Exist", color="red"))
    else:
        cr.execute(f"INSERT INTO skills(user_id, skill, progress) VALUES ({uid}, '{skill}', {progress})")
        db.commit()


def deleteSkill(uid: int) -> None:
    cr.execute(f"DELETE FROM skills WHERE user_id = {uid}")
    db.commit()


def updateSkill(uid: int, new_progress: int) -> None:
    cr.execute(f"UPDATE skills SET progress={new_progress} WHERE user_id={uid}")
    db.commit()


def main() -> None:
    try:
        print(colored("""
What do you want to do?
[1]Show All Skills
[2]Add Skill
[3]Delete Skill
[4]Update Skill
[0]Quit App
        """, color="blue"))
        while True:
            print("")
            option = int(input(colored("[++]Choose Option: ", color="blue")))
            print("\n")
            if option == 1:
                showAllSkills()
            elif option == 2:
                ID = int(input(colored("[+]ID: ", color="blue")))
                skillName = str(input(colored("[+]Skill Name: ", color="blue"))).strip().capitalize()
                Progress = int(input(colored("[+]Progress: ", color="blue")))
                addNewSkill(uid=ID, skill=skillName, progress=Progress)
                print("\n")
                print(colored(f"[++]===================== Add IS DONE =====================[++]", color="blue"))
            elif option == 3:
                ID = int(input(colored("[+]ID: ", color="blue")))
                deleteSkill(uid=ID)
                print("\n")
                print(colored(f"[++]===================== DELETE IS DONE =====================[++]", color="blue"))
            elif option == 4:
                ID = int(input(colored("[+]ID: ", color="blue")))
                newProgress = int(input(colored("[+]New Progress: ", color="blue")))
                updateSkill(uid=ID, new_progress=newProgress)
            elif option == 0:
                db.close()
                sys.exit()
            else:
                print(colored(f"[!!]Invalid Option", color="red"))
    except Exception as er:
        print(colored(er, color="red"))


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("Skill App"), color="blue"))
    print("\n")
    main()
