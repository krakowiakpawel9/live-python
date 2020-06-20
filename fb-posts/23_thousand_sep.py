present_value = 100_000_000
rate = 0.04
n = 5
future_value = present_value * (1 + rate) ** n
print(f'Future value: {future_value}')
print(f'Future value: {future_value:_}')
print(f'Future value: {future_value:_.2f}')
print(f'Future value: {future_value:,.2f}')


