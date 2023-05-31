import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir,'compressed.zip')
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)   
            archive.write(filepath, arcname=filepath.name)

if __name__  == '__main__':
    print("Hello")
    
    
    ## For checking = make_archive(filepaths=['bonus1.py', 'bonus2.py'], dest_dir="dest")