from pathlib import Path

fnames = [f'{str(i).zfill(2)}_sales' for i in range(1, 13)]
paths = [Path.cwd() / f'2020/{fname}' for fname in fnames]

t = 3
target_fnames = [f'Q{i // t}/{str(i - t + 1).zfill(2)}_sales'
                 for i in range(t, t + 12)]
target_paths = [Path.cwd() / f'2020/{fname}' for fname in target_fnames]

for target_path in target_paths:
    print(target_path)
