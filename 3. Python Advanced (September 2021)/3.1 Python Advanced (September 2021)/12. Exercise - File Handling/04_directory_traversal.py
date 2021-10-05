import os
import sys

if sys.platform.startswith("win"):
    #  Windows
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    report_file = f"{desktop}\\report.txt"
else:
    # Linux and MacOS
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    report_file = f"{desktop}/report.txt"
all_files = {}

path_to_traverse = input()
path = os.walk(path_to_traverse)
for _, _, files in path:
    for file in files:
        extension = f".{file.split('.')[-1]}"
        if extension not in all_files:
            all_files[extension] = []
        all_files[extension].append(file)

with open(report_file, "w") as f:
    for extension, files in sorted(all_files.items()):
        f.write(f"{extension}\n")
        for file in sorted(files):
            f.write(f"- - - {file}\n")
