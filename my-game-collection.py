# Modules

import sqlite3
import os
import sys

# Variables

user = os.getlogin()
db = os.path.join(fr"C:\Users\{user}\Dropbox\Dev\Python\Projects\My Game Collection\db\games.db")
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

    print("--- Collection ---\n")

    sql_totalgamecount = cursor.execute("SELECT COUNT (name) FROM GBA")
    for i in sql_totalgamecount:
        print(f"Total Games Collected: {str(i[0])} Games")

    sql_physicalgamecount = cursor.execute("SELECT COUNT (collection) FROM GBA WHERE collection=(?)", ("Sold",))
    for i in sql_physicalgamecount:
        print(f"Physical Games Sold: {str(i[0])} Games")

    sql_currentgamesowned = cursor.execute("SELECT COUNT (collection) FROM GBA WHERE collection=(?)", ("Own",))
    for i in sql_currentgamesowned:
        print(f"Current GBA Games Owned: {str(i[0])} Games")

    print("\n--- Currently Playing ---\n")

    filter11 = cursor.execute("SELECT name FROM GBA WHERE playing=(?)", ("Y",))
    for i in filter11:
        print(f"- {str(i[0])}")

    print("\n--- GBA Game Collection ---")

    sql_physicallcount = cursor.execute("SELECT COUNT (Format) FROM GBA WHERE Format=(?) and collection=(?)", ("Physical", "Own",))
    for i in sql_physicallcount:
        print(f"\nPhysical: {str(i[0])} Games\n")

    sql_physicallist = cursor.execute("SELECT DISTINCT name FROM GBA where format=(?) and collection=(?) order by release_date ASC;", ("Physical", "Own",))
    for i in sql_physicallist:
        print(f"- {i[0]}")

def PC():
    print("\nHere is a breakdown of your PC Game Library (1993 - Present):\n")

    print("--- Collection ---\n")

    sql_totalgamecount = cursor.execute("SELECT COUNT (name) FROM PC")
    for i in sql_totalgamecount:
        print(f"Total Games Collected: {str(i[0])} Games")

    sql_physicalgamecount = cursor.execute("SELECT COUNT (collection) FROM PC WHERE collection=(?)", ("Sold",))
    for i in sql_physicalgamecount:
        print(f"Physical Games Sold: {str(i[0])} Games")

    sql_currentgamesowned = cursor.execute("SELECT COUNT (collection) FROM PC WHERE collection=(?)", ("Own",))
    for i in sql_currentgamesowned:
        print(f"Current PC Games Owned: {str(i[0])} Games")

    print("\n--- Currently Playing ---\n")

    filter11 = cursor.execute("SELECT name FROM PC WHERE playing=(?)", ("Y",))
    for i in filter11:
        print(f"- {str(i[0])}")

    print("\n--- PC Game Collection ---")

    sql_digitalcount = cursor.execute("SELECT COUNT (Format) FROM PC WHERE Format=(?)", ("Digital",))
    for i in sql_digitalcount:
        print(f"\nDigital: {str(i[0])} Games\n")

    sql_digitallist = cursor.execute("SELECT DISTINCT name FROM PC where format=(?) order by release_date ASC;", ("Digital",))
    for i in sql_digitallist:
        print(f"- {i[0]}")

    sql_f2plcount = cursor.execute("SELECT COUNT (Format) FROM PC WHERE Format=(?)", ("F2P",))
    for i in sql_f2plcount:
        print(f"\nF2P (Free to Play): {str(i[0])} Games\n")

    sql_f2plist = cursor.execute("SELECT DISTINCT name FROM PC where format=(?) order by release_date ASC;", ("F2P",))
    for i in sql_f2plist:
        print(f"- {i[0]}")

