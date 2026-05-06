from logic import add, view, search, delete
import sys
import os
import json

BASE_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(BASE_DIR, "data.json")

try:
    with open(DATA_FILE) as file:
        information = json.load(file)
except FileNotFoundError:
    with open(DATA_FILE, "x") as file:
        json.dump({}, file)
    with open(DATA_FILE) as file:
        information = json.load(file)

if len(sys.argv) == 1:
    sys.exit("Use the commands 'add' 'view' 'search' 'delete' to use program")

if sys.argv[1] == "add":
    tag = input("Tag: ").strip().lower()
    title = input("Title: ").strip().lower()
    content = input("Content: ").strip()

    print(add(tag, title, content, information))

elif sys.argv[1] == "view":
    view(information)

elif sys.argv[1] == "search":
    tag = input("Tag: ").lower().strip()
    title = input("Title: ").lower().strip()

    print(search(tag, title, information))

elif sys.argv[1] == "delete":
    tag = input("Tag: ").lower().strip()
    title = input("Title: ").lower().strip()
    print(delete(information, tag, title))

else:
    print("Invalid input")