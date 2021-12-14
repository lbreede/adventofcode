import argparse
import json
from pathlib import Path
import os

parser = argparse.ArgumentParser(
	description="Create template py file from day number.")
parser.add_argument("day", type=int, help="Day")
args = parser.parse_args()

def create_file(day):
	with open("template.txt", "r") as f:
		raw_txt = f.read()

	with open("chapters.json", "r") as f:
		chapters = json.load(f)

	daypad = str(day).zfill(2)
	chapter = chapters[str(day)]
	txt = raw_txt.format(day=day, chapter=chapter, daypad=daypad)	

	name = "day" + daypad
	ext = [".py", "_input.txt", "_example.txt"]
	txt = [txt, "", ""]

	for i in range(3):
		path = "/".join(str(Path().parent.absolute()).split("\\")[:-1])
		filename = name + ext[i]
		path = path + "/" + filename

		if not os.path.isfile(path):
			with open(path, "w") as f:
				f.write(txt[i])

			print(f"Created {filename}")

		else:
			print(f"{filename} already exists.")

if __name__ == "__main__":
	create_file(args.day)