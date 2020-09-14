from pathlib import Path

path = Path.cwd() / 'music'
if not path.is_dir():
    path.mkdir()

mp3_files = [path / f'{str(i).zfill(2)}_track.mp3' for i in range(1, 3)]
wav_files = [path / f'{str(i).zfill(2)}_track.wav' for i in range(1, 5)]
fnames = mp3_files + wav_files

for fname in fnames:
    fname.touch()

for file in path.glob('*.mp3'):
    print(file)



