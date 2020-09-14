from pathlib import Path


fnames = [f'music/playlist_{str(i).zfill(2)}' for i in range(1, 7)]
paths = [Path.cwd() / f'{fname}' for fname in fnames]

for path in paths:
    path.mkdir(parents=True)
    print(path)

