columns = 'Open,High,Low,Close'
first, *middle, last = columns.split(',')

print(f'first: {first} type: {type(first)}')
print(f'middle: {middle} type: {type(middle)}')
print(f'last: {last} type: {type(last)}')

