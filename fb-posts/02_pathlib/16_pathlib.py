from pathlib import Path


fnames = [f'{str(i).zfill(2)}' for i in range(1, 13)]
paths = [Path.cwd() / f'reports/2020/{fname}' for fname in fnames]

for path in paths:
    path.mkdir(parents=True)

targets = [Path.cwd() / f'reports/2020/{fname}_sales' for fname in fnames]

for path, target in zip(paths, targets):
    path.rename(target)
