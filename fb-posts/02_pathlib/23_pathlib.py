from pathlib import Path


path = Path.cwd() / 'sample.txt'
path.write_text('Open,High,Low,Close\n110,115,108,109')
