import os


fnames = []
for dirpath, dirnames, filenames in os.walk('.'):
    fnames.extend(filenames)
    # break
print(fnames)