import os
from pathlib import Path

root = "day"

folders = next(os.walk(root))[1]
print(folders)

for i in range(1, 26):
    if str(i) in folders:
        continue
    path = os.path.join(root, str(i))
    os.mkdir(path)
    path = os.path.join(path, "main.py")
    print(path)
    Path(path).touch()
