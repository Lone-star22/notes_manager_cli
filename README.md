## Notes Manager CLI

A command line program that manages notes

##Features

-Add notes
-List notes
-Search notes
-Delete notes
-Edit tags
-Command history

## Architecture
CLI
-> Validation layer
-> Operations layer
-> Storage layer

## Technologies
-Python
-argparse
-JSON

## How to run
Use the appropriate command of the intended function with arguments in the format: 'tag' or/and 'title' or/and 'content'
example: python main.py --add "machine learning" "math for ML" "this is an example"
         python main.py --delete "machine learning" "math for ML"

## Future Improvements
SQlite support
Author, favourites and ratings
Full-text search
