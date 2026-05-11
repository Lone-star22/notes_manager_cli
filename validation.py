def validation(tag=False, title=False, new_tag=False, information=False):
    if tag:
        if len(tag) > 15:
            return False
    if title:
        if len(title) > 15:
            return False  
    if new_tag:
        if len(new_tag) > 15:
            return False
    if information != False:
        if type(information) != dict:
            return False
        for tags in information:
            if type(information[tags]) != dict:
                return False
            for titles in information[tags]:
                if type(information[tags][titles]) != dict:
                    return False   
                if len(information[tags][titles]) != 2:
                    return False
                if "content" not in information[tags][titles].keys() or "date" not in information[tags][titles].keys():
                    return False
    return True