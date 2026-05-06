import json
try:
    with open("level_1/knowledge_tracker/data.json") as file:
        information = json.load(file)
except FileNotFoundError:
    with open("level_1/knowledge_tracker/data.json", "x") as file:
        json.dump({}, file)
    with open("level_1/knowledge_tracker/data.json") as file:
        information = json.load(file)

def add(title, content, tag):
    #Check if the all arguments have values
    if not title or not content or not tag:
        return False
    
    #creation of the needed timestamp
    from datetime import datetime as dt
    timestamp = dt.now().strftime("%H:%M:%S")
    
    collection = information.get(tag, [])

    #Update specified note if the note exists
    found_title = False
    for i in collection:
        info = i.get(title, False)
        if not info:
            continue
        new_info = f"{info[0]}. {content}"
        i[title][0] = new_info
        i[title][1] = timestamp
        found_title = True
        break
    
    #Add specified note if the note doesn't exist yet
    if not found_title:
        collection.append({title: [content, timestamp]})
    
    information[tag] = collection

    #Writing back to the json file after the above changes
    with open("level_1/knowledge_tracker/data.json", "w") as file:
        json.dump(information, file, indent=4)
        print("Note successfully added")
        return True


def view():
    #Check if data file exists
    if not information:
        return False
    
    #Print the name of the tags alongside all notes associated with them
    for tag in information:
        tags = information.get(tag)
        print(f"Tag: {tag.upper()}\nNotes:")
        title_names = get_title(tags)
        for i in sorted(title_names):
            print(f"     {i.title()}")
    return True
    

def search(title, tag):
    #Check if data file exists
    if not information:
        return False
    
    #If tag name isn't correct handle the output for a correct/incorrect title
    collection = information.get(tag)
    if not collection:
        found_title = False
        for t in information:
            tags = information.get(t)
            title_names = get_title(tags)
            if title in title_names:
                print(f"Tag: {t.title()} -- Note: {title.title()}")
                found_title = True
        if not found_title:
            return False
        return True
    
    #If tag name is correct handle the output for a correct/incorrect title 
    for note in collection:
        note_content = note.get(title)
        if not note_content:
            continue
        print(f"Title: {title.title()}    Time Created: {note_content[1]}\n\nContent: \n{note_content[0]}")
        return True
    
    title_names = get_title(collection)
    print(f"Tag: {tag.title()}\nNotes: ")
    for i in title_names:
        print(f"      {i.title()}") 
    return True 


def delete(title, tag):
    #Check if data file exists
    if not information:
        return False
    
    #Check if the tag and title of the note are correct
    collection = information.get(tag)
    if not collection:
        return False
    title_names = get_title(collection)    
    if title not in title_names:
        return False
    
    #Remove the specified note
    for i in collection:
        note = i.pop(title, None)
        if note:
            collection.remove(i)
            break
    
    #Remove tag if it isn't attached to any note again
    information[tag] = collection
    if not collection:
        information.pop(tag)

    #Write back to the json file after the above changes
    with open("level_1/knowledge_tracker/data.json", "w") as file:
        json.dump(information, file, indent=4)
    print("Note successfully deleted")
    return True


def get_title(tag_list):
    title_names = []
    for notes in tag_list:
        for title in notes:
            title_names.append(title)
    return title_names