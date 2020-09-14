dates = ['01012020', '02012020', '03012020']
quotes = [195.5, 192.1, 193.5, 194.0]

for date, price in zip(dates, quotes):
    print(f'Date: {date} Price: {price}')

print(list(zip(dates, quotes)))
