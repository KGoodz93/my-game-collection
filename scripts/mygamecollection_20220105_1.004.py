# Release Notes

"""
Release Notes 1.004

- Added a clear function to clear screen once the sub_menu function has been run.

"""

# Modules

import sqlite3
import os
import sys

# Variables

user = os.getlogin()
db = os.path.join(fr"C:\Users\{user}\Dropbox\Coding\Python\Apps\My Game Collection\db\games.db")
clear = lambda: os.system("cls")

# DB

connection = sqlite3.connect(db)
cursor = connection.cursor()

print("Successfully Connected to SQLite3!")

print("\n---| M Y   G A M E   C O L L E C T I O N |---")


def sub_menu():
    submenu = input("\nWould you like to return to the Main Menu? (Y or N): ")

    if (submenu == "Y") or (submenu == "y"):
        clear()
        main_menu()
    elif (submenu == "N") or (submenu == "n"):
        sys.exit()
    else:
        clear()
        print("This option is invalid. Please try again")
        sub_menu()

# Consoles

def GBA():
    viewall = cursor.execute("SELECT DISTINCT name FROM GBA order by release_date ASC;")
    for i in viewall:
        print("- " + i[0])

    print("\nHere is a breakdown of your GBA Game Library:\n")

    print("--- Collection ---\n")

    filter1 = cursor.execute("SELECT COUNT (name) FROM GBA")
    for i in filter1:
        print("Total Collected: " + str(i[0]) + " Games")

    filter2 = cursor.execute("SELECT COUNT (collection) FROM GBA WHERE collection=(?)", ("Sold",))
    for i in filter2:
        print("Total Sold: " + str(i[0]) + " Games")

    filter3 = cursor.execute("SELECT COUNT (collection) FROM GBA WHERE collection=(?)", ("Own",))
    for i in filter3:
        print("Total Own: " + str(i[0]) + " Games")

    print("\n--- Currently Own ---\n")

    filter4 = cursor.execute("SELECT COUNT (Format) FROM GBA WHERE Format=(?) AND collection=(?)", ("Physical", "Own",))
    for i in filter4:
        print("Physical: " + str(i[0]) + " Games")

    print("\n--- Status ---\n")

    filter8 = cursor.execute("SELECT COUNT (status) FROM GBA WHERE status=(?)", ("Completed",))
    for i in filter8:
        print("Completed: " + str(i[0]) + " Games")

    filter9 = cursor.execute("SELECT COUNT (status) FROM GBA WHERE status=(?)", ("Finished",))
    for i in filter9:
        print("Finished: " + str(i[0]) + " Games")

    filter10 = cursor.execute("SELECT COUNT (playing) FROM GBA WHERE playing=(?)", ("Y",))
    for i in filter10:
        print("Playing: " + str(i[0]) + " Games")

    filter11 = cursor.execute("SELECT name FROM GBA WHERE playing=(?)", ("Y",))
    print("\n--- Currently Playing ---\n")
    for i in filter11:
        print("- " + str(i[0]))

def PC():
    viewall = cursor.execute("SELECT DISTINCT name FROM PC order by release_date ASC;")
    for i in viewall:
        print("- " + i[0])

    print("\nHere is a breakdown of your PC Game Library:\n")

    print("--- Collection ---\n")

    filter1 = cursor.execute("SELECT COUNT (name) FROM PC")
    for i in filter1:
        print("Total Collected: " + str(i[0]) + " Games")

    filter2 = cursor.execute("SELECT COUNT (collection) FROM PC WHERE collection=(?)", ("Sold",))
    for i in filter2:
        print("Total Sold: " + str(i[0]) + " Games")

    filter3 = cursor.execute("SELECT COUNT (collection) FROM PC WHERE collection=(?)", ("Own",))
    for i in filter3:
        print("Total Own: " + str(i[0]) + " Games")

    print("\n--- Currently Own ---\n")

    filter4 = cursor.execute("SELECT COUNT (Format) FROM PC WHERE Format=(?) AND collection=(?)", ("Digital", "Own",))
    for i in filter4:
        print("Physical: " + str(i[0]) + " Games")

    print("\n--- Status ---\n")

    filter8 = cursor.execute("SELECT COUNT (status) FROM PC WHERE status=(?)", ("Completed",))
    for i in filter8:
        print("Completed: " + str(i[0]) + " Games")

    filter9 = cursor.execute("SELECT COUNT (status) FROM PC WHERE status=(?)", ("Finished",))
    for i in filter9:
        print("Finished: " + str(i[0]) + " Games")

    filter10 = cursor.execute("SELECT COUNT (playing) FROM PC WHERE playing=(?)", ("Y",))
    for i in filter10:
        print("Playing: " + str(i[0]) + " Games")

    filter11 = cursor.execute("SELECT name FROM PC WHERE playing=(?)", ("Y",))
    print("\n--- Currently Playing ---\n")
    for i in filter11:
        print("- " + str(i[0]))

