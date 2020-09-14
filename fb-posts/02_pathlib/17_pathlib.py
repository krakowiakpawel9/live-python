from pathlib import Path


fnames = [f'{str(i).zfill(2)}' for i in range(1, 13)]
paths = [Path.cwd() / f'reports/{fname}_sales' for fname in fnames]

for path in paths:
    path.mkdir(parents=True)

for item in Path.cwd().joinpath('reports').iterdir():
    print(item)
