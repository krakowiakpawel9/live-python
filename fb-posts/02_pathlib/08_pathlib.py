from pathlib import Path


path = Path.cwd() / 'reports'

if not path.is_dir():
    path.mkdir()



