def file_gen(files):
    for file in files:
        yield file


fnames = ['view.jpg', 'bear.png', 'logo.png']

for fname in file_gen(fnames):
    print(fname)

gen = file_gen(fnames)
print(next(gen))
