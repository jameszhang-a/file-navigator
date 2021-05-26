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
# def copy_file(src, dst=None):
#     for (root, dir, files) in os.walk(src):  # recursively traverses to each file
#         for y in files:
#             temp = y.casefold()  # to perserve the original file ending
#             if (".pdf" in temp or ".xlsx" in temp) and (
#                 "quote" not in temp
#                 and "po " not in temp
#                 and "quotation" not in temp
#                 and "qu-" not in temp
#                 and "msg" not in temp
#             ):
#                 file_path = Path(root, y)
#                 try:
#                     shutil.copy2(file_path, dst)
#                 except:
#                     unadded.append(
#                         f"PROJECT: {project} \nFILE: {y} \nPATH: {file_path}\n\n"
#                     )
#                 f.writelines([y, "\n"])


def copy_condition(filepath):
    """
    Checks to make sure only certain files are copied

    Args:
        filepath (Path): The path of the current file to be checked

    Returns:
        bool: True if passes conditions, False if fails
    """
    return True


def recur_copy(src, dst):
    """
    Recursively copies files from source directory to destination

    Args:
        src (Path): Path to orgin directory
        dst (Path): Path to desired location
    """
    for item in os.listdir(src):
        filepath = Path(src, item)

        # if filepath is a file and what we want, copy
        if os.path.isfile(filepath) and copy_condition(filepath):
            shutil.copy2(filepath, dst)

        # if filepath is another dir, recursion
        elif os.path.isdir(filepath):
            recur_copy(filepath, dst)


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
    recur_copy(project, dst)

    # for (root, dir, files) in os.walk(Path(src, project)):
    #     # only looks at ones that has more directories to avoid double inclusion
    #     if dir:
    #         for test_dir in dir:
    #             if ("test" or "testing") in test_dir.casefold() and not (
    #                 "hot" or "po" or "box"
    #             ) in test_dir.casefold():
    #                 # test_dir is now a directory that contain tests
    #                 org = Path(root, test_dir)
    #                 copy_file(org, dst)

f.write(
    "\n-------------------------------------------UNADDED-------------------------------------------\n"
)
for remaining in unadded:
    f.write(remaining)

print(f"There are {len(unadded)} files not added")
f.close()