def PS5():

    print("\nHere is a breakdown of your Sony Playstation 5 Game Library (2020 - Present):\n")

    print("--- Collection ---\n")

    sql_totalgamecount = cursor.execute("SELECT COUNT (name) FROM PS5")
    for i in sql_totalgamecount:
        print(f"Total Games Collected: {str(i[0])} Games")

    sql_physicalgamecount = cursor.execute("SELECT COUNT (collection) FROM PS5 WHERE collection=(?)", ("Sold",))
    for i in sql_physicalgamecount:
        print(f"Physical Games Sold: {str(i[0])} Games")

    sql_currentgamesowned = cursor.execute("SELECT COUNT (collection) FROM PS5 WHERE collection=(?)", ("Own",))
    for i in sql_currentgamesowned:
        print(f"Current PS5 Games Owned: {str(i[0])} Games")

    print("\n--- Currently Playing ---\n")

    filter11 = cursor.execute("SELECT name FROM PS5 WHERE playing=(?)", ("Y",))
    for i in filter11:
        print(f"- {str(i[0])}")

    print("\n--- PS5 Game Collection ---")

    sql_physicallcount = cursor.execute("SELECT COUNT (Format) FROM PS5 WHERE Format=(?) and collection=(?)", ("Physical", "Own",))
    for i in sql_physicallcount:
        print(f"\nPhysical: {str(i[0])} Games\n")

    sql_physicallist = cursor.execute("SELECT DISTINCT name FROM PS5 where format=(?) and collection=(?) order by release_date ASC;", ("Physical", "Own",))
    for i in sql_physicallist:
        print(f"- {i[0]}")

    sql_digitalcount = cursor.execute("SELECT COUNT (Format) FROM PS5 WHERE Format=(?)", ("Digital",))
    for i in sql_digitalcount:
        print(f"\nDigital: {str(i[0])} Games\n")

    sql_digitallist = cursor.execute("SELECT DISTINCT name FROM PS5 where format=(?) order by release_date ASC;", ("Digital",))
    for i in sql_digitallist:
        print(f"- {i[0]}")

    sql_f2plcount = cursor.execute("SELECT COUNT (Format) FROM PS5 WHERE Format=(?)", ("F2P",))
    for i in sql_f2plcount:
        print(f"\nF2P (Free to Play): {str(i[0])} Games\n")

    sql_f2plist = cursor.execute("SELECT DISTINCT name FROM PS5 where format=(?) order by release_date ASC;", ("F2P",))
    for i in sql_f2plist:
        print(f"- {i[0]}")

    sql_pspluscount = cursor.execute("SELECT COUNT (Format) FROM PS5 WHERE Format=(?)", ("PS Plus",))
    for i in sql_pspluscount:
        print(f"\nPS Plus: {str(i[0])} Games\n")

    sql_pspluslist = cursor.execute("SELECT DISTINCT name FROM PS5 where format=(?) order by release_date ASC;", ("PS Plus",))
    for i in sql_pspluslist:
        print(f"- {i[0]}")

