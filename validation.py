def validation(tag=None, title=None, new_tag=None, information=None):
    if tag:
        if len(tag) > 20:
            return False
    if title:
        if len(title) > 20:
            return False  
    if new_tag:
        if len(new_tag) > 20:
            return False
    if information is not None:
        if not isinstance(information, dict):
            return False
        for tags in information:
            if not isinstance(information[tags], dict):
                return False
            for titles in information[tags]:
                if not isinstance(information[tags][titles], dict):
                    return False   
                required = {"content", "date"}
                if not required.issubset(information[tags][titles].keys()):
                    return False
    return True