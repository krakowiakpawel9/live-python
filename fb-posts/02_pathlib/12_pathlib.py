from pathlib import Path


fnames = [f'{str(i).zfill(2)}' for i in range(1, 13)]
paths = [Path.cwd() / f'reports/2020/{fname}' for fname in fnames]

for path in paths:
    path.mkdir(parents=True)

reports_2020 = Path.cwd() / 'reports/2020'
for dir_name in reports_2020.iterdir():
    print(dir_name)





