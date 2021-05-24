import shutil
from pathlib import Path

src = Path('G:', '/', '_PROJECT FILES', "_Old PROJ NO's", 'CLOSED PROJECTS','COMPLETED PROJECTS', '1000-Bedliners','_Non-Numbered Projects')
dst = Path('G:\DE\Test Results Archive\XXXX-2021\Tests')

# print(src)
# print(src.is_dir())

# print(dst)
# print(dst.is_dir())

for dir in src.iterdir():
    if dir.is_dir:
        for sub in dir.iterdir():
            path_string = str(Path(sub))
            if ('test' or 'testing') in (path_string.casefold()):
                if sub.is_dir():
                    for files in sub.iterdir():
                        if not files.is_dir() and ('pdf' in str(Path(files)).casefold()):
                            print(files)
                            shutil.copy2(str(Path(files)), dst)
                elif not sub.is_dir() and ('pdf' in path_string):
                    shutil.copy2(path_string, dst)