def PS4():

    print("\nHere is a breakdown of your Sony Playstation 4 Game Library (2013 - Present):\n")

    print("--- Collection ---\n")

    sql_totalgamecount = cursor.execute("SELECT COUNT (name) FROM PS4")
    for i in sql_totalgamecount:
        print(f"Total Games Collected: {str(i[0])} Games")

    sql_physicalgamecount = cursor.execute("SELECT COUNT (collection) FROM PS4 WHERE collection=(?)", ("Sold",))
    for i in sql_physicalgamecount:
        print(f"Physical Games Sold: {str(i[0])} Games")

    sql_currentgamesowned = cursor.execute("SELECT COUNT (collection) FROM PS4 WHERE collection=(?)", ("Own",))
    for i in sql_currentgamesowned:
        print(f"Current PS4 Games Owned: {str(i[0])} Games")

    print("\n--- Currently Playing ---\n")

    filter11 = cursor.execute("SELECT name FROM PS4 WHERE playing=(?)", ("Y",))
    for i in filter11:
        print(f"- {str(i[0])}")

    print("\n--- PS4 Game Collection ---")

    sql_physicallcount = cursor.execute("SELECT COUNT (Format) FROM PS4 WHERE Format=(?) and collection=(?)", ("Physical", "Own",))
    for i in sql_physicallcount:
        print(f"\nPhysical: {str(i[0])} Games\n")

    sql_physicallist = cursor.execute("SELECT DISTINCT name FROM PS4 where format=(?) and collection=(?) order by release_date ASC;", ("Physical", "Own",))
    for i in sql_physicallist:
        print(f"- {i[0]}")

    sql_digitalcount = cursor.execute("SELECT COUNT (Format) FROM PS4 WHERE Format=(?)", ("Digital",))
    for i in sql_digitalcount:
        print("\nDigital: {str(i[0])} Games\n")

    sql_digitallist = cursor.execute("SELECT DISTINCT name FROM PS4 where format=(?) order by release_date ASC;", ("Digital",))
    for i in sql_digitallist:
        print(f"- {i[0]}")

    sql_f2plcount = cursor.execute("SELECT COUNT (Format) FROM PS4 WHERE Format=(?)", ("F2P",))
    for i in sql_f2plcount:
        print(f"\nF2P (Free to Play): {str(i[0])} Games\n")

    sql_f2plist = cursor.execute("SELECT DISTINCT name FROM PS4 where format=(?) order by release_date ASC;", ("F2P",))
    for i in sql_f2plist:
        print(f"- {i[0]}")

    sql_pspluscount = cursor.execute("SELECT COUNT (Format) FROM PS4 WHERE Format=(?)", ("PS Plus",))
    for i in sql_pspluscount:
        print(f"\nPS Plus: {str(i[0])} Games\n")

    sql_pspluslist = cursor.execute("SELECT DISTINCT name FROM PS4 where format=(?) order by release_date ASC;", ("PS Plus",))
    for i in sql_pspluslist:
        print(f"- {i[0]}")

def SWITCH():

    print("\nHere is a breakdown of your Nintendo Switch Game Library (2017 - Present):\n")

    print("--- Collection ---\n")

    sql_totalgamecount = cursor.execute("SELECT COUNT (name) FROM Switch")
    for i in sql_totalgamecount:
        print(f"Total Games Collected: {str(i[0])} Games")

    sql_physicalgamecount = cursor.execute("SELECT COUNT (collection) FROM Switch WHERE collection=(?)", ("Sold",))
    for i in sql_physicalgamecount:
        print(f"Physical Games Sold: {str(i[0])} Games")

    sql_currentgamesowned = cursor.execute("SELECT COUNT (collection) FROM Switch WHERE collection=(?)", ("Own",))
    for i in sql_currentgamesowned:
        print(f"Current Switch Games Owned: {str(i[0])} Games")

    print("\n--- Currently Playing ---\n")

    filter11 = cursor.execute("SELECT name FROM Switch WHERE playing=(?)", ("Y",))
    for i in filter11:
        print(f"- {str(i[0])}")

    print("\n--- Switch Game Collection ---")

    sql_physicallcount = cursor.execute("SELECT COUNT (Format) FROM Switch WHERE Format=(?) and collection=(?)", ("Physical", "Own",))
    for i in sql_physicallcount:
        print(f"\nPhysical: {str(i[0])} Games\n")

    sql_physicallist = cursor.execute("SELECT DISTINCT name FROM Switch where format=(?) and collection=(?) order by release_date ASC;", ("Physical", "Own",))
    for i in sql_physicallist:
        print(f"- {i[0]}")

    sql_digitalcount = cursor.execute("SELECT COUNT (Format) FROM Switch WHERE Format=(?)", ("Digital",))
    for i in sql_digitalcount:
        print(f"\nDigital: {str(i[0])} Games\n")

    sql_digitallist = cursor.execute("SELECT DISTINCT name FROM Switch where format=(?) order by release_date ASC;", ("Digital",))
    for i in sql_digitallist:
        print(f"- {i[0]}")

    sql_f2plcount = cursor.execute("SELECT COUNT (Format) FROM Switch WHERE Format=(?)", ("F2P",))
    for i in sql_f2plcount:
        print(f"\nF2P (Free to Play): {str(i[0])} Games\n")

    sql_f2plist = cursor.execute("SELECT DISTINCT name FROM Switch where format=(?) order by release_date ASC;", ("F2P",))
    for i in sql_f2plist:
        print(f"- {i[0]}")

