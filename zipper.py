import zipfile
import pathlib

def zipper(filepaths,folderpath):
    folderpath=pathlib.Path(folderpath,"compressed.zip")
    with zipfile.ZipFile(folderpath,'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

if __name__=='__main__':
    zipper(filepaths=['__init__.py', 'avgoftemp'],
           folderpath="destination")

