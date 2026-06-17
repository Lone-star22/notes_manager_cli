from datetime import datetime as dt


class Note:
    def __init__(self, tag=None, title=None, content=None):
        self.tag = tag
        self.title = title
        self.content = content

class NotesManager: 
    def __init__(self):
        pass

    def add(self, note, information):
        #creation of the needed timestamp
        timestamp = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        
        #Add note if it doesn't exist else update the existing one
        the_tag = information.get(note.tag, {})
        the_note = the_tag.get(note.title, {})
        if not the_note:
            the_tag[note.title] = {"content": note.content, "date": timestamp}
        else:
            the_note["content"] = f"{the_note['content']}. {note.content}"
            the_note["date"] = timestamp
        information[note.tag] = the_tag
        return information
    
    
    def search(self, note, information):
        #Handle output for user's search
        the_tag = information.get(note.tag, {})
        if not the_tag:
            return "Invalid tag"
        the_note = the_tag.get(note.title, {})
        if not the_note:
            return "Invalid title"
        return f"Tag: {note.tag.title()}    Title: {note.title.title()}    Date Created: {the_note['date']}\n\nContent: \n{the_note['content']}"
    
    
    def delete(self, note, information):
        #Handle user input
        the_tag = information.get(note.tag, {})
        if not the_tag:
            return False
        the_note = the_tag.get(note.title, {})
        if not the_note:
            return False
        information[note.tag].pop(note.title)
        if not information[note.tag]:
            information.pop(note.tag)
        return information
    

    def view(self, information):
        #Print the name of the tags alongside all notes associated with them
        max_count, max_tag = 0, None
        for tag in information:
            print(f"Tag: {tag.upper()}\nNotes:")
            if len(information[tag]) > max_count:
                max_count = len(information[tag])
                max_tag = tag
            for title in sorted(information[tag]):
                print(f"     {title.title()}")
        print(f"Most Used Tag: {max_tag} -- Number of Times: {max_count}") 

    
    def edit_tag(self, note, information, new_tag):
        #Change the name of the current tag to that of new tag
        the_tag = information.pop(note.tag, {})
        if not the_tag:
            return False
        information[new_tag] = the_tag
        return information