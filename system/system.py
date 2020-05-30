import easygui
import json
from components.long_date import long_date
from components.speedtest import main
from components.editor import execute
from components.calculator import run

apps = ["calculator", "text editor"]
filename = 'username.json'


def record_username():
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
record_username()

cmd = input("Please enter a command: ")

if cmd == 'plain text':
    execute()
elif cmd == 'tests':
    main()
elif cmd == 'calculator':
    run()
else:
    print("Invalid command")
