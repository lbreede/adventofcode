import os

folders = next(os.walk("day/"))[1]

for i in range(1, 26):
    if i in folders:
        continue
    os.mkdir(str(i))
