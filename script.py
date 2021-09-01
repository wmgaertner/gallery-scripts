import os, zipfile
from subprocess import Popen



try:
    cwd = os.getcwd()
    for files in os.listdir(cwd):
        if zipfile.is_zipfile(files):
            filename = files
            cbzname = filename.replace(".zip", ".cbz")
            path = os.path.join(os.getcwd(), files)
            file = zipfile.ZipFile(path, "r")
            file.extractall()

            p = Popen(os.path.join(cwd, "convert png to webp.bat"))
            stdout, stderr = p.communicate()
            p.kill()

            cbz = zipfile.ZipFile(os.path.join(cwd, cbzname), "w")
            for files2 in os.listdir(cwd):
                if files2.endswith('.webp') or files2.endswith('.json'):
                    cbz.write(files2)
                    os.remove(files2)
            cbz.close()
            


except Exception as e:
    print(e)