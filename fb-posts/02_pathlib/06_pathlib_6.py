from pathlib import Path


path = Path.home() / 'reports/2020/01/sales.csv'
print(path.parts)

for part in path.parts:
    print(part)

