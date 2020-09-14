stocks_1 = ['PLW', 'CDR', 'TEN', 'BBT', '11B']
stocks_2 = ['CDR', 'TEN']

set_1 = set(stocks_1)
set_2 = set(stocks_2)

result = list(set_1.symmetric_difference(set_2))
print(result)
