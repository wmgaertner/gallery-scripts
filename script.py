import os, zipfile, subprocess
from pathlib import Path
from rich import print

def convert_image(source_path: Path, dest_path: Path):
    try:
        subprocess.run(["cwebp"," -lossless", "-mt", source_path, "-o", dest_path, "-quiet"], check=True)
        os.remove(source_path)
    except Exception as e:
        print(f"[red]e")
    

if __name__ == '__main__':
    try:
        cwd = os.getcwd()
        for files in os.listdir(cwd):
            if zipfile.is_zipfile(files):
                filename = files
                cbzname = filename.replace(".zip", ".cbz")
                path = os.path.join(os.getcwd(), files)
                file = zipfile.ZipFile(path, "r")
                file.extractall()

                paths = Path(".").glob("*.png")

                for image_path in paths:
                    convert_image(image_path, image_path.with_suffix(".webp"))

                cbz = zipfile.ZipFile(os.path.join(cwd, cbzname), "w")
                for files2 in os.listdir(cwd):
                    if files2.endswith('.webp') or files2.endswith('.json') or files2.endswith('.jpg'):
                        cbz.write(files2)
                        os.remove(files2)
                cbz.close()
                print(f"[green]Created: {cbzname}")

    except Exception as e:
        print(f"[red]e")