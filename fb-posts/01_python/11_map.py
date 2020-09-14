stocks = ['facebook', 'google', 'apple', 'microsoft']

print(list(map(lambda word: 'a' in word, stocks)))
print(list(map(lambda word: len(word), stocks)))
print(list(map(lambda word: word.upper(), stocks)))
