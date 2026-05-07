from logic import add, view, search, delete, edit_tag
import sys
import os
import json

BASE_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_DIR, "data.json")
TEXT_FILE = os.path.join(BASE_DIR, "command.txt")

if not os.path.exists(TEXT_FILE):
    with open(TEXT_FILE, "x") as file:
        ...
if not os.path.exists(JSON_FILE):
    with open(JSON_FILE, "x") as file:
        json.dump({}, file)

with open(JSON_FILE) as file:
    information = json.load(file)

if len(sys.argv) == 1:
    sys.exit("Use the commands 'add' 'view' 'search' 'delete' 'history' to use program")

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

elif sys.argv[1] == "edit":
    old_tag = input("Old Tag: ").lower().strip()
    new_tag = input("New Tag: ").lower().strip()
    print(edit_tag(old_tag, new_tag, information))

elif sys.argv[1] == "history":
    with open(TEXT_FILE) as file:
        for line in file:
            print(line.rstrip())

else:
    sys.exit("Invalid input")

with open(TEXT_FILE, "a") as file:
    file.write(f"{sys.argv[1]}\n")