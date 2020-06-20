import os
from pathlib import Path


path_to_file = Path(os.path.join(os.getcwd(), 'sample.txt'))
print(path_to_file)
if path_to_file.is_file():
    print('File exists')
