from pathlib import Path

base_dir = Path.cwd() / 'reports'
if not base_dir.is_dir():
    base_dir.mkdir()

fnames = [f'{str(i).zfill(2)}_sales.txt' for i in range(1, 13)]
paths = [Path.cwd() / base_dir / f'{fname}' for fname in fnames]
for path in paths:
    path.touch()

for path in base_dir.iterdir():
    if path.is_file():
        new_name = path.stem + '.csv'
        path.rename(Path(path.parent, new_name))

