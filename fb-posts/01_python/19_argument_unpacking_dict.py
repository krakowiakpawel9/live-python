def print_args(var1, var2, var3):
    print(f'var1: {var1}\nvar2: {var2}\nvar3: {var3}')


variables = {'var3': 3.0, 'var2': 4.0, 'var1': 5.0}
print_args(**variables)