# Features

def add():
    print("--- Add Game ---\n")
    value1 = input("Enter Title: ")
    value2 = input("Enter Platform (PC / PS5 / PS4 / Switch / GBA): ").upper()
    value3 = input("Enter Release Date (YYYY-MM-DD): ")
    value4 = input("Enter Format (Physical / F2P / PS Store / PS Plus): ")

    cursor.execute(f"INSERT INTO {value2} VALUES (?,?,?,?,?,NULL,NULL,NULL)", (value1, value2, value3, "Own", value4))
    connection.commit()
    print()
    print(f"{value1} has now been added to {value2} collection!")

def remove():
    print("--- Remove Game ---\n")
    value1 = input("Enter Title: ")
    value2 = input("Enter Platform (PC / PS5 / PS4 / Switch): ").upper()

    cursor.execute(f"DELETE FROM {value2} WHERE name=(?)", (value1,))
    connection.commit()
    print()
    print(f"{value1} has now been removed from {value2} collection!")

def search():
    print("\n--- Search ---")
    print("\n- GBA"
          "\n- PC"
          "\n- PS5"
          "\n- PS4"
          "\n- Switch")

    main = input("\nEnter Platform: ")

    clear()
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
        clear()
        print("\nNot a valid option. Please try again.")
        search()