def PS5():
    viewall = cursor.execute("SELECT DISTINCT name FROM PS5 order by release_date ASC;")
    for i in viewall:
        print("- " + i[0])

    print("\nHere is a breakdown of your Sony Playstation 5 Game Library (2020 - Present):\n")

    print("--- Collection ---\n")

    filter1 = cursor.execute("SELECT COUNT (name) FROM PS5")
    for i in filter1:
        print("Total Collected: " + str(i[0]) + " Games")

    filter2 = cursor.execute("SELECT COUNT (collection) FROM PS5 WHERE collection=(?)", ("Sold",))
    for i in filter2:
        print("Total Sold: " + str(i[0]) + " Games")

    filter3 = cursor.execute("SELECT COUNT (collection) FROM PS5 WHERE collection=(?)", ("Own",))
    for i in filter3:
        print("Total Own: " + str(i[0]) + " Games")

    print("\n--- Currently Own ---\n")

    filter4 = cursor.execute("SELECT COUNT (Format) FROM PS5 WHERE Format=(?) AND collection=(?)", ("Physical", "Own",))
    for i in filter4:
        print("Physical: " + str(i[0]) + " Games")

    filter5 = cursor.execute("SELECT COUNT (Format) FROM PS5 WHERE Format=(?)", ("PS Store",))
    for i in filter5:
        print("Digital (PS Store): " + str(i[0]) + " Games")

    filter6 = cursor.execute("SELECT COUNT (Format) FROM PS5 WHERE Format=(?)", ("PS Plus",))
    for i in filter6:
        print("Digital (PS Plus): " + str(i[0]) + " Games")

    filter7 = cursor.execute("SELECT COUNT (Format) FROM PS5 WHERE Format=(?)", ("F2P",))
    for i in filter7:
        print("Digital (F2P): " + str(i[0]) + " Games")

    print("\n--- Status ---\n")

    filter8 = cursor.execute("SELECT COUNT (status) FROM PS5 WHERE status=(?)", ("Completed",))
    for i in filter8:
        print("Completed: " + str(i[0]) + " Games")

    filter9 = cursor.execute("SELECT COUNT (status) FROM PS5 WHERE status=(?)", ("Finished",))
    for i in filter9:
        print("Finished: " + str(i[0]) + " Games")

    filter10 = cursor.execute("SELECT COUNT (playing) FROM PS5 WHERE playing=(?)", ("Y",))
    for i in filter10:
        print("Playing: " + str(i[0]) + " Games")

    filter11 = cursor.execute("SELECT name FROM PS5 WHERE playing=(?)", ("Y",))
    print("\n--- Currently Playing ---\n")
    for i in filter11:
        print("- " + str(i[0]))

