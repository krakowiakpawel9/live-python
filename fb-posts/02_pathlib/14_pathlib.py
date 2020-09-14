from pathlib import Path


path = Path.cwd() / 'hello.txt'

if not path.is_file():
    path.write_text('Open,High,Low,Close')

content = path.read_text()
print(content)
