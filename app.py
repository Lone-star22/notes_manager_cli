from logic import add, view, search, delete
import sys

if len(sys.argv) == 1:
    sys.exit("Use the commands 'add' 'view' 'search' 'delete' to use program")

if sys.argv[1] == "add":
    title = input("title: ").strip().lower()
    content = input("Content: ").strip()
    tag = input("Tag: ").strip().lower()

    if not add(title, content, tag):
        print("Please input title, content and tag of note")

elif sys.argv[1] == "view":
    if not view():
        print("No results")

elif sys.argv[1] == "search":
    if len(sys.argv) == 4:
        if not search(sys.argv[2].lower(), sys.argv[3].lower()):
            print("No results")
    else:
        print("Please input note (title) + (tag)")

elif sys.argv[1] == "delete":
    if len(sys.argv) == 4:
        if not delete(sys.argv[2], sys.argv[3]):
            print("Invalid tag or title")
    else:
        print("Please input note (title) + (tag)")

else:
    print("Invalid input")