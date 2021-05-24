import shutil
from pathlib import Path

# experiment_dir = Path.joinpath(Path.cwd(), 'Experiment')
# print(experiment_dir)

# file1 = Path.joinpath(experiment_dir, '1', 'file1.txt')

src = Path('G:', '/', '_PROJECT FILES', "_Old PROJ NO's", 'CLOSED PROJECTS','COMPLETED PROJECTS', '1000-Bedliners','_Non-Numbered Projects')
dst = Path('G:\DE\Test Results Archive\XXXX-2021')

# shutil.move(file1, Path.joinpath(experiment_dir,'2'))
# shutil.move(dst, file1)

print(src)
print(src.is_dir())

print(dst)
print(dst.is_dir())