def PS4():
    viewall = cursor.execute("SELECT DISTINCT name FROM PS4 order by release_date ASC;")
    for i in viewall:
        print("- " + i[0])

    print("\nHere is a breakdown of your Sony Playstation 4 Game Library (2013 - 2020):\n")

    print("--- Collection ---\n")

    filter1 = cursor.execute("SELECT COUNT (name) FROM PS4")
    for i in filter1:
        print("Total Collected: " + str(i[0]) + " Games")

    filter2 = cursor.execute("SELECT COUNT (collection) FROM PS4 WHERE collection=(?)", ("Sold",))
    for i in filter2:
        print("Total Sold: " + str(i[0]) + " Games")

    filter3 = cursor.execute("SELECT COUNT (collection) FROM PS4 WHERE collection=(?)", ("Own",))
    for i in filter3:
        print("Total Own: " + str(i[0]) + " Games")

    print("\n--- Currently Own ---\n")

    filter4 = cursor.execute("SELECT COUNT (Format) FROM PS4 WHERE Format=(?) AND collection=(?)", ("Physical", "Own",))
    for i in filter4:
        print("Physical: " + str(i[0]) + " Games")

    filter5 = cursor.execute("SELECT COUNT (Format) FROM PS4 WHERE Format=(?)", ("PS Store",))
    for i in filter5:
        print("Digital (PS Store): " + str(i[0]) + " Games")

    filter6 = cursor.execute("SELECT COUNT (Format) FROM PS4 WHERE Format=(?)", ("PS Plus",))
    for i in filter6:
        print("Digital (PS Plus): " + str(i[0]) + " Games")

    filter7 = cursor.execute("SELECT COUNT (Format) FROM PS4 WHERE Format=(?)", ("F2P",))
    for i in filter7:
        print("Digital (F2P): " + str(i[0]) + " Games")

    print("\n--- Status ---\n")

    filter8 = cursor.execute("SELECT COUNT (status) FROM PS4 WHERE status=(?)", ("Completed",))
    for i in filter8:
        print("Completed: " + str(i[0]) + " Games")

    filter9 = cursor.execute("SELECT COUNT (status) FROM PS4 WHERE status=(?)", ("Finished",))
    for i in filter9:
        print("Finished: " + str(i[0]) + " Games")

    filter10 = cursor.execute("SELECT COUNT (playing) FROM PS4 WHERE playing=(?)", ("Y",))
    for i in filter10:
        print("Playing: " + str(i[0]) + " Games")

    filter11 = cursor.execute("SELECT name FROM PS4 WHERE playing=(?)", ("Y",))
    print("\n--- Currently Playing ---\n")
    for i in filter11:
        print("- " + str(i[0]))

def SWITCH():
    viewall = cursor.execute("SELECT DISTINCT name FROM Switch order by release_date ASC;")
    for i in viewall:
        print("- " + i[0])

    print("\nHere is a breakdown of your Nintendo Switch Game Library (2017 - Present):\n")

    print("--- Collection ---\n")

    filter1 = cursor.execute("SELECT COUNT (name) FROM Switch")
    for i in filter1:
        print("Total Collected: " + str(i[0]) + " Games")

    filter2 = cursor.execute("SELECT COUNT (collection) FROM Switch WHERE collection=(?)", ("Sold",))
    for i in filter2:
        print("Total Sold: " + str(i[0]) + " Games")

    print("\n--- Currently Own ---\n")

    filter3 = cursor.execute("SELECT COUNT (collection) FROM Switch WHERE collection=(?)", ("Own",))
    for i in filter3:
        print("Total Own: " + str(i[0]) + " Games")

    filter4 = cursor.execute("SELECT COUNT (Format) FROM Switch WHERE Format=(?) AND collection=(?)",
                             ("Physical", "Own",))
    for i in filter4:
        print("Physical: " + str(i[0]) + " Games")

    filter5 = cursor.execute("SELECT COUNT (Format) FROM Switch WHERE Format=(?)", ("Nintendo Store",))
    for i in filter3:
        print("Digital: " + str(i[0]) + " Games")

    filter6 = cursor.execute("SELECT COUNT (Format) FROM Switch WHERE Format=(?)", ("F2P",))
    for i in filter6:
        print("Digital: " + str(i[0]) + " Games")

    print("\n--- Status ---\n")

    filter7 = cursor.execute("SELECT COUNT (status) FROM Switch WHERE status=(?)", ("Completed",))
    for i in filter7:
        print("Completed: " + str(i[0]) + " Games")

    filter8 = cursor.execute("SELECT COUNT (status) FROM Switch WHERE status=(?)", ("Finished",))
    for i in filter8:
        print("Finished: " + str(i[0]) + " Games")

    filter9 = cursor.execute("SELECT COUNT (playing) FROM Switch WHERE playing=(?)", ("Y",))
    for i in filter9:
        print("Playing: " + str(i[0]) + " Games")

    filter11 = cursor.execute("SELECT name FROM switch WHERE playing=(?)", ("Y",))
    print("\n--- Currently Playing ---\n")
    for i in filter11:
        print("- " + str(i[0]))

# Features

