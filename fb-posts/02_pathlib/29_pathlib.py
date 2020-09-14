from collections import Counter
from pathlib import Path

music_path = Path.cwd() / 'music'
if not music_path.is_dir():
    music_path.mkdir()

mp3_files = [music_path / f'{str(i).zfill(2)}_track.mp3' for i in range(1, 3)]
wav_files = [music_path / f'{str(i).zfill(2)}_track.wav' for i in range(1, 5)]
fnames = mp3_files + wav_files

for fname in fnames:
    fname.touch()

extensions = [path.suffix for path in music_path.iterdir()
              if path.is_file() and path.suffix]
cnt = Counter(extensions)
print(cnt)


