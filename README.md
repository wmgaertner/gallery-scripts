# Personal scripts I use to manage downloaded manga for local komga server

All scripts written in python 3.10.5

## Script.py

### What this does
Unzips every zip folder in the directory, converts png images to webp losslessly, deletes the extracted png files, then rezips the webp images (and .json) into a .cbz folder

### Requirements
* cwebp added to PATH (https://developers.google.com/speed/webp/download)
### How to use
1. Drop script.py and requirements.txt in the same directory as your zips
2. Run `pip install -r requirements.txt` in terminal
3. Run `python script.py` in terminal

## remove underscores.py

### What this does
As the name implies, replaces underscores found in filenames with spaces


### How to use
1. Drop file in same location as files to rename and run in terminal

## cbz to zip.py

### What this does
Converts cbz folders to zips to use before the main script.py


### How to use
1. Drop file in same location as cbz folders to convert and run in terminal