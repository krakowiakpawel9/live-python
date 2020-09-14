from pathlib import Path


path = Path.home() / 'reports/2020/01/sales.csv'
print(path)
print(path.parent)
print(path.parent.parent)
print(path.parent.parent.parent)

