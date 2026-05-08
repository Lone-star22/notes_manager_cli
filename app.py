from logic import add, view, search, delete, edit_tag
from storage import load, save
import sys

information = load()

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
    load(history=True)

else:
    sys.exit("Invalid input")

save(command=sys.argv[1])