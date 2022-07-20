import os

try:
    cwd = os.getcwd()

    for files in os.listdir(cwd):
        if files.endswith('.cbz'):
            filename = files
            cbzname = filename.replace(".cbz", ".zip")
            os.rename(files, cbzname)
except:
    print("Error")
