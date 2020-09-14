from pathlib import Path


for item in Path.cwd().iterdir():
    print(item)


