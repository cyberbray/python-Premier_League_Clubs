
import os
import sys

def menu():
    print("****MENU****\n")
    print("1. Start")
    print("2. HACK")
    print("3. Quit")

    choice = input("\nCommand: ")
    validate_choice(choice,1,3)

    if choice == '1':
        print()

    elif choice == '2':
        print()

    else:
        print("\nError.")
        sys.exit(0)

def validate_choice(choice, first_num, last_num):
    error_message = '\nYou should provide a number between {} and {}.'.format(first_num, last_num)

    while True:
        if choice.isdigit():
            if int(choice) not in range(first_num,last_num+1):
                print(error_message)
                choice = input()
            else:
                break
        else:
            print(error_message)
            choice = input()
