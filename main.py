import shutil
from pathlib import Path
import os

src = Path(
    "G:",
    "/",
    "_PROJECT FILES",
    "_Old PROJ NO's",
    "CLOSED PROJECTS",
    "COMPLETED PROJECTS",
    "1000-Bedliners",
)
dst = Path("G:\DE\Test Results Archive\XXXX-2021\Tests")

# Copies only files from src to dst
def copy_file(src, dst):
    # if not src.is_dir():
    #     shutil.copy2(str(Path(src)), dst)
    for (root, dir, files) in os.walk(src):
        for y in files:
            if ".pdf" in y.casefold() or ".xlsx" in y.casefold():
                print(y)
        print("----------------------------")


# v2
# traverses each project
for project in os.listdir(src):

    # ignore this directory
    if project == "_Non-Numbered Projects":
        break

    for (root, dir, files) in os.walk(Path(src, project)):
        # only looks at ones that has more directories to avoid double inclusion
        if dir:
            for test_dir in dir:
                if ("test" or "testing") in test_dir.casefold() and not ("hot" or "po" or "box") in test_dir.casefold():  # test_dir is now a directory that contain tests
                    org = Path(root, test_dir)
                    copy_file(org, None)
