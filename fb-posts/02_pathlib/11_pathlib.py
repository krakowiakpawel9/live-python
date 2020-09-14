from pathlib import Path


fnames = [f'{str(i).zfill(2)}' for i in range(1, 13)]
paths = [Path.cwd() / f'reports/2020/{fname}' for fname in fnames]
for path in paths:
    print(path)

