import easygui
import json
from components.long_date import long_date
from components.editor import execute
from components.calculator import run
from components.pie_chart import plot
from components.financial import main

filename = 'username.json'


def username():
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("Please enter your username: ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you the next time you come back, {username}")
    else:
        print(f"Welcome back, {username}!")


# the main program
easygui.msgbox("- All functions working", "version 1.0.0")
print("Hello")
long_date()
print("Welcome to the Portals Operation System")
print("Enter calculator for calculator, text for the text editor, tests to see if your internet connection is active")
username()

cmd = input("Please enter a command: ")

if cmd == 'plain text':
    execute()
elif cmd == 'calculator':
    run()
elif cmd == 'poll':
    plot()
elif cmd == 'income':
    main()
else:
    print("Invalid command")
