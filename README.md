# Personal scripts I use to manage downloaded manga for local komga server

## Script.py

### What this does
Unzips every zip folder in the directory, converts png images to webp losslessly, deletes the extracted png files, then rezips the webp images (and .json) into a .cbz folder

### Requirements
* python3
* cwebp added to PATH (https://developers.google.com/speed/webp/download)
### How to use
1. Drop script.py and requirements.txt in the same directory as your zips
2. Run `pip install -r requirements.txt` in terminal
3. Run `python script.py` in terminal
