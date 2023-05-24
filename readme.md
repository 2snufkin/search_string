# search_string
a python based app with UI that let you search a string inside a folder

## How to
when running the app you will be asked:
search_path: the folder that contains the files in which you want to search the string
File type: the file extention, this is optional. If you don't fill it it will look in all the files without filtering

At the end of the search a list of all the found files are copy to the clipboard

you can build the app with pyinstaller
1. pip install pyinstaller
2. if you want only exe file: pyinstaller --onefile search_inside_file.py 
otherwise: pyinstaller  search_inside_file.py

