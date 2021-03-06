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

dst = Path(
    "G:",
    "/",
    "DE",
    "Test Results Archive",
    "XXXX-2021",
    "Tests",
)


# Copies only files from src to dst
def copy_file(src, dst=None):
    for (root, dir, files) in os.walk(src):  # recursively traverses to each file
        for y in files:
            temp = y.casefold()  # to perserve the original file ending
            if (".pdf" in temp or ".xlsx" in temp) and (
                "quote" not in temp
                and "po " not in temp
                and "quotation" not in temp
                and "qu-" not in temp
                and "msg" not in temp
            ):
                file_path = Path(root, y)
                try:
                    shutil.copy2(file_path, dst)
                except:
                    unadded.append(f"PROJECT: {project} \nFILE: {y} \nPATH: {file_path}\n\n")
                f.writelines([y, "\n"])

# Logs the process
f = open("log.txt", "w")
unadded = []

# v2
# traverses each project
for project in os.listdir(src):

    # ignore this directory
    if project == "_Non-Numbered Projects":
        break

    f.writelines(
        [
            "\n-------------------------------------------",
            project,
            ": -------------------------------------------",
            "\n",
        ]
    )
    for (root, dir, files) in os.walk(Path(src, project)):
        # only looks at ones that has more directories to avoid double inclusion
        if dir:
            for test_dir in dir:
                if ("test" or "testing") in test_dir.casefold() and not (
                    "hot" or "po" or "box"
                ) in test_dir.casefold():
                    # test_dir is now a directory that contain tests
                    org = Path(root, test_dir)
                    copy_file(org, dst)

f.write(
        "\n-------------------------------------------UNADDED-------------------------------------------\n"
    )
for remaining in unadded:
    f.write(remaining)

print(f'There are {len(unadded)} files not added')
f.close()
