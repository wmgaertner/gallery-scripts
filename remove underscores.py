import os

try:
    path = os.getcwd()
    for files in os.listdir(path):
        if files.endswith(".cbz"):
            filename = files
            no_underscores = filename.replace('_', ' ')
            os.rename(files, no_underscores)
except Exception as e:
    print(e)