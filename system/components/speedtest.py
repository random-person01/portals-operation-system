import urllib
from urllib.request import urlopen
from time import sleep


def is_internet():
    """
    Query internet using python
    """
    try:
        urlopen('https://www.google.com', timeout=1)
        return True
    except urllib.error.URLError as Error:
        print(Error)
        return False


def wait(n, stuff):
    sleep(n)
    print(stuff)


def main():
    wait(2, "Checking Status")
    wait(2, "... ... ...")
    wait(3, "Almost completed")
    sleep(1)
    if is_internet():
        print("Internet is active")
    else:
        print("Internet disconnected")
