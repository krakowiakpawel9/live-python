from pathlib import Path

path = Path.cwd() / 'scripts'
if not path.is_dir():
    path.mkdir()

files = [path / f'{str(i).zfill(2)}_script.py' for i in range(1, 4)]
files.append(path / 'README.md')

for file in files:
    file.touch()

for file in path.glob('*.py'):
    print(file)