def add():
    print("--- Add Game ---\n")
    value1 = input("Enter Title: ")
    value2 = input("Enter Platform (PC / PS5 / PS4 / Switch / GBA): ").upper()
    value3 = input("Enter Release Date (YYYY-MM-DD): ")
    value4 = input("Enter Format (Physical / F2P / PS Store / PS Plus): ")

    cursor.execute("INSERT INTO " + value2 + " VALUES (?,?,?,?,?,NULL,NULL,NULL)", (value1, value2, value3, "Own", value4))
    connection.commit()
    print()
    print(value1 + " has now been added to " + value2 + " collection!")

def remove():
    print("--- Remove Game ---\n")
    value1 = input("Enter Title: ")
    value2 = input("Enter Platform (PC / PS5 / PS4 / Switch): ").upper()

    cursor.execute("DELETE FROM " + value2 + " WHERE name=(?)", (value1,))
    connection.commit()
    print()
    print(value1 + " has now been removed from " + value2 + " collection!")

def search():
    print("\n--- Search ---")
    print("\n- GBA"
          "\n- PC"
          "\n- PS5"
          "\n- PS4"
          "\n- Switch")

    main = input("\nEnter Platform: ")

    print("-----")
    if (main == "GBA") or (main == "Gba") or (main == "gBa") or (main == "gbA") or (main == "gba"):
        GBA()
        sub_menu()
    if (main == "PC") or (main == "pc") or (main == "Pc"):
        PC()
        sub_menu()
    elif (main == "PS5") or (main == "ps5") or (main == "Ps5")or (main == "pS5"):
        PS5()
        sub_menu()
    elif (main == "PS4") or (main == "ps4") or (main == "Ps4") or (main == "pS4"):
        PS4()
        sub_menu()
    elif (main == "SWITCH") or (main == "switch") or (main == "Switch"):
        SWITCH()
    else:
        print("\nNot a valid option. Please try again.")

def update():
    print("\n- GBA"
          "\n- PC"
          "\n- PS5"
          "\n- PS4"
          "\n- Switch")
    value1 = input("\nEnter Console: ").upper()
    update1 = cursor.execute("SELECT * FROM " + value1 + " order by release_date ASC;")
    for i in update1:
        print("- " + str(i[0]))
    value2 = input("\nWhich game would you like to update: ")
    update2 = cursor.execute("SELECT * FROM " + value1 + " where name =(?)", (value2,))
    global j

    for j in update2:
        print("Name: " + str(j[0]))
        print("Platform: " + str(j[1]))
        print("Release Date: " + str(j[2]))
        print("Collection: " + str(j[3]))
        print("Format: " + str(j[4]))
        print("Favourite: " + str(j[5]))
        print("Status: " + str(j[6]))
        print("Playing: " + str(j[7]))
    value3 = input("\nWhich value would you like to update: ")

    if value3 == "Name":
        try:
            print("\nGame: " + value2)
            value4 = input("\nEnter a new name: ")
            cursor.execute("UPDATE " + value1 + " SET name=(?) WHERE name=(?);", (value4, value2,))
            connection.commit()
            print("\nThis has been saved.")
        except:
            print("\nThere has been an error. Please try again.")

    elif value3 == "Platform":
        try:
            print("\nGame: " + value2)
            print("\nCurrent Value: " + j[1])
            value4 = input("Enter a new Value (GBA / PC / PS4 / PS5 / Switch): ")
            cursor.execute("UPDATE " + value1 + " SET platform=(?) WHERE name=(?) AND platform=(?);", (value4, value2, j[1],))
            connection.commit()
            sub_menu()
            print("\nThis has been saved.")
        except:
            print("\nThere has been an error. Please try again.")

    elif value3 == "Release Date":
        try:
            print("\nGame: " + value2)
            print("\nRelease Date: " + j[2])
            value4 = input("Enter a new Value (YYYY-MM-DD): ")
            cursor.execute("UPDATE " + value1 + " SET release_date=(?) WHERE name=(?) AND release_date=(?);", (value4, value2, j[2],))
            connection.commit()
            sub_menu()
            print("\nThis has been saved.")
        except:
            print("\nThere has been an error. Please try again.")

    elif value3 == "Collection":
        try:
            print("\nGame: " + value2)
            print("\nCollection: " + j[3])
            value4 = input("Enter a new Value (Own / Sold): ")
            cursor.execute("UPDATE " + value1 + " SET collection=(?) WHERE name=(?) AND collection=(?);", (value4, value2, j[3],))
            connection.commit()
            sub_menu()
            print("\nThis has been saved.")
        except:
            print("\nThere has been an error. Please try again.")

    elif value3 == "Format":
        try:
            print("\nGame: " + value2)
            print("\nFormat: " + j[4])
            value4 = input("Enter a new Value (Physical / F2P / PS Plus / PS Store): ")
            cursor.execute("UPDATE " + value1 + " SET format=(?) WHERE name=(?) AND format=(?);", (value4, value2, j[4],))
            connection.commit()
            sub_menu()
            print("\nThis has been saved.")
        except:
            print("\nThere has been an error. Please try again.")

    elif value3 == "Favourite":
        try:
            print("\nGame: " + value2)
            print("\nFavourite: " + j[5])
            value4 = input("Enter a new Value (Y or N): ")
            cursor.execute("UPDATE " + value1 + " SET favourite=(?) WHERE name=(?);", (value4, value2,))
            connection.commit()
            print("\nThis has been saved.")
            sub_menu()
        except:
            print("\nThere has been an error. Please try again.")

    elif value3 == "Status":
        try:
            print("\nGame: " + value2)
            print("\nStatus: " + j[6])
            value4 = input("Enter a new Value (Completed / Finished): ")
            cursor.execute("UPDATE " + value1 + " SET status=(?) WHERE name=(?);", (value4, value2,))
            connection.commit()
            print("\nThis has been saved.")
            sub_menu()
        except:
            print("\nThere has been an error. Please try again.")

    elif value3 == "Playing":
        try:
            print("\nGame: " + value2)
            print("\nPlaying: " + str(j[7]))
            value4 = input("Enter a new Value (Y or N): ")
            cursor.execute("UPDATE " + value1 + " SET playing=(?) WHERE name=(?);", (value4, value2,))
            connection.commit()
            print("\nThis has been saved.")
            sub_menu()
        except:
            print("\nThere has been an error. Please try again.")



