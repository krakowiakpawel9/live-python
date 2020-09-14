from pathlib import Path
from shutil import copyfile


source_path = Path.cwd() / 'quotations.txt'
source_path.write_text('Open,High,Low,Close\n110,115,108,109')

destination_path = Path('quotations_copy.txt')

copyfile(source_path, destination_path)



