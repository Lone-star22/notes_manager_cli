import os
import json
from datetime import datetime as dt

BASE_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_DIR, "data.json")
TEXT_FILE = os.path.join(BASE_DIR, "command.txt")

if not os.path.exists(JSON_FILE):
    with open(JSON_FILE, "x") as file:
        json.dump({}, file)

if not os.path.exists(TEXT_FILE):
    with open(TEXT_FILE, "x") as file:
        ...

def load(history=False):
    if history:
        with open(TEXT_FILE) as file:
            for line in file:
                print(line.rstrip())
        return

    with open(JSON_FILE) as file:
        information = json.load(file)
        return information
    

def save(information=None, command=None):
    if information:
        with open(JSON_FILE, "w") as file:
            json.dump(information, file, indent=4)
    
    if command:
        with open(TEXT_FILE, "a") as file:
            file.write(f"Command: {command} -- Time: {dt.now().strftime("%Y-%m-%d %H:%M:%S")}\n")
    