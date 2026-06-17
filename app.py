import argparse
import sys

from logic import Note, NotesManager
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
    notes_manager = NotesManager()

    updated_info = notes_manager.add(note, information)
    print("Note added successfuly")
    save(command="add", information=updated_info)

elif args.search:
    validate = validation(tag=args.search[0], title=args.search[1])
    if not validate:
        sys.exit("Invalid Input")

    note = Note(tag=args.search[0].lower(), title=args.search[1].lower())
    notes_manager = NotesManager()

    print(notes_manager.search(note, information))
    save(command="search")

elif args.delete:
    validate = validation(tag=args.delete[0], title=args.delete[1])
    if not validate:
        sys.exit("Invalid Input")

    note = Note(tag=args.delete[0].lower(), title=args.delete[1].lower())
    notes_manager = NotesManager()

    updated_info = notes_manager.delete(note, information)
    if not isinstance(updated_info, dict):
        sys.exit("Invalid tag/title")

    print("Note deleted successfully")
    save(command="delete", information=updated_info)
    

elif args.view:
    notes_manager = NotesManager()
    notes_manager.view(information)
    save(command="view")

elif args.edit:
    validate = validation(tag=args.edit[0], new_tag=args.edit[1])
    if not validate:
        sys.exit("Invalid Input")

    note = Note(tag=args.edit[0].lower())
    notes_manager = NotesManager()
    
    updated_info = notes_manager.edit_tag(note, information, args.edit[1])
    if not isinstance(updated_info, dict):
        sys.exit("Invalid tag")

    save(command="edit", information=updated_info)
    print("Tag edited successfully")
    
elif args.history:
    load(history=True, load_notes=False)
    save(command="history")