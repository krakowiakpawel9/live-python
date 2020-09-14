stocks = ['facebook', 'google', 'apple', 'microsoft', 'sas']

print(list(filter(lambda name: 'a' in name, stocks)))
print(list(filter(lambda name: len(name) > 6, stocks)))
print(list(filter(lambda name: name == name[::-1], stocks)))