def update():
    print("\n- GBA"
          "\n- PC"
          "\n- PS5"
          "\n- PS4"
          "\n- Switch")
    value1 = input("\nEnter Console: ").upper()
    update1 = cursor.execute(f"SELECT * FROM {value1} order by release_date ASC;")
    for i in update1:
        print(f"- {str(i[0])}")
    value2 = input("\nWhich game would you like to update: ")
    update2 = cursor.execute(f"SELECT * FROM {value1} where name =(?)", (value2,))
    global j

    for j in update2:
        print(f"Name: {str(j[0])}")
        print(f"Platform: {str(j[1])}")
        print(f"Release Date: {str(j[2])}")
        print(f"Collection: {str(j[3])}")
        print(f"Format: {str(j[4])}")
        print(f"Favourite: {str(j[5])}")
        print(f"Status: {str(j[6])}")
        print(f"Playing: {str(j[7])}")
    value3 = input("\nWhich value would you like to update: ")

    if value3 == "Name":
        try:
            print(f"\nGame: : {value2}")
            value4 = input("\nEnter a new name: ")
            cursor.execute(f"UPDATE {value1} SET name=(?) WHERE name=(?);", (value4, value2,))
            connection.commit()
            print("\nThis has been saved.")
        except:
            print("\nThere has been an error. Please try again.")

    elif value3 == "Platform":
        try:
            print(f"\nGame: : {value2}")
            print(f"\nCurrent Value: {j[1]}")
            value4 = input("Enter a new Value (GBA / PC / PS4 / PS5 / Switch): ")
            cursor.execute(f"UPDATE {value1} SET platform=(?) WHERE name=(?) AND platform=(?);", (value4, value2, j[1],))
            connection.commit()
            sub_menu()
            print("\nThis has been saved.")
        except:
            print("\nThere has been an error. Please try again.")

    elif value3 == "Release Date":
        try:
            print(f"\nGame: {value2}")
            print(f"\nRelease Date: {j[2]}")
            value4 = input("Enter a new Value (YYYY-MM-DD): ")
            cursor.execute(f"UPDATE {value1} SET release_date=(?) WHERE name=(?) AND release_date=(?);", (value4, value2, j[2],))
            connection.commit()
            sub_menu()
            print("\nThis has been saved.")
        except:
            print("\nThere has been an error. Please try again.")

    elif value3 == "Collection":
        try:
            print(f"\nGame: {value2}")
            print(f"\nCollection: {j[3]}")
            value4 = input("Enter a new Value (Own / Sold): ")
            cursor.execute(f"UPDATE {value1} SET collection=(?) WHERE name=(?) AND collection=(?);", (value4, value2, j[3],))
            connection.commit()
            sub_menu()
            print("\nThis has been saved.")
        except:
            print("\nThere has been an error. Please try again.")

    elif value3 == "Format":
        try:
            print(f"\nGame: {value2}")
            print(f"\nFormat: {j[4]}")
            value4 = input("Enter a new Value (Physical / F2P / PS Plus / PS Store): ")
            cursor.execute(f"UPDATE {value1} SET format=(?) WHERE name=(?) AND format=(?);", (value4, value2, j[4],))
            connection.commit()
            sub_menu()
            print("\nThis has been saved.")
        except:
            print("\nThere has been an error. Please try again.")

    elif value3 == "Favourite":
        try:
            print(f"\nGame: {value2}")
            print(f"\nFavourite: {j[5]}")
            value4 = input("Enter a new Value (Y or N): ")
            cursor.execute(f"UPDATE {value1} SET favourite=(?) WHERE name=(?);", (value4, value2,))
            connection.commit()
            print("\nThis has been saved.")
            sub_menu()
        except:
            print("\nThere has been an error. Please try again.")

    elif value3 == "Status":
        try:
            print(f"\nGame: {value2}")
            print(f"\nStatus: {j[6]}")
            value4 = input("Enter a new Value (Completed / Finished): ")
            cursor.execute(f"UPDATE {value1} SET status=(?) WHERE name=(?);", (value4, value2,))
            connection.commit()
            print("\nThis has been saved.")
            sub_menu()
        except:
            print("\nThere has been an error. Please try again.")

    elif value3 == "Playing":
        try:
            print(f"\nGame: {value2}")
            print(f"\nPlaying: {str(j[7])}")
            value4 = input("Enter a new Value (Y or N): ")
            cursor.execute(f"UPDATE {value1} SET playing=(?) WHERE name=(?);", (value4, value2,))
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
        clear()
        add()
        sub_menu()
    elif Q1 == "2":
        clear()
        remove()
        sub_menu()
    elif Q1 == "3":
        clear()
        search()
        sub_menu()
    elif Q1 == "4":
        clear()
        testing = cursor.execute("select * from PS5 where playing=(?) union select * from PS4 where playing=(?) union select * from PC where playing=(?) union select * from switch where playing=(?) ORDER BY platform ASC", ("Y", "Y", "Y", "Y",))
        print("\n--- Currenty Playing ---\n")
        for i in testing:
            print(f"- {i[0]} | {i[1]}")
        sub_menu()
    elif Q1 == "5":
        clear()
        testing = cursor.execute("select * from PS5 where status=(?) union select * from PS4 where status=(?) union select * from PC where status=(?) union select * from switch where status=(?) ORDER BY platform ASC", ("Completed", "Completed", "Completed", "Completed",))
        print("\n--- Completed ---\n")
        for i in testing:
            print(f"- {i[0]} | {i[1]}")
        sub_menu()
    elif Q1 == "6":
        clear()
        testing = cursor.execute("select * from PS5 where status=(?) union select * from PS4 where status=(?) union select * from PC where status=(?) union select * from switch where status=(?) ORDER BY platform ASC", ("Finished", "Finished", "Finished", "Finished",))
        print("\n--- Finished ---\n")
        for i in testing:
            print(f"- {i[0]} | {i[1]}")
        sub_menu()
    elif Q1 == "7":
        clear()
        testing = cursor.execute("select * from PS5 where favourite=(?) union select * from PS4 where favourite=(?) union select * from PC where favourite=(?) union select * from switch where favourite=(?) ORDER BY platform ASC", ("Y", "Y", "Y", "Y",))
        print("\n--- Favourite Games ---\n")
        for i in testing:
            print(f"- {i[0]} | {i[1]}")
        sub_menu()
    elif Q1 == "8":
        clear()
        update()
    else:
        print("Incorrect option, please try again.")
        main_menu()

main_menu()