# Main Menu

def main_menu():
    print("\n--- Main Menu ---\n")
    print("1. Add a Game\n"
          "2. Remove a Game\n"
          "3. Search Games\n"
          "4. Currently Playing\n"
          "5. Completed\n"
          "6. Beaten\n"
          "7. Favourites\n"
          "8. Update\n")

    Q1 = input("Select an option: ")

    if Q1 == "1":
        add()
        sub_menu()
    elif Q1 == "2":
        remove()
        sub_menu()
    elif Q1 == "3":
        search()
        sub_menu()
    elif Q1 == "4":
        testing = cursor.execute("select * from PS5 where playing=(?) union select * from PS4 where playing=(?) union select * from PC where playing=(?) union select * from switch where playing=(?) ORDER BY platform ASC", ("Y", "Y", "Y", "Y",))
        print("\n--- Currenty Playing ---\n")
        for i in testing:
            print("- " + i[0] + " | " + i[1])
        sub_menu()
    elif Q1 == "5":
        testing = cursor.execute("select * from PS5 where status=(?) union select * from PS4 where status=(?) union select * from PC where status=(?) union select * from switch where status=(?) ORDER BY platform ASC", ("Completed", "Completed", "Completed", "Completed",))
        print("\n--- Completed ---\n")
        for i in testing:
            print("- " + i[0] + " | " + i[1])
        sub_menu()
    elif Q1 == "6":
        testing = cursor.execute("select * from PS5 where status=(?) union select * from PS4 where status=(?) union select * from PC where status=(?) union select * from switch where status=(?) ORDER BY platform ASC", ("Finished", "Finished", "Finished", "Finished",))
        print("\n--- Finished ---\n")
        for i in testing:
            print("- " + i[0] + " | " + i[1])
        sub_menu()
    elif Q1 == "7":
        testing = cursor.execute("select * from PS5 where favourite=(?) union select * from PS4 where favourite=(?) union select * from PC where favourite=(?) union select * from switch where favourite=(?) ORDER BY platform ASC", ("Y", "Y", "Y", "Y",))
        print("\n--- Favourite Games ---\n")
        for i in testing:
            print("- " + i[0] + " | " + i[1])
        sub_menu()
    elif Q1 == "8":
        update()
    else:
        print("Incorrect option, please try again.")
        main_menu()

main_menu()
