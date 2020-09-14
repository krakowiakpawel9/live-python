from pathlib import Path


path = Path.cwd() / f'reports/2020/01'
if not path.is_dir():
    path.mkdir(parents=True)

target = Path.cwd() / f'reports/2020/01_sales'
path.rename(target)

