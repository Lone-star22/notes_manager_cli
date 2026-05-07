import json
import os

BASE_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_DIR, "data.json")

def add(tag, title, content, information):
    #Check if the all arguments have values
    if not title or not content or not tag:
        return "Please input title, content and tag of note"
    
    #creation of the needed timestamp
    from datetime import datetime as dt
    timestamp = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    
    #Add note if it doesn't exist else update the existing one
    the_tag = information.get(tag, {})
    note = the_tag.get(title, {})
    if not note:
        the_tag[title] = {"content": content, "date": timestamp}
    else:
        note["content"] = f"{note['content']}. {content}"
        note["date"] = timestamp
    information[tag] = the_tag
    
    #Writing back to the json file after the above changes
    with open(JSON_FILE, "w") as file:
        json.dump(information, file, indent=4)
        return "Note successfully added"


def view(information):
    #Check if data file exists
    if not information:
        print("No results")
        return
    
    #Print the name of the tags alongside all notes associated with them
    max_count, max_tag = 0, None
    for tag in information:
        print(f"Tag: {tag.upper()}\nNotes:")
        if len(information[tag]) > max_count:
            max_count = len(information[tag])
            max_tag = tag
        for title in sorted(information[tag]):
            print(f"     {title.title()}")
    
    print(f"Most Used Tag: {max_tag.title()} -- Number Of Times: {max_count}")
    

def search(tag, title, information):
    #Check if data file exists
    if not information:
        return "No notes to search"
    if not title or not tag:
        return "Please input note 'title' and 'tag'"
    
    #Handle output for user's search
    the_tag = information.get(tag, {})
    if not the_tag:
        return "Invalid tag"
    note = the_tag.get(title, {})
    if not note:
        return "Invalid title"
    return f"Tag: {tag.title()}    Title: {title.title()}    Date Created: {note["date"]}\n\nContent: \n{note["content"]}"


def delete(information, tag=None, title=None):
    #Check if data file exists
    if not information:
        return "No notes to delete"
    
    #Handle user inputs for tag OR title
    if not title and not tag:
        return "Please input note 'title' or/and 'tag'"
    if not tag:
        for tags in information:
            popped = information[tags].pop(title, None)
            if not popped:
                return "Invalid title"
    if not title:
        popped = information.pop(tag, None)
        if not popped:
            return "Invalid tag"

    #Handle user input for tag AND title
    if title and tag:
        the_tag = information.get(tag, {})
        if not the_tag:
            return "Invalid tag"
        note = the_tag.get(title, {})
        if not note:
            return "Invalid title"
        information[tag].pop(title)

    #Write back to the json file after the above changes
    with open(JSON_FILE, "w") as file:
        json.dump(information, file, indent=4)
    return "Successfully deleted"

def edit_tag(old_tag, new_tag, information):
    #Check if information, old and new tag exits
    if not information:
        return "No tags to edit"
    if not old_tag or not new_tag:
        return "Please input 'old tag' and 'new tag'" 
    
    #Handle user input for tag to be updated
    the_tag = information.get(old_tag, {})
    if not the_tag:
        return "Invalid tag"
    information.pop(old_tag)
    information.setdefault(new_tag, the_tag)

    #Write back to the json file after above changes
    with open(JSON_FILE, "w") as file:
        json.dump(information, file, indent=4)
    return "Tag edited successfully"
