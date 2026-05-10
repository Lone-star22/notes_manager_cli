from datetime import datetime as dt
from storage import save


class Note: 
    def __init__(self, tag=None, title=None, content=None):
        self.tag = tag
        self.title = title
        self.content = content
    
    def add(self, information):
        #creation of the needed timestamp
        timestamp = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        
        #Add note if it doesn't exist else update the existing one
        the_tag = information.get(self.tag, {})
        note = the_tag.get(self.title, {})
        if not note:
            the_tag[self.title] = {"content": self.content, "date": timestamp}
        else:
            note["content"] = f"{note['content']}. {self.content}"
            note["date"] = timestamp
        information[self.tag] = the_tag
        
        #Writing back to the json file after the above changes
        save(information)
        return "Note added succesfully"
    
    def search(self, information):
        #Check if data file exists
        if not information:
            return "No notes to search"
        
        #Handle output for user's search
        the_tag = information.get(self.tag, {})
        if not the_tag:
            return "Invalid tag"
        note = the_tag.get(self.title, {})
        if not note:
            return "Invalid title"
        return f"Tag: {self.tag.title()}    Title: {self.title.title()}    Date Created: {note["date"]}\n\nContent: \n{note["content"]}"
    
    def delete(self, information):
        #Check if data file exists
        if not information:
            return "No notes to delete"    

        #Handle user input
        the_tag = information.get(self.tag, {})
        if not the_tag:
            return "Invalid tag"
        note = the_tag.get(self.title, {})
        if not note:
            return "Invalid title"
        information[self.tag].pop(self.title)
        if not information[self.tag]:
            information.pop(self.tag)


        #Write back to the json file after the above changes
        save(information)
        return "Successfully deleted"

    def view(self, information):
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
        print(f"Most Used Tag: {max_tag.title()} -- Number of Times: {max_count}") 
    
    def edit_tag(self, information, new_tag):
        #Check if information, current tag and new tag exists
        if not information:
            return "No tags to edit"
        
        #Change the name of the current tag to that of new tag
        the_tag = information.get(self.tag, {})
        if not the_tag:
            return "Invalid tag"
        information.pop(self.tag)
        information.setdefault(new_tag, the_tag)

        #Write back to the json file after above changes
        save(information)
        return "Tag edited successfully"