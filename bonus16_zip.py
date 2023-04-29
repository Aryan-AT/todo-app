import pathlib
import zipfile

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "Compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

if __name__ == "__main__":
    make_archive(filepaths=["all txt/a.txt"], dest_dir="all txt")