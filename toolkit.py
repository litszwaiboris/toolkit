import os
import time


def launchpadApps():
    os.system('clear')
    appname = input("Please enter the app name that you want to delete: ")
    print("DO YOU WANT TO DELETE " + appname + "?")
    choice = input("Enter Y to CONFIRM. Enter N to DECLINE and retype. Enter other key to exit: ")
    if choice == "Y":
        os.system('sqlite3 $(getconf DARWIN_USER_DIR)com.apple.dock.launchpad/db/db "DELETE FROM apps WHERE title='+"'"+appname+"'"+'"')
        os.system('killall Dock')
        print("You deleted " + appname + ".")
    elif choice == "N":
        launchpadApps()
    else:
        main()


def resetLaunchpad():
    os.system('clear')
    print("Are you sure to reset the launchpad. This operation cannot be rollback!")
    choice = input("Enter Y to confirm. Enter N to leave and go back to main menu: ")
    if choice == "Y":
        os.system("default write com.apple.dock ResetLaunchPad -bool true")
        os.system("killall Dock")
        print("Launchpad have been reset.")
    elif choice == "N":
        main()
    else:
        print("Please enter Y or N")
        time.sleep(1)
        resetLaunchpad()


def main():
    os.system('clear')
    print("Boris' Toolkit for Mac v1.0")
    print("Hello user. Please choose your choice of function")
    print("1. Delete Launchpad Apps")
    print("2. Reset Launchpad")
    print("3. Exit Toolkit")
    main_choose = input("Function number: ")
    if main_choose == "1":
        launchpadApps()
    elif main_choose == "2":
        resetLaunchpad()
    elif main_choose == "3":
        SystemExit(0)
    else:
        print("You typed the wrong function number.")
        print("Y) Try Again")
        print("N) Leave")
        main_choose_exit = input("Choice: ")
        if main_choose_exit == "Y":
            main()
        else:
            SystemExit(0)


if __name__ == "__main__":
    main()
