import argparse
import sys

from logic import Note
from storage import load, save
from validation import validation

parser = argparse.ArgumentParser(description="This is a CLI program that let's you store and track your notes.")

parser.add_argument("--add", help="add notes or update existing ones in the format (tags) (title) (content)", nargs=3, type=str)
parser.add_argument("--search", help="search for a note in the format (tag) (title)", nargs=2)
parser.add_argument("--delete", help="delete a note in a tag in the format (tag) (tile)", nargs=2)
parser.add_argument("--view", help="view all notes stored", action="store_true")
parser.add_argument("--edit", help="change the name of a tag to new one in format (old tag) (new tag)", nargs=2)
parser.add_argument("--history", help="view command history", action="store_true")

args = parser.parse_args()

information = load()

validate = validation(information=information)
if not validate:
    sys.exit("Invalid structure")

if args.add:
    validate = validation(tag=args.add[0], title=args.add[1])
    if not validate:
        sys.exit("Invalid Input")

    note = Note(tag=args.add[0].lower(), title=args.add[1].lower(), content=args.add[2])
    print(note.add(information))
    save(command="add")

elif args.search:
    validate = validation(tag=args.search[0], title=args.search[1])
    if not validate:
        sys.exit("Invalid Input")

    note = Note(tag=args.search[0].lower(), title=args.search[1].lower())
    print(note.search(information))
    save(command="search")

elif args.delete:
    validate = validation(tag=args.delete[0], title=args.delete[1])
    if not validate:
        sys.exit("Invalid Input")

    note = Note(tag=args.delete[0].lower(), title=args.delete[1].lower())
    print(note.delete(information))
    save(command="delete")

elif args.view:
    note = Note()
    note.view(information)
    save(command="view")

elif args.edit:
    validate = validation(tag=args.edit[0], new_tag=args.edit[1])
    if not validate:
        sys.exit("Invalid Input")

    note = Note(tag=args.edit[0].lower())
    print(note.edit_tag(information, args.edit[1]))
    save(command="edit")

elif args.history:
    load(history=True, load_notes=